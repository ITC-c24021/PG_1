import random

gameStart = False #ゲーム開始判定

#マップ(30マス)
g_mapLi = ["[]"for i in range(30)]
g_mapLi[0] = "[S]" #スタート
g_mapLi[29] = "[G]" #ゴール

viewStatus = lambda:print(f"""
---現在位置---

{"-".join(g_mapLi)}

---金貨---

あなた:{coinCount[0]}枚 相手:{coinCount[1]}枚
""")

#現在位置(マス目)
g_pos = [0,0] #[0]プレイヤー [1]相手

#マーカー
marks = ["P","E"]
 
turn = 0 #ターン

#ターン切り替え用
def TurnChange(): 
    global turn
    turn = 1 - turn
 
diceNum = 0 #サイコロの出目

coinCount = [5,5]

#イベント系

#イベントをランダムに生成＋固定数イベント
eventLi = [random.randint(1,4) for _ in range(15)] + [5,5,5,5,6,6] #イベントの種類
eventNumLi = random.sample(range(1,29), len(eventLi)) #イベントを配置するマス
eventDi = dict(zip(eventNumLi, eventLi)) #上記2つを辞書として格納
eventTextLi = ["",
               ["金貨をゲット！！","枚ゲットしました！！"],
               ["金貨をロス...","枚ロストしました..."],
               ["〇マス進む！！","マス進みます！！"],
               ["〇マス戻る...","マス戻ります"],
               ["1回休み...","次のターンがスキップされます..."],
               ["振り出しに戻る...","振り出しに戻ります..."]]


ok = [True,True] #休みの判定(休みはFalse)

# 説明表示
print(
"""---------------
すごろくゲーム
---------------

--- ルール ---

[勝利条件]
・30マス目にあるゴールに先にぴったりに到着した人 == 「スピード的勝利」
・ゲーム終了時により金貨の多いほう== 「金銭的勝利」

[金貨]
・最初からそれぞれ５枚ずつ金貨を所持しています
・金貨は止まったマスにより増えたり減ったりします

[マス]
1.金貨をゲット！！
2.金貨をロス...
3.〇マス進む
4.〇マス戻る
5.1回休み
6.振り出しに戻る

[その他]
・ゴールまでのマス目以上の目が出るとオーバーした分ゴールマスから戻りそのマスのイベントも発生します

--------------

ではゲームスタート！！！！

""")


def EventCheck(x):
    def EventHappen(x):
        global ok
        print("""
        　　　※ イベント発生!!!※
              """)
        if 1 <= x <= 4:
            value = random.randint(1,3)
            print(f"""
            ---{eventTextLi[x][0]}---

               {value}{eventTextLi[x][1]}
                  """)
            if x == 1:
                coinCount[turn] += value
            elif x == 2:
                coinCount[turn] -= value
            elif x == 3:
                Move(value)
            elif x == 4:
                Move(value * -1)
        if 5 <= x <= 6:
            print(f"""
            ---{eventTextLi[x][0]}---

               {eventTextLi[x][1]}
                  """)
            if x == 5:
                ok[turn] = False
            elif x == 6:
                Move(len(g_mapLi) * -1)
        


    if x in eventDi:
        EventHappen(eventDi[x])
        viewStatus()



def Move(num,isDice=False):
    
    global g_mapLi,g_pos #グローバル宣言
    if isDice:
        print(f"""
        {num}が出ました！！！

        {num}マス進みます...
              """)


    g_mapLi[g_pos[turn]] = g_mapLi[g_pos[turn]].replace(marks[turn],"")

    #移動
    if g_pos[turn] + num < 0:
        g_pos[turn] = 0
    elif g_pos[turn] + num <= 29: #進んだ先がゴールのマス目以下の時
        g_pos[turn] += num

    elif g_pos[turn] + num > 29: #進んだ先がゴールのマス目より大きい時
        g_pos[turn] = 29 - (g_pos[turn] + num - 29)
        print("ゴールを超えるため超えた値の分戻ります")

    #マップの更新(現在位置)
    g_mapLi[g_pos[turn]] = g_mapLi[g_pos[turn]][:-1] + marks[turn] + g_mapLi[g_pos[turn]][-1]
    

while True:

    #毎ターン空行開ける
    if gameStart:
        print("""

================================================================
================================================================
              """)
    else:
        gameStart = True


    #サイコロ振る
    diceNum = random.randint(1,6) #出目決定
    
    if turn == 0: #プレイヤー
        print("あなたのターンです")
        input("Enterキーを押してサイコロを振って下さい")

    else: #相手
        print("相手がサイコロを振ります")

    Move(diceNum,True) #進む処理
    
    viewStatus() #マップ表示

    EventCheck(g_pos[turn]) #イベントマスかどうかを確認

    #どちらかがゴールしていたらゲーム終了
    if g_mapLi[29] != "[G]":
        print("""

-----ゴールに到達したためゲームを終了します-----

              """)
        break

    #ターン切り替え
    input("Enterキーを押してターン終了")

    while True:
        next_turn = 1 - turn
        if ok[next_turn]:
            turn = next_turn  # ターン切り替え
            break
        else:
            print("""
-----1回休みにつきターンをスキップします-----
                  """)
            ok[next_turn] = True  # 休み解除
            turn = next_turn      # ターン進めてもう一度判定



print(f"""
-----結果発表！！！-----""")

viewStatus()

print(f"""
スピード勝利:{"あなた" if "P" in g_mapLi[29] else "相手"}

金銭的勝利:{"あなた" if coinCount[0] > coinCount[1] else "相手" if coinCount[0] < coinCount[1] else "引き分け"}
      """)
