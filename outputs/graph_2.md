
classDiagram
    direction LR

    %% LLD Actions

        class LLD_37["LLD_37: 目視や手触りによる外観チェックで300Dトルーフの不具合を観察する"] {
            Input: 治具にセット済みの300Dトルーフ
            Output: 300Dトルーフの１打点目がパネルズレがあり、
打点すると位置ズレが起こる
        }
        

        class LLD_38["LLD_38: 部品の1打点目のパネルズレ（隙間）を測定する"] {
            Input: 300Dトルーフの１打点目がパネルズレがあり、
打点すると位置ズレが起こる
            Output: 測定結果：300Dトルーフの1打点目の隙間：5mm
        }
        

        class LLD_39["LLD_39: 300Dトルーフがどんな不具合があるのかを判断する"] {
            Input: 測定結果：300Dトルーフの1打点目の隙間：5mm
            Output: 300Dトルーフの1打点目に隙間が発生した
        }
        

        class LLD_40["LLD_40: 隙間の原因を推定する"] {
            Input: 300Dトルーフの1打点目に隙間が発生した
            Output: 推定した原因：
隙間の発生は治具の固定に関係する
        }
        

        class LLD_41["LLD_41: クランプを使い、300Dトルーフの治具の固定に問題ないかを繰り返し調べる"] {
            Input: 推定した原因：
隙間の発生は治具の固定に関係する
            Output: クランプでと止めた300Dトルーフ
        }
        

        class LLD_42["LLD_42: 300Dトルーフの三次元形状を測定する"] {
            Input: クランプでと止めた300Dトルーフ
            Output: 測定結果：300Dトルーフの1打点目の隙間：5mm
        }
        

        class LLD_43["LLD_43: 300Dトルーフ部品に隙間の発生は治具の固定に関係したかを判断する"] {
            Input: 測定結果：300Dトルーフの1打点目の隙間：5mm
            Output: 300Dトルーフ隙間の発生は治具の固定に関係なし
        }
        

        class LLD_44["LLD_44: 推定した隙間発生の原因が正しいかを判断する"] {
            Input: 300Dトルーフ隙間の発生は治具の固定に関係なし
            Output: 推定した原因が正しくない
        }
        

        class LLD_45["LLD_45: 300Dトルーフの隙間発生の原因を推定する"] {
            Input: 推定した原因が正しくない
            Output: 推定した原因：300Dトルーフ隙間の発生
は部品の単体精度に関係する
        }
        

        class LLD_46["LLD_46: 5Nの荷重をかけた時の300Dトルーフ単品の形状変位量を解析する"] {
            Input: 推定した原因：300Dトルーフ隙間の発生
は部品の単体精度に関係する
            Output: 5Nの荷重をかけた時の300Dトルーフ単品の形状変位量：T＝0.7
変位量データ(荷重パターン)
x方向変位量：-1.39mm
y方向変位量：1.03mm
z方向変位量：-0.55mm
300D-61697,8において基準穴付近の剛性不足
        }
        

        class LLD_47["LLD_47: 300Dトルーフ部品に隙間の発生は単体精度に関係したかを判断する"] {
            Input: 5Nの荷重をかけた時の300Dトルーフ単品の形状変位量：T＝0.7
変位量データ(荷重パターン)
x方向変位量：-1.39mm
y方向変位量：1.03mm
z方向変位量：-0.55mm
300D-61697,8において基準穴付近の剛性不足
            Output: 300D-61697,8において基準穴付近の
剛性不足のため、
隙間の発生は300Dトルーフの
部品の単体精度に関係する
        }
        

        class LLD_48["LLD_48: 推定した隙間発生の原因が正しいかを判断する"] {
            Input: 300D-61697,8において基準穴付近の
剛性不足のため、
隙間の発生は300Dトルーフの
部品の単体精度に関係する
            Output: 推定した原因が正しい
        }
        

        class LLD_49["LLD_49: 300Dトルーフの隙間発生の原因を推定する"] {
            Input: 推定した原因が正しい
            Output: 推定した原因：300Dトルーフ隙間の発生
は部品の基準設定に関係する
        }
        

        class LLD_50["LLD_50: 300Dトルーフ単品の基準数が適切なのかを調べる"] {
            Input: 推定した原因：300Dトルーフ隙間の発生
は部品の基準設定に関係する
            Output: 300Dトルーフ単品の基準数が問題なし
        }
        

        class LLD_51["LLD_51: 300Dトルーフ単品の基準位置が適切なのかを調べる"] {
            Input: 300Dトルーフ単品の基準数が問題なし
            Output: 固定用副基準の追加が必要
        }
        

        class LLD_52["LLD_52: 300Dトルーフ部品に隙間の発生は単体精度に関係したかを判断する"] {
            Input: 固定用副基準の追加が必要
            Output: 300Dトルーフ隙間の発生は
部品の基準設定に関係する
        }
        

        class LLD_53["LLD_53: 推定した隙間発生の原因が正しいかを判断する"] {
            Input: 300Dトルーフ隙間の発生は
部品の基準設定に関係する
            Output: 推定した原因が正しい
        }
        

        class LLD_54["LLD_54: 不具合が発生しうるサブプロセスから一つのサブプロセスを選ぶ"] {
            Input: 推定した原因が正しい
            Output: 選択したサブプロセス：
300Dトルーフの単体精度不良
        }
        

        class LLD_55["LLD_55: 選択されたサブプロセスに対して隙間の解消案を立案する"] {
            Input: 選択したサブプロセス：
300Dトルーフの単体精度不良
            Output: 300Dトルーフのパネル形状を変更する
        }
        

        class LLD_56["LLD_56: 300Dトルーフ単品の形状変更の位置を決める"] {
            Input: 300Dトルーフのパネル形状を変更する
            Output: 300Dトルーフの形状変更位置：トリムライン
        }
        

        class LLD_57["LLD_57: 300Dトルーフ単品の形状変更の形を決める"] {
            Input: 300Dトルーフの形状変更位置：トリムライン
            Output: トリムライン形状変更案
        }
        

        class LLD_58["LLD_58: トリムライン形状変更案を実行する"] {
            Input: トリムライン形状変更案
            Output: トリムライン形状変更後の300Dトルーフ
        }
        

        class LLD_59["LLD_59: トリムライン形状変更後、5Nの荷重をかけた時の300Dトルーフ単品の形状変位量を解析する"] {
            Input: トリムライン形状変更後の300Dトルーフ
            Output: トリムライン変更後
形状変位量測定結果(荷重パターン)
x方向変位量：-1.19mm
y方向変位量：0.91mm
z方向変位量：-0.47mm変更前の変位量データ(荷重パターン)
x方向変位量：-1.39mm
y方向変位量：1.03mm
z方向変位量：-0.55mm
        }
        

        class LLD_60["LLD_60: トリムラインの形状変更による効果を評価する"] {
            Input: トリムライン変更後
形状変位量測定結果(荷重パターン)
x方向変位量：-1.19mm
y方向変位量：0.91mm
z方向変位量：-0.47mm変更前の変位量データ(荷重パターン)
x方向変位量：-1.39mm
y方向変位量：1.03mm
z方向変位量：-0.55mm
            Output: 形状変更前後、5Nをかける際変位量の差があまりないため、
形状変更の効果がない
        }
        

        class LLD_61["LLD_61: 不具合が発生しうるサブプロセスから一つのサブプロセスを選ぶ"] {
            Input: 形状変更前後、5Nをかける際変位量の差があまりないため、
形状変更の効果がない
            Output: 選択されたサブプロセス：300Dトルーフの基準設定
        }
        

        class LLD_62["LLD_62: 300Dトルーフの基準設定に対して隙間の解消案を立案する"] {
            Input: 選択されたサブプロセス：300Dトルーフの基準設定
            Output: 固定用W副基準の追加
        }
        

        class LLD_63["LLD_63: 300Dトルーフ単品の固定用W副基準の位置を決める"] {
            Input: 固定用W副基準の追加
            Output: 固定用W副基準の位置：SQ05C
        }
        

        class LLD_64["LLD_64: 300Dトルーフ単品の固定用W副基準の構造を決める"] {
            Input: 固定用W副基準の位置：SQ05C
            Output: 固定用W副基準の構造：シム構造
        }
        

        class LLD_65["LLD_65: 300Dトルーフ単品のSQ05Cにシム構造のW副基準を設定する"] {
            Input: 変更前の300Dトルーフ
            Output: SQ05Cにシム構造のW副基準
を追加した300Dトルーフ単品
        }
        

        class LLD_66["LLD_66: 部品を組み付ける"] {
            Input: SQ05Cにシム構造のW副基準
を追加した300Dトルーフ単品
            Output: 組み付けた部品
        }
        

        class LLD_67["LLD_67: 部品の1打点目のパネルズレ（隙間）を測定する"] {
            Input: 組み付けた部品
            Output: 部品の1打点目の隙間：0.7mm(仮)
        }
        

        class LLD_68["LLD_68: 部品の1打点目の隙間が解消したかを評価する"] {
            Input: 部品の1打点目の隙間：0.7mm(仮)
            Output: 部品の1打点目の隙間が解消した
        }
        

        class LLD_69["LLD_69: 300Dトルーフ単品のSQ05Cにシム構造のW副基準の追加による前後工程への影響を調べる"] {
            Input: 300Dトルーフの1打点目の隙間が解消した
            Output: 前後工程への影響なし
        }
        

        class LLD_70["LLD_70: 300Dトルーフ単品のSQ05Cにシム構造のW副基準の追加によるコストを評価する"] {
            Input: 前後工程への影響なし
            Output: コストOK
        }
        

        class LLD_71["LLD_71: 300Dトルーフ単品のSQ05Cにシム構造のW副基準を設定する"] {
            Input: コストOK
            Output: 固定用副基準追加後
の300Dトルーフ部品
        }
        

        class LLD_72["LLD_72: 部品の組み付けに問題ないかを観察する"] {
            Input: 固定用副基準追加後
の300Dトルーフ部品
            Output: 不具合なし
        }
        

    %% GPM Actions

        class GPM_1["GPM_1: 現状を計測・評価する"] {
            Input: ワーク/組付け体、測定計画・図面
            Output: 現状評価結果（変位/隙間/外観）
        }
        

        class GPM_2["GPM_2: 原因を解析・検証する"] {
            Input: 現状評価結果、現場所見/測定・解析データ
            Output: 原因仮説と検証結果（正否）
        }
        

        class GPM_3["GPM_3: 対策方針を策定する"] {
            Input: 原因・制約情報、改善目標
            Output: 対策方針・優先順位
        }
        

        class GPM_4["GPM_4: 基準を見直す（変更・追加）"] {
            Input: 対策方針、設備制約/可動性情報
            Output: 見直し設計・実装（位置/構造/追加）
        }
        

        class GPM_5["GPM_5: 形状を変更する（プレス/金型）"] {
            Input: 対策方針、成形性・品質制約
            Output: 形状変更仕様・改修計画
        }
        

        class GPM_6["GPM_6: 溶接計画を最適化する"] {
            Input: 変形/品質課題、現行溶接計画
            Output: 最適化案・更新された溶接計画
        }
        

        class GPM_7["GPM_7: 現物をセット・調整する"] {
            Input: 部品、治具、締付設備
            Output: セット・調整完了状態
        }
        

        class GPM_8["GPM_8: 製造を実施する"] {
            Input: 製造計画、設備/治具
            Output: 製造された部品/サンプル
        }
        

        class GPM_9["GPM_9: 実施可否を判断する"] {
            Input: 効果評価、影響評価、コスト評価
            Output: 実施/保留の意思決定
        }
        

        class GPM_10["GPM_10: 目視・触診で外観を確認する"] {
            Input: 対象部品・組付け体
            Output: 外観所見（打痕/干渉/歪み）
        }
        

        class GPM_11["GPM_11: 組み付け状態を観察する"] {
            Input: 組付け体（仮組含む）
            Output: 異常所見（当たり/ガタ/位置ずれ）
        }
        

        class GPM_12["GPM_12: 三次元形状を測定する"] {
            Input: 治具にセット済みワーク、測定計画
            Output: 形状点群/寸法データ
        }
        

        class GPM_13["GPM_13: CADとの差分カラーマップを作成する"] {
            Input: 三次元形状データ、CADモデル
            Output: 差分カラーマップ/偏差分布
        }
        

        class GPM_14["GPM_14: 隙間量を測定する"] {
            Input: 組付け体、隙間ゲージ/三次元測定機
            Output: 隙間量データ
        }
        

        class GPM_15["GPM_15: 溶接後の寸法精度を測定する"] {
            Input: 溶接済み部品、測定基準
            Output: 寸法測定データ（溶接影響含む）
        }
        

        class GPM_16["GPM_16: 穴径・面精度を測定する"] {
            Input: プレス/加工品、ゲージ/三次元測定機
            Output: 穴径・面位置データ
        }
        

        class GPM_17["GPM_17: 単体精度を評価する"] {
            Input: 単体測定結果、基準値/公差
            Output: 合否/偏差評価
        }
        

        class GPM_18["GPM_18: 形状データから状態を評価・判定する"] {
            Input: 測定・差分データ
            Output: 不具合部位・変位量・判定結果
        }
        

        class GPM_19["GPM_19: 公差適合性を確認する"] {
            Input: 測定データ、公差情報/図面
            Output: 公差内/外の判定結果
        }
        

        class GPM_20["GPM_20: 不具合有無を最終確認する"] {
            Input: 全評価結果・判定基準
            Output: 最終の不具合有無（OK/NG）
        }
        

        class GPM_21["GPM_21: 精度データを準備する"] {
            Input: 図面、公差、測定条件・治具情報
            Output: 測定・評価用データセット
        }
        

        class GPM_22["GPM_22: 原因を推定する"] {
            Input: 評価結果・所見、制約/工程情報
            Output: 推定原因リスト（仮説）
        }
        

        class GPM_23["GPM_23: CAEで剛性・変位を解析する"] {
            Input: CAD/メッシュ、荷重・拘束条件
            Output: 変位/剛性/荷重-変位解析結果
        }
        

        class GPM_24["GPM_24: 治具干渉箇所を解析する"] {
            Input: 実測下がり量/3Dデータ、治具構造情報
            Output: 干渉疑い箇所/下がり比較結果
        }
        

        class GPM_25["GPM_25: 干渉の有無を簡易確認する"] {
            Input: 現物治具・部品、当たり/抜け確認手段
            Output: 干渉有無の所見
        }
        

        class GPM_26["GPM_26: 基準穴周辺の剛性を評価する"] {
            Input: 実測/解析データ、基準周辺条件
            Output: 剛性評価（弱点/影響度）
        }
        

        class GPM_27["GPM_27: 推定原因の正否を判断する"] {
            Input: 推定原因、追加測定/解析結果
            Output: 正/否判定と根拠
        }
        

        class GPM_28["GPM_28: 不具合の解決対象を選定する"] {
            Input: 不具合影響度、納期・コスト、リスク
            Output: 優先度付き解決対象リスト
        }
        

        class GPM_29["GPM_29: サブプロセスを選定する"] {
            Input: 対象工程候補、改善目的
            Output: 着手工程の選定結果
        }
        

        class GPM_30["GPM_30: 対策案を立案する"] {
            Input: 原因・制約、改善目標
            Output: 対策案（基準/形状/工程/溶接）
        }
        

        class GPM_31["GPM_31: 基準群・基準関係を同定する"] {
            Input: 図面/工程情報、現物治具
            Output: 基準リスト/関係整理
        }
        

        class GPM_32["GPM_32: 基準の可動性・制約を確認する"] {
            Input: 設備仕様・図面、冶具機構情報
            Output: 可動/固定・制約条件一覧
        }
        

        class GPM_33["GPM_33: 基準位置を決定する"] {
            Input: 制約/CG/設備条件、可動範囲
            Output: 目標基準位置案
        }
        

        class GPM_34["GPM_34: 基準構造を決定する"] {
            Input: 干渉/剛性/固定性要件、治具制約
            Output: 基準構造仕様（ピン/シム/異形）
        }
        

        class GPM_35["GPM_35: 基準位置を変更する（実装）"] {
            Input: 目標位置・変更手順、治工具
            Output: 変更済み基準（位置更新）
        }
        

        class GPM_36["GPM_36: 基準追加案を立案する"] {
            Input: 固定性課題、治具構成、制約
            Output: 基準追加案
        }
        

        class GPM_37["GPM_37: 基準を追加する（実装）"] {
            Input: 追加案、部品/治具
            Output: 追加済み基準（新規基準実装）
        }
        

        class GPM_38["GPM_38: 形状変更位置を決定する"] {
            Input: 変形/干渉情報、成形性・工程制約
            Output: 改修位置案
        }
        

        class GPM_39["GPM_39: 形状変更形状を決定する"] {
            Input: 目標公差・機能、成形性・ビード/トリム条件
            Output: 変更形状案（ビード/トリム）
        }
        

        class GPM_40["GPM_40: 金型を改修する"] {
            Input: 改修仕様、現金型/3Dデータ
            Output: 改修済み金型
        }
        

        class GPM_42["GPM_42: 形状変更を実施する"] {
            Input: CAD反映/改修仕様、製造条件
            Output: 形状変更反映品/データ
        }
        

        class GPM_44["GPM_44: 打点位置を確認する"] {
            Input: 溶接計画/図、現物
            Output: 打点位置確認結果
        }
        

        class GPM_45["GPM_45: 打点順位を確認する"] {
            Input: 現行打点順序、品質課題
            Output: 現行打点順位の確認結果
        }
        

        class GPM_46["GPM_46: 打点順位の調整案を立案する"] {
            Input: 変形課題/解析結果、工程制約
            Output: 打点順位調整案
        }
        

        class GPM_47["GPM_47: 打点順位を変更する（実装）"] {
            Input: 調整案、設備設定手順
            Output: 更新された打点順序
        }
        

        class GPM_48["GPM_48: 部品を治具にセットする"] {
            Input: 部品、治具
            Output: 治具セット済み部品
        }
        

        class GPM_49["GPM_49: クランプで仮固定する"] {
            Input: セット済み部品、クランプ
            Output: 仮固定状態
        }
        

        class GPM_50["GPM_50: クランプを一部解除する"] {
            Input: 固定状態の組付け体
            Output: 解放状態/挙動情報
        }
        

        class GPM_51["GPM_51: 部品を組み付ける"] {
            Input: 各部品、治具/締結具
            Output: 組付け体
        }
        

        class GPM_52["GPM_52: 治具の締付を強化する"] {
            Input: 締付不足の所見、工具・トルク管理値
            Output: 締付力向上/トルク設定
        }
        

        class GPM_53["GPM_53: 押さえ側基準を補強する（板材挿入）"] {
            Input: 押さえ側基準、補強板材/スペーサ
            Output: 補強済み基準
        }
        

        class GPM_54["GPM_54: 受け側基準を調整する（シム挿入）"] {
            Input: 受け側基準、シム/スペーサ
            Output: 調整済み基準（シム厚含む）
        }
        

        class GPM_55["GPM_55: 溶接を実施する"] {
            Input: 溶接計画、部材、治具/設備
            Output: 溶接済み部品
        }
        

        class GPM_56["GPM_56: プレス成形を実施する"] {
            Input: プレス金型、材料、成形条件
            Output: プレス単品
        }
        

        class GPM_57["GPM_57: 基準変更の効果を評価する"] {
            Input: 基準変更後の測定/シミュレーション結果
            Output: 効果評価結果（倒れ/隙間改善）
        }
        

        class GPM_58["GPM_58: 形状変更の効果を評価する"] {
            Input: 形状変更後の測定/CAE結果
            Output: 効果評価結果（変位/剛性/隙間）
        }
        

        class GPM_59["GPM_59: 前後工程への影響を評価する"] {
            Input: 変更案/実装案、工程計画・品質要求
            Output: 前後工程への影響評価（可/不可・対策）
        }
        

        class GPM_60["GPM_60: コストを評価する"] {
            Input: 変更案/実装案、工数・設備改造要件
            Output: コスト見積・採算性評価
        }
        

        class GPM_61["GPM_61: 干渉解消可否を評価する"] {
            Input: 干渉情報、形状/基準変更案、設備制約
            Output: 干渉解消の可否評価（可能/困難）
        }
        

    %% LLD Edges
