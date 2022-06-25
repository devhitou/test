import random
import datetime
import calendar
import math
import sys
import time

""" 文字の出力
print("ハローワールド","野球","サッカー" ,end="ジャンル：スポーツ")

print("うどん")
print("そば")

print("ラーメン", end="")
print("かつどん")

print("選択肢：円","ドル","ユーロ","ペリカ", sep="or")
"""
#################################################################################
""" 変数に代入
name = "千尋"
print(name)

print(name + "：こんにちは")
print(name + "：いいお天気ですね")
print(name + "：こんな日はいつもより遠くに散歩したくなります")

name = "フレデリカ"
print(name + "：こんにちは")
print(name + "：いいお天気ですね")
print(name + "：こんな日はいつもより遠くに散歩したくなります")
"""
#################################################################################
""" キャスト
num = 3 
gold = 100 
msg1 = "スライム を" + str(num) + "体倒した"
msg2 = str(gold * num) + "ゴールドを手に入れた" 
print(msg1) 
print(msg2)
"""
#################################################################################
""" 標準入力
line = input("文字を入力してください")
print("入力値：" + line)

num = int(input("数値１を入力してください"))
num2 = int(input("数値２を入力してください"))
num3 = num * num2
print(str(num) + "×" + str(num2) + "=" + str(num3))
"""
#################################################################################
""" if 条件分岐
score = int(input("0~100の間でスコアを入力してください"))

if score == 100:
    print("評価[A] 100点すごいね。")
elif score >= 80:
    print("評価[B] まあまあすごいね。")
elif score >= 60:
    print("評価[C] OK。")
elif score >= 40:
    print("評価[D] もうちょっと、がんばろうよ。")
elif score >= 20:
    print("評価[E] テスト中寝てた？")
else:
    print("評価[F] やる気ないやん絶対")
"""
#################################################################################
""" for 繰り返し
for i in range(10):

    if i == 5:
        continue

    print(i)
else:
    print("ひじ！")
"""
#################################################################################
""" while 繰り返し
num = int(input("繰り返し回数を入力してくだされ"))
i = 0

while i < num:

    if i == 7:
        print("おっとそこまでだ！")
        break

    if i == 2:
        print("2はきらいだからスキップするよ")
        i += 1
        continue
    print(i)
    i += 1
else:
    print("おわり")
"""
#################################################################################
""" モジュール　ライブラリのインポート
num = random.randint(1,10)
print(num)
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

print("今日は" + str(now.year) + "年" + str(now.month) + "月" + str(now.day) + "日です")

print(calendar.month(2022,12,w=1,l=1))

print(math.floor(3.123))
print(math.ceil(3.123))

print(math.pi)
radius = 5
print(2*radius*math.pi)
print(radius*radius*math.pi)
"""
#################################################################################
""" 魔王を倒すゲーム
hero_hp = 200
maou_hp = 200
print("魔王が現れた！ \n戦闘開始！")

while True:
    print("現在のHP  勇者:" + str(hero_hp) + "  魔王のHP:" + str(maou_hp))

    hero_atack = random.randint(10,20)

    hissatu = int(input("必殺技を使いますか？ 1:使う 2:使わない"))

    if hissatu == 1:
        hantei = random.randint(0,1)
        if hantei == 1:
             hero_atack = hero_atack * 2
             maou_hp -= hero_atack
             print("\n必殺技が決まった！ダメージが2倍！ 魔王に" + str(hero_atack) +"のダメージ！")
        else:
            hero_atack = 0
            print("\n攻撃がはずれた！")

    else:
        maou_hp -= hero_atack
        print("\n勇者の攻撃！魔王に" + str(hero_atack) +"のダメージ！")

    if maou_hp <= 0:
        print("\n魔王を倒した！")
        print("魔王：うわああああああ！")
        break

    maou_atack = random.randint(10,20)
    kyuusyo = random.randint(0,5)
    
    if kyuusyo == 2:
        maou_atack = int(maou_atack * 2.5)
        print("魔王の攻撃がきゅうしょに当たった！勇者に" + str(maou_atack) +"のダメージ！\n")
    else:
        print("魔王の攻撃！勇者に" + str(maou_atack) +"のダメージ！\n")

    hero_hp -= maou_atack

    if hero_hp <= 0:
        print("\nあなたは死にました。 \n目の前が真っ暗になった！")
        print("魔王：雑魚め！出直せ！")
        break

input("\nenterで画面を終了します")
"""
#################################################################################
""" リスト
menbers = ["太郎","次郎","三郎","四郎"]
print (menbers)

menber_1 = "太郎"
menber_2 = "次郎"
menbers2 = [menber_1,menber_2]
print(menbers2)

print(menbers[0])
print(menbers[1])
print(menbers[2])
print(menbers[3])

print(len(menbers))

menbers.append("五郎")
print(menbers)
print(len(menbers))

menbers[2] = "六郎"

print(menbers)
menberskn = ["イイダ" ,"ウエダ","アキハラ","イマイ"]
print(sorted(menberskn))
menbers.pop(2)
print(menbers)


menberskn_new = sorted(menberskn)
print(menberskn_new)
print(menberskn)

print(sorted(menberskn,reverse = True))


for i in menbers:
    print(i + "君が登校しました")


for i,name in enumerate(menbers):
    print(str(i) + name)


menbers = ["イイダ" ,"ウエダ","アキハラ","イマイ","エノモト","オオニシ"]
print(sorted(menbers))
menbers[4] = "カワハラ"
print(sorted(menbers))

numbers = [1, 2, 4, 6, 12, 24]
i = 0
for num in numbers:
    i += num
print(i)

"""
#################################################################################
""" 複数の入力値の取得
menbers = input("名前入力してな").split(",")
print(menbers)

for num,name in enumerate(menbers):
    print("出席番号"+ str(num + 1) + ":" + name)


members = []
for i in range(2):
    members.append(input("名前を入力してな"))
print(members)

members = [input("名前を入力してな") for i in range(2)]
print(members)

members = []

for i in sys.stdin.readlines():
    members.append(i.rstrip())
print(members)

#members = input("名簿リストを入力してください").split(",")
#print(sorted(members))

ninzuu = int(input("クラスの人数を入力してください"))
members = [input("名前と点数を,区切りで入力") for i in range(ninzuu)]
for i in members:
    score = i.split(",")
    print(score[0] + "：" + score[1])

ninzuu = int(input("クラスの人数を入力してください"))
members = [input("名前を入力してください") for i in range(ninzuu)]

print(sorted(members))
"""
#################################################################################
""" タイピングゲーム
"""
words = ["りんご", "ばなな", "みかん", "ぶどう", "もも", "なし", "めろん", "さくらんぼ", "きうい", "いちご","まぐろ","きつね","まんとひひ","せんぷうき","だいおうぐそくむし",
"たかあしがに","いるか","しゃち","かつどん","うんち","ほうじちゃくらしっくてぃーらて","すまーとふぉん","ねぎとろどん","どらいやー","よくいにん","ごりら","はさみ","きりん","ねこ","らいおん",
"えあこん","ぱそこん","あめりか","いんたーねっと","たおる","れいぞうこ","りんがーはっと","やきにく","ふらいぱん","なべ","にほんご","えいご","てーぶる","でーたーべーす","べんきょう",
"あかてん","りゅうねん","やまと","たけおくん","すべりだい","ぶらんこ","じゃんぐるじむ","やきゅう","さっかー","すいえい","だいえっと","まっとれす","りせっしゅ","ふらんすぱん","おさしみ",
"おかねもちになりたい","はたらきたくない","べてるぎうす","すぴか","おりおんざ","ありあなぐらんで","まいけるじゃくそん","ほいっとにーひゅーすとん","なかやまきんにくん",
"ちかてつ","やまのてせん","けいひんとうほくせん","しぶやく","しんじゅくく","とうきょうと","ほっかいどう","さっぽろし","しずおかけん","すのーぼーど","すきー","もにたー",
"りゅっく","とうきょうどーむ","えび","すいはんき","そうじき","さいとうかずよし","へのへのもへじ","ぐらうんど","はしりたかとび","おおさかふ","ほうりゅうじ","だいびんぐ","ひこうき","かいがいりょこう",
"ごーるでんうぃーく","なつやすみ","うなぎ","ひとりぐらし","こっせつ","いちごぱふぇ","ばななくれーぷ","さんそ","ばった","かぶとむし","はくさい","ぶたにく","れんこん","はんばーぐ",
"すまっぷ","すてーき","ふじさん",]

