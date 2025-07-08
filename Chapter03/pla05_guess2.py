
import random

gameStart = False

num = random.randint(1,10)

score = 5

answerCount = 10
roundAnswerCount = 10
challengeCount = 1
while True:
    if not gameStart:
        gameStart = True
    else:
        print("")
    print(f"問題[{challengeCount}] 残り回答回数:{roundAnswerCount}回 現在のスコア:{score}点")
    answer = int(input("1から10の数字のどれかを予想して数字で入力してください(0を入力すると途中終了できます):"))
    roundAnswerCount -= 1
    if answer == 0:
        break
    elif answer == num:
        answerCount -= 1
        challengeCount += 1
        score += 10
        num = random.randint(1,10)
        if answerCount > 0:
            print("当たりです！(+10点)")
            roundAnswerCount = answerCount
        else:
            print("当たりです！全問正解おめでとう！")
            break
        continue
    elif roundAnswerCount < 1:
        print(f"残念！正解は{num}でした！(‐1点)")
        score -= 1
        break
    elif answer > num:
        print("数字が大きいです(―1点)")
    else:
        print("数字が小さいです(‐1点)")
        
    score-= 1

print(f"あなたの最終スコア:{score}点")
