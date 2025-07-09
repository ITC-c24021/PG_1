import random

#手の種類
jankenLi = ["グー",
            "チョキ",
            "パー"]

#種類ごとの指の本数
fingerLi = {"グー":0,
            "チョキ":2,
            "パー":5}

#勝利回数
pWinCount = 0 #プレイヤー
cWinCount = 0 #相手

#指の残り本数
pFingerAmount = 18 #プレイヤー
cFingerAmount = 18 #相手

gameStart = False #じゃんけんが始まっているかどうか

roundNum = 1 #n回戦か



print("今から10回じゃんけんをします。")

#プレイヤーと相手の手を比べて勝敗を決める
def Check (p,c):
    #グローバル使用宣言
    global pWinCount
    global cWinCount

    #プレイヤー勝利パターン
    if p == "グー" and jankenLi[c] == "チョキ" or p == "チョキ" and jankenLi[c] == "パー" or p == "パー" and jankenLi[c] == "グー":

        #6回目、10回目は2点。それ以外は1点
        if roundNum == 6 or roundNum == 10:
            pWinCount += 2
        else:
            pWinCount += 1

        return 0 #結果を返す

    #あいこパターン
    elif p == jankenLi[c]:
        return 2 #結果を返す

    #負けパターン
    else:
        #6回目、10回目は2点。それ以外は1点
        if roundNum == 6 or roundNum == 10:
            cWinCount += 2
        else:
            cWinCount += 1

        return 1 #結果を返す
        

#指減らす用
def DecreaseFinger (p,c):
    global pFingerAmount,cFingerAmount
    pFingerAmount -= p #プレイヤー
    cFingerAmount -= c #相手


#10試合行う
for i in range(10):

    if gameStart:
        print("")
    else:
        gameStart = True

    #出す手を決める

    while True: #相手側
        com = random.randrange(0,3)

        #指が足りるなら決定
        if fingerLi[jankenLi[com]] <= cFingerAmount:
            break

    while True: #プレイヤー側
        s = "勝利点2倍！！"
        player = input(f"[{s + str(roundNum) if roundNum == 6 or roundNum == 10 else roundNum}回戦]\n[現在の指の本数]あなた:{pFingerAmount}本　相手:{cFingerAmount}本\n「グー」「チョキ」「パー」のどれかを選び、入力してください:")

        #入力が正しいか
        if player in jankenLi:

            #指が足りるなら決定
            if fingerLi[player] > pFingerAmount:
                print("指が足りません！！")
            else:
                break

    #指の本数を減らす
    DecreaseFinger(fingerLi[player],fingerLi[jankenLi[com]])

    print(f"あなたの手:{player} 相手の手:{jankenLi[com]}") #両者の手を表示

    winCheck = Check(player,com) #勝敗確認

    #結果に応じて表示
    if winCheck == 0:
        print("あなたの勝ちです！")
    elif winCheck == 1:
        print("あなたの負けです")
    else:
        print("あいこです！")

    print(f"[勝利点(現在)]あなた:{pWinCount} 相手:{cWinCount}") #現時点での勝敗状況
    roundNum += 1 #1ラウンド進む


#結果発表
print(f"""

最終結果！！
[得点]　=　[勝利点]　-　[指の残り本数]
[勝利点]あなた:{pWinCount} 相手:{cWinCount}
[指の残り本数]あなた:{pFingerAmount} 相手:{cFingerAmount}
      
{pWinCount-pFingerAmount}対{cWinCount-cFingerAmount}で...

""")


#最終結果に応じて表示
if pWinCount - pFingerAmount > cWinCount - cFingerAmount:
    print("あなたの勝ち！！")
elif pWinCount - pFingerAmount < cWinCount - cFingerAmount:
    print("あなたの負け！！")
else:
    print("引き分け！！")

