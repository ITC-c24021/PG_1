moneyAmount = int(input("お釣りの金額を入力してください:"))
coins = [100,10,1]
coinCount = {100:0,
             10:0,
             1:0}

print(f"お釣りの金額：{moneyAmount}")

for i in coins:
    coinCount[i] = moneyAmount // i
    moneyAmount %= i

print(f"100円玉{coinCount[100]}枚,10円玉{coinCount[10]}枚,1円玉{coinCount[1]}枚")