LLD_37 --> LLD_38
LLD_38 --> LLD_39
LLD_39 --> LLD_40
LLD_40 --> LLD_41
LLD_41 --> LLD_42
LLD_42 --> LLD_43
LLD_43 --> LLD_44
LLD_44 --> LLD_45
LLD_45 --> LLD_46
LLD_46 --> LLD_47
LLD_47 --> LLD_48
LLD_48 --> LLD_49
LLD_49 --> LLD_50
LLD_50 --> LLD_51
LLD_51 --> LLD_52
LLD_52 --> LLD_53
LLD_53 --> LLD_54
LLD_54 --> LLD_55
LLD_55 --> LLD_56
LLD_56 --> LLD_57
LLD_57 --> LLD_58
LLD_58 --> LLD_59
LLD_59 --> LLD_60
LLD_60 --> LLD_61
LLD_61 --> LLD_62
LLD_62 --> LLD_63
LLD_63 --> LLD_64
LLD_64 --> LLD_65
LLD_65 --> LLD_66
LLD_66 --> LLD_67
LLD_67 --> LLD_68
LLD_68 --> LLD_69
LLD_69 --> LLD_70
LLD_70 --> LLD_71
LLD_71 --> LLD_72

    %% LLD-GPM Edges
LLD_37 <|.. GPM_20 : Implements
LLD_38 <|.. GPM_33 : Implements
LLD_39 <|.. GPM_3 : Implements
LLD_40 <|.. GPM_4 : Implements
LLD_41 <|.. GPM_54 : Implements
LLD_42 <|.. GPM_33 : Implements
LLD_43 <|.. GPM_10 : Implements
LLD_44 <|.. GPM_10 : Implements
LLD_45 <|.. GPM_4 : Implements
LLD_46 <|.. GPM_22 : Implements
LLD_47 <|.. GPM_10 : Implements
LLD_48 <|.. GPM_10 : Implements
LLD_49 <|.. GPM_4 : Implements
LLD_50 <|.. GPM_29 : Implements
LLD_51 <|.. GPM_11 : Implements
LLD_52 <|.. GPM_10 : Implements
LLD_53 <|.. GPM_10 : Implements
LLD_54 <|.. GPM_23 : Implements
LLD_55 <|.. GPM_25 : Implements
LLD_56 <|.. GPM_24 : Implements
LLD_57 <|.. GPM_25 : Implements
LLD_58 <|.. GPM_26 : Implements
LLD_59 <|.. GPM_27 : Implements
LLD_60 <|.. GPM_28 : Implements
LLD_61 <|.. GPM_23 : Implements
LLD_62 <|.. GPM_12 : Implements
LLD_63 <|.. GPM_30 : Implements
LLD_64 <|.. GPM_44 : Implements
LLD_65 <|.. GPM_31 : Implements
LLD_66 <|.. GPM_32 : Implements
LLD_67 <|.. GPM_33 : Implements
LLD_68 <|.. GPM_40 : Implements
LLD_69 <|.. GPM_17 : Implements
LLD_70 <|.. GPM_18 : Implements
LLD_71 <|.. GPM_31 : Implements
LLD_72 <|.. GPM_55 : Implements

    