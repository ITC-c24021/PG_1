year = int(input("生まれた年を数字で入力してください:"))
month = int(input("生まれた月を数字で入力してください:"))
day = int(input("生まれた日を数字で入力してください:"))

def Addition(x):
    result = 0
    while x > 0:
        i = x % 10
        result += i
        x = x // 10
    return result

add = Addition(year)+Addition(month)+Addition(day)

print(f"あなたの運命数は{Addition(add)}です")
