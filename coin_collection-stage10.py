# === Stage 10: Поиск по нескольким словам ===
# Project: CoinCollection
def parse_query(query):
    tokens = query.split()
    includes = []
    excludes = []
    for token in tokens:
        if token.startswith('-'):
            excludes.append(token[1:].lower())
        else:
            includes.append(token.lower())
    return includes, excludes


def matches_coin(coin, includes, excludes):
    text = f"{coin['name']} {coin['country']} {coin['year']} {coin['condition']}".lower()
    for term in includes:
        if term not in text:
            return False
    for term in excludes:
        if term in text:
            return False
    return True


def search_coins(coins, query):
    includes, excludes = parse_query(query)
    results = [coin for coin in coins if matches_coin(coin, includes, excludes)]
    return results


if __name__ == '__main__':
    sample = [
        {'name': 'Ruble', 'country': 'Russia', 'year': 2020, 'condition': 'Uncirculated'},
        {'name': 'Dollar', 'country': 'USA', 'year': 1999, 'condition': 'Worn'},
        {'name': 'Yuan', 'country': 'China', 'year': 2018, 'condition': 'Proof'},
    ]
    for q in ['russian', 'russian -worn', 'dollar china']:
        print(q, '->', [c['name'] for c in search_coins(sample, q)])
