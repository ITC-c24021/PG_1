class Music:
    name = ""
    artist = ""
    release = 0
    ganre = ""
    sound = ""

    def music_info():
        print(f"name = {name}, artist = {artist}, release = {release}, genre = {genre}")

    def music_play():
        play(sound)

    def music_stop():
        stop(sound)

song = Music()

song.name = "Little L"
song.artist = "Jamiroquai"
song.release = 2001
song.genre = "Acid Jazz"
song.sound = "a;lkfjeoijioejsjddfdasfeoijsdf"

inst = Music()
inst.name = "Longing"
inst.artist = "George Winston"
inst.releasse = 1984
inst.genre = "instrumental"
inst.sound = "klajsfoeohndklgohgkdj\\\e:leskafl;fhkdf"

song.music_info()
print(f"Music Number:{Music,count}")

while True:
    song.music_play()
    r = input("eを入力すると終了します")
    if r == "e":
        break

song.music_stop()
