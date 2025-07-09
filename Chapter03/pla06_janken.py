import random

#手の種類
jankenLi = ["グー",
            "チョキ",
            "パー"]
#勝利回数
pWinCount = 0 #プレイヤー
cWinCount = 0 #相手

gameStart = False #じゃんけんが始まっているかどうか

print("今から10回じゃんけんをします。")

#プレイヤーと相手の手を比べて勝敗を決める
def Check (p,c):
    #グローバル使用宣言
    global pWinCount
    global cWinCount

    #プレイヤー勝利パターン
    if p == "グー" and jankenLi[c] == "チョキ" or p == "チョキ" and jankenLi[c] == "パー" or p == "パー" and jankenLi[c] == "グー":
        pWinCount += 1
        return 0

    #あいこパターン
    elif p == jankenLi[c]:
        return 2

    #負けパターン
    else:
        cWinCount += 1
        return 1
        

roundNum = 1 #n回戦か

#10試合行う
for i in range(10):
    #出す手を決める
    com = random.randrange(0,3) #相手

    if gameStart:
        print("")
    else:
        gameStart = True

    while True:
        player = input(f"[{roundNum}回戦]「グー」「チョキ」「パー」のどれかを選び、入力してください:") #プレイヤー

        if player in jankenLi:
            break

    print(f"あなたの手:{player} 相手の手:{jankenLi[com]}") #両者の手を表示

    winCheck = Check(player,com) #勝敗確認

    #結果に応じて表示
    if winCheck == 0:
        print("あなたの勝ちです！")
    elif winCheck == 1:
        print("あなたの負けです")
    else:
        print("あいこです！")

    print(f"[勝った回数(現在)]あなた:{pWinCount} 相手:{cWinCount}") #現時点での勝敗状況
    roundNum += 1 #1ラウンド進む


print(f"[勝った回数]あなた:{pWinCount} 相手:{cWinCount}") #最終結果表示

#最終結果に応じて表示
if pWinCount > cWinCount:
    print("あなたの勝ち！！")
elif pWinCount < cWinCount:
    print("あなたの負け！！")
else:
    print("引き分け！！")


