print("""
      突然ですが、あなたはドラゴンを7日間預かることになりました。
      ドラゴンを飢えさせたり怒らせたりしないよう、ちゃんと世話をしないといけません。
      1．7日間、世話をするコマンドを入力し、ドラゴンのステータスを変化させます
      
      2．1日につき4回コマンドを入力できます
      
      3．ドラゴンのステータスは満腹度と機嫌度の2つあり、どちらも初期値は10、最大値も10です

      ４．上記3.のステータスがどちらでも0以下になるとゲームオーバーになります
      ５．ドラゴンは毎日ウンチをします。掃除をしないと機嫌度の減少が3倍になり、その効果は累積していきます。

      6．コマンドは食事、掃除、散歩、睡眠の4つです
      　・食事:満腹度+2
      　・掃除:満腹度-1、機嫌度の減少を1に戻します
      　・散歩:満腹度-1、機嫌度+1
      　・睡眠:満腹度-2、機嫌度+2

      7．1日の各コマンドの実行には制限があります
      　・食事は1日最大3回までです
      　・掃除は連続して実行できません
      　・散歩は連続して実行できません

      8．1日に1度も食事や睡眠を与えないと、さらにステータスが減少します
      　・まる1日食事を与えない:満腹度-3
      　・まる1日睡眠を与えない:機嫌度-3
      """)

dragon = input("ドラゴンの名前を入力してください:")

dragonCondition = [10,10] #満腹度、機嫌度

taskLi = [[2,0], #食事
          [-1,0], #掃除
          [-1,1], #散歩
          [-2,2] #睡眠
          ]

taskText = ["""
            ---食事を与えました---
            """,
            """
            ---掃除をしました---
            """,
            """
            ---散歩をしました---
            """,
            """
            ---睡眠を取らせました---
            """
            ]

viewStatus = lambda:print(f"""
---現在の{dragon}の様子---

満腹度:{dragonCondition[0]}
機嫌度:{dragonCondition[1]}
掃除をしていない日数(連続):{badCount}
                          """)

mealCount = 0 #食事の回数(1日単位)
badCount = 0 #掃除していない日数(連続)
sleep = False
clean = False

live = True

currentTask = 0
def TaskCheck():
    global dragonCondition,badCount,currentTask,sleep,mealCount,clean

    taskNum = 0

    while True:
        li = ["1","2","3","4"]
        taskNum = input(f"""
何をしますか？？
1.食事({mealCount}/3)(満腹度+2)
2.掃除(満腹度‐1、機嫌度の減少を1に戻す)
3.散歩(満腹度‐1、機嫌度+1)
4.睡眠(満腹度‐2、機嫌度+2)

番号で入力してください:
""")
        if taskNum == None or taskNum not in li:
            continue
        elif taskNum == "1" and mealCount >= 3:
            print("""
※ 食事は1日3回までです！！！
                  """)
        elif taskNum == "2" and currentTask == 2:
            print("""
※ 掃除は連続して行えません！！！
                  """)
        elif taskNum == "3" and currentTask == 3:
            print("""
※ 散歩は連続して行えません！！！
                  """)
        else:
            currentTask = int(taskNum)
            break
    taskNum = int(taskNum)
    print(taskText[taskNum-1])
    dragonCondition[0] += taskLi[taskNum-1][0]
    dragonCondition[1] += taskLi[taskNum-1][1]

    for i in range(2):
        if dragonCondition[i] > 10:
            dragonCondition[i] = 10

    if taskNum == 1:
        mealCount += 1
    elif taskNum == 2:
        print("""
※ 機嫌度の減少を1に戻します
              """)
        clean = True
        badCount = 0
    elif taskNum == 4:
        sleep = True

    viewStatus()




for i in range(7):
    
    print(f"""
-----{i+1}日目-----
    """)

    viewStatus()

    for n in range(4):
        print(f"""
行動回数({n}/4)
              """)
        TaskCheck()
        
        if dragonCondition[0] <= 0:
            print(f"""
※ ※ ※ 満腹度が0以下になったためあなたは{dragon}に食べられました※ ※ ※
                  """)
            live = False
            break
        
        elif dragonCondition[1] <= 0:
            print(f"""
※ ※ ※ 機嫌度が0以下になったためあなたは{dragon}に黒焦げにされました※ ※ ※ 
                  """)
            live = False
            break
    if not live:
        break

    if not clean:
        badCount += 1
        print(f"""
※ 掃除を{badCount}日していないため機嫌度が{1 if badCount == 1 else 3*badCount}減少します
              """)
        dragonCondition[1] -= 1 if badCount == 1 else 3*badCount
    if not sleep:
        print("""
※ 丸1日睡眠をしていないため機嫌度が3減少します
              """)
        dragonCondition[1] -= 3
    if mealCount <= 0:
        print("""
※ 丸1日食事を与えなかったため満腹度が3減少します
              """)
        dragonCondition[0] -= 3

    sleep = False
    clean = False
    mealCount = 0
    
    if dragonCondition[0] <= 0:
            print(f"""
※ ※ ※ 満腹度が0以下になったためあなたは{dragon}に食べられました※ ※ ※
                  """)
            live = False
            break

        elif dragonCondition[1] <= 0:
            print(f"""
※ ※ ※ 機嫌度が0以下になったためあなたは{dragon}に黒焦げにされました※ ※ ※
                  """)
            live = False
            break




print("""

-----最終結果-----
      """)

print(f"""
ゲーム{"クリア!!!" if live else "オーバー..."}
      """)
