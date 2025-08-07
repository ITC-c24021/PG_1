print("""
-----ライツアウト-----

1.5x5のパネルがあります
2.毎回座標を入力しその位置から十字型にパネルをひっくり返します
3.上記2.を繰り返し全面をひっくり返すことが出来ればクリアとなります
      """)
panelLi = [["□" for _ in range(5)] for _ in range(5)]

directionLi = [(0,-1),
               (1,0),
               (0,1),
               (-1,0)]

def ShowPanel():
    num = 1
    print("""
  1 2 3 4 5""")
    for i in panelLi:
        print(f"{num} "+" ".join(i))
        num += 1


def PanelChange(y,x):
    print(y,x)
    if panelLi[y][x] == "□":
        panelLi[y][x] = "■"
    else:
        panelLi[y][x] = "□"
    for dx,dy in directionLi:
        if 0 <= x+dx < 5 and 0 <= y+dy < 5:
            if panelLi[y+dy][x+dx] == "□":
                panelLi[y+dy][x+dx] = "■"
            else:
                panelLi[y+dy][x+dx] = "□"

ShowPanel()


while True:
    clear = True
    y,x = 0,0
    while True:
        try:
            y = int(input("\n縦の行を選択して番号を入力してください:"))
            if 1 <= y <= 5:
                break
        except ValueError:
            print("\n正しく入力してください:")
    while True:
        try:
            x = int(input("\n横の行を選択して番号を入力してください:"))
            if 1 <= x <= 5:
                break
        except ValueError:
            print("\n正しく入力してください:")

    PanelChange(y-1,x-1)
    ShowPanel()

    for i in panelLi:
        if "□" in i:
            clear = False

    if clear:
        break

print("ゲームクリア！！")



