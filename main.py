import socket
import re
from collections import Counter

# Маппинг значений карт
RANKS = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
    "1": 14,
}  # '1' используется как 'A'
# Названия комбинаций в порядке возрастания
COMB_NAMES = [
    "HIGH CARD",
    "ONE PAIR",
    "TWO PAIR",
    "THREE OF A KIND",
    "STRAIGHT",
    "FLUSH",
    "FULL HOUSE",
    "FOUR OF A KIND",
    "STRAIGHT FLUSH",
    "ROYAL FLUSH",
]

HOST = "178.170.197.11"
PORT = 10315

CARD_RE = re.compile(r"([2-9TJQKA1])([shdc])")


# Функция для вычисления лучшей комбинации
def evaluate_hand(cards):
    ranks = sorted([RANKS[c[0]] for c in cards])
    suits = [c[1] for c in cards]
    counts = Counter(ranks)
    count_values = sorted(counts.values(), reverse=True)
    # Проверка на флеш и стрит
    is_flush = len(set(suits)) == 1
    is_straight = False
    if len(counts) == 5:
        high = max(ranks)
        low = min(ranks)
        if high - low == 4:
            is_straight = True
        elif set(ranks) == {2, 3, 4, 5, 14}:
            is_straight = True
            ranks = [1, 2, 3, 4, 5]
    # Определение комбинации
    if is_straight and is_flush:
        return "ROYAL FLUSH" if max(ranks) == 14 else "STRAIGHT FLUSH"
    if 4 in count_values:
        return "FOUR OF A KIND"
    if count_values == [3, 2]:
        return "FULL HOUSE"
    if is_flush:
        return "FLUSH"
    if is_straight:
        return "STRAIGHT"
    if 3 in count_values:
        return "THREE OF A KIND"
    if count_values == [2, 2, 1]:
        return "TWO PAIR"
    if 2 in count_values:
        return "ONE PAIR"
    return "HIGH CARD"


# Парсинг строк вывода сервера
def parse_cards(line):
    return CARD_RE.findall(line)


# Чтение следующей строки, содержащей ключевое слово и карту
def read_next(prefix, f):
    while True:
        line = f.readline()
        if not line:
            return None
        if line.startswith(prefix):
            return parse_cards(line)


# Основная логика бота
def run_bot():
    with socket.create_connection((HOST, PORT)) as sock:
        f = sock.makefile("rw", buffering=1)
        while True:
            line = f.readline()
            if not line:
                break
            print(line.strip())
            if line.startswith("Flop"):
                # Парсим Flop
                flop = parse_cards(line)
                # Парсим Turn
                turn_cards = read_next("Turn", f)
                # Парсим River
                river_cards = read_next("River", f)
                if not flop or not turn_cards or not river_cards:
                    continue
                cards = flop + turn_cards + river_cards
                combo = evaluate_hand(cards)
                print(f"Sending: {combo}")
                f.write(combo + "\n")


if __name__ == "__main__":
    run_bot()
