# === Stage 9: Текстовый поиск ===
# Project: CoinCollection
def search_with_highlight(coins, query):
    normalized_query = query.strip().lower()
    if not normalized_query:
        return []

    results = []
    for coin in coins:
        fields = [coin.name, coin.country, str(coin.year), coin.condition]
        if any(normalized_query in field.lower() for field in fields):
            results.append(coin)

    return results


def highlight_matches(text, query):
    normalized_query = query.strip().lower()
    if not normalized_query:
        return text

    text = text.replace("<mark>", "&lt;mark&gt;")
    text = text.replace("</mark>", "&lt;/mark&gt;")

    import re
    pattern = re.compile(re.escape(normalized_query), re.IGNORECASE)

    def replace_match(match):
        return "<mark>" + match.group(0) + "</mark>"

    highlighted = pattern.sub(replace_match, text)

    return highlighted.replace("&lt;mark&gt;", "<mark>").replace("&lt;/mark&gt;", "</mark>")


class Coin:
    def __init__(self, name, country, year, condition):
        self.name = name
        self.country = country
        self.year = year
        self.condition = condition


def format_coin(coin, query):
    line = "Название: {} | Страна: {} | Год: {} | Состояние: {}".format(
        coin.name,
        coin.country,
        coin.year,
        coin.condition,
    )

    if query:
        line = highlight_matches(line, query)

    return line


def main():
    coins = [
        Coin("Rubel", "Russia", 1997, "Uncirculated"),
        Coin("Ruble", "Russia", 2000, "Worn"),
        Coin("Euro", "Germany", 2002, "Uncirculated"),
        Coin("Dollar", "USA", 1963, "Worn"),
    ]

    query = input("Введите текст для поиска (или 'stop'): ").strip()

    while query.lower() != "stop":
        results = search_with_highlight(coins, query)

        if results:
            print("Найдено монет: {}".format(len(results)))
            for coin in results:
                print(format_coin(coin, query))
        else:
            print("Ничего не найдено.")

        print()

        query = input("Введите текст для поиска (или 'stop'): ").strip()


if __name__ == "__main__":
    main()