input("enterでスタートします。\n制限時間は45秒です\n正解すると1点、間違えると-1点だよ。")

print("ゲームスタート！")
start = time.time()
timelimit = int(time.time() - start)

score = 0
ok = 0
ng = 0


while timelimit < 45: 
    timelimit = time.time() - start
    word = random.choice(words)
    print(word)
    in_word = input()

    timelimit = time.time() - start
    
    if word == in_word:
        if timelimit < 45:
            print("OK！\n")
            score += 1
            ok += 1
        else:
            print("そこまでっ！\n")
    else:
        if timelimit < 45:
            score -= 1
            ng += 1 
            print("残念！\n")
        else:
            print("そこまでっ！\n")

rank = "A"
if score >= 20:
    rank = "S"
elif score >= 15:
    rank = "A"
elif score >= 10:
    rank = "B"
elif score >= 6:
    rank = "C"
else:
    rank = "D"

print("制限時間です！")
print("あなたのスコアは" + str(score) + "点です！")
print("タイピングレベル：" + rank)
print("成績詳細\n" + "OK:" + str(ok) + "\nNG:" + str(ng))
input("\nenterで終了します")

#################################################################################
""" 辞書
akihara = {"出席番号":1, "指名":"秋原", "国語":30, "数学":40, "英語":50}
print(akihara)

print(akihara["国語"])
eng = "英語"
print(akihara[eng])

print(len(akihara))

akihara ["理科"] = 60

print(akihara)
akihara["数学"] = 70
print(akihara)

del akihara["国語"]
print(akihara)

score = {"イマイ":30, "ウエダ":65,"アキハラ":40}

print(sorted(score))

new_list = sorted(score)
print(score)
print(new_list)

print(sorted(score.items()))
"""