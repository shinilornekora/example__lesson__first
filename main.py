#  Задана строка. Посчитать количество каждого символа в ней.
#  O(N^2), но можно решить за O(N) или за O(N*M)
#  JavaScript -> TypeScript (Enterprise), там такая же типизация.
# aaabbbcccdddddd
# Решение задаяи за O(N^2)
def symbolCounter(s: str):
    for sym in s:
        print(sym, s.count(sym))


# Решение задаяи за O(N * M), N - количество всех символов в строке, а M - количество уникальных симвыолов в строке
def symbolCounterBetter(s: str):
    for sym in set(s):
        print(sym, s.count(sym))


# Решение задаяи за O(N)
# O(2N) -> O(N)
#
def symbolCounterTheBest(s: str):
    symbols = {}
    for char in s:
        symbols[char] = symbols.get(char, 0) + 1
    print(symbols)
    # for char, counter in symbols.items():
    #     print(char, counter)


symbolCounter('aaabbbcccdddddd')
print('\n')
symbolCounterBetter('aaabbbcccdddddd')
print('\n')
symbolCounterTheBest('aaabbbcccdddddd')

