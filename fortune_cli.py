import random

FORTUNES = [
    ("大吉", "今日は素晴らしい一日になります！"),
    ("中吉", "良いことが訪れるでしょう。"),
    ("小吉", "まずまずの運勢です。"),
    ("吉",   "平穏な一日になりそう。"),
    ("凶",   "慎重に行動した方が良さそうです。"),
    ("大凶", "今日は無理をしないで過ごしましょう。")
]

LUCKY_ITEMS = [
    "青いペン",
    "赤いハンカチ",
    "ラッキーコイン",
    "星形のアクセサリー",
    "四つ葉のクローバー"
]

LUCKY_COLORS = [
    "赤",
    "青",
    "緑",
    "黄",
    "紫"
]

def tell_fortune():
    fortune, message = random.choice(FORTUNES)
    lucky_item = random.choice(LUCKY_ITEMS)
    lucky_color = random.choice(LUCKY_COLORS)
    print("今日の運勢: {}".format(fortune))
    print(message)
    print("ラッキーアイテム: {}".format(lucky_item))
    print("ラッキーカラー: {}".format(lucky_color))

if __name__ == "__main__":
    tell_fortune()
