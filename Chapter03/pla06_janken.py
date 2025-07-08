import random
jankenLi = ["グー",
            "チョキ",
            "パー"]
cWinCount = 0
pWinCount = 0

print("今から10回じゃんけんをします。")

def Check (p,c):
    global pWinCount
    global cWinCount
    if p == "グー" and jankenLi[c] == "チョキ" or p == "チョキ" and jankenLi[c] == "パー" or p == "パー" and jankenLi[c] == "グー":
        pWinCount += 1
        return 0
    elif p == jankenLi[c]:
        return 2
    else:
        print("hoge")
        cWinCount += 1
        return 1
        
roundNum = 1

for i in range(10):
    com = random.randrange(0,3)
    player = input(f"[{roundNum}回戦]「グー」「チョキ」「パー」のどれかを選び、入力してください:")

    print(f"あなたの手:{player} 相手の手:{jankenLi[com]}")

    winCheck = Check(player,com)

    if winCheck == 0:
        print("あなたの勝ちです！")
    elif winCheck == 1:
        print("あなたの負けです")
    else:
        print("あいこです！")

    roundNum += 1

print(f"[勝った回数]あなた:{pWinCount} 相手:{cWinCount}")

if pWinCount > cWinCount:
    print("あなたの勝ち！！")
elif pWinCount < cWinCount:
    print("あなたの負け！！")
else:
    print("引き分け！！")


