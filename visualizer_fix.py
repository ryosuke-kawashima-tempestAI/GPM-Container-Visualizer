import pandas as pd

def get_log_edges(df_pd3, df_GPM, GPM_graph, GPM_descendants, LLD_Logs = "Log", LLD_IDs = "Action ID", GPM_IDs="ClassID", GPM_Inputs="ClassInput", GPM_Names="ClassName", GPM_Outputs="ClassOutput", GPM_Parents="PartOf") -> list:
    """
    Identifies edges (transitions) between GPM actions based on sequence in LLD Logs.
    Handles hierarchy by finding edges between children of the lowest common ancestor container.
    """
    # Group by Log to iterate over each trace sequence
    # This creates a GroupBy object where keys are Log IDs and values are DataFrames of that trace
    df_each_log_group = df_pd3.groupby(LLD_Logs)
    
    log_edges = set()
    
    # Iterate through each log trace
    for log_id, df_log in df_each_log_group:
        df_log = df_log.reset_index(drop=True)
        # Iterate through the sequence of actions in this log
        for index in range(len(df_log) - 1):
            from_action = df_log.at[index, LLD_IDs]
            to_action = df_log.at[index + 1, LLD_IDs]
            
            # Helper to get GPM info safely
            def get_gpm_info(lld_id):
                rows = df_GPM[df_GPM[GPM_IDs] == lld_id]
                if len(rows) == 0: return None, None
                return rows[GPM_IDs].values[0], rows[GPM_Parents].values[0]

            gpm_from, parent_from = get_gpm_info(from_action)
            gpm_to, parent_to = get_gpm_info(to_action)

            if gpm_from is None or gpm_to is None:
                continue

            # Logic: If they share the same parent, draw edge between them.
            # If not, climb up hierarchy until we find the level where they share a parent (common container).
            # Draw edge between the children of that common container.
            
            if parent_from == parent_to:
                log_edges.add((gpm_from, gpm_to))
            else:
                curr_from_node = gpm_from
                curr_to_node = gpm_to
                curr_from_parent = parent_from
                curr_to_parent = parent_to
                
                # Climb up
                found_common = False
                # Max depth safety
                for _ in range(10): 
                    # If parents match (Common Container found), link the current nodes
                    if curr_from_parent == curr_to_parent:
                        log_edges.add((curr_from_node, curr_to_node))
                        found_common = True
                        break
                    
                    # Move up one level
                    # Get grandparent for from
                    row_parent_from = df_GPM[df_GPM[GPM_IDs] == curr_from_parent]
                    if len(row_parent_from) == 0: break
                    grand_from = row_parent_from[GPM_Parents].values[0]
                    
                    # Get grandparent for to
                    row_parent_to = df_GPM[df_GPM[GPM_IDs] == curr_to_parent]
                    if len(row_parent_to) == 0: break
                    grand_to = row_parent_to[GPM_Parents].values[0]

                    # Update references to move up
                    # The edge will be drawn between the nodes *just below* the common parent
                    curr_from_node = curr_from_parent
                    curr_to_node = curr_to_parent
                    curr_from_parent = grand_from
                    curr_to_parent = grand_to

    return log_edges
