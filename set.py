#!/venv/bin/ python

"""
set.py: something something set
"""

__author__ = "Max Hariri-Turner"
__email__ = "maxkht8@gmail.com"

from selenium import webdriver

counts = [1, 2, 3]
fills = ["solid", "shaded", "empty"]
colors = ["red", "green", "purple"]
symbols = ["squiggle", "oval", "diamond"]
test = ["2 shaded red squiggle",
        "3 empty red diamond",
        "2 empty green oval",
        "1 solid green diamond",
        "1 shaded green oval",
        "2 empty green squiggle",
        "1 solid purple squiggle",
        "1 shaded green squiggle",
        "2 solid purple squiggle",
        "1 solid red oval",
        "3 shaded red squiggle",
        "2 shaded green oval"]


def solve(arr):
    sets = []
    count = 1
    for a in range(len(arr)):
        for b in range(a + 1, len(arr)):
            for c in range(b + 1, len(arr)):
                if a == b or a == c or b == c:
                    continue
                i = arr[a]
                j = arr[b]
                k = arr[c]
                bad = False
                for l in range(4):
                    if not ((i[l] == j[l] and j[l] == k[l]) or (i[l] != j[l] and i[l] != k[l] and j[l] != k[l])):
                        bad = True
                if not bad:
                    # print(f"set {count}:\n{i}\n{j}\n{k}\n")
                    set = [i, j, k]
                    sets.append(set)
                    count += 1
    return sets


def change_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def main():
    print("Starting up")
    # Initialize driver
    driver = webdriver.Chrome("./chromedriver")

    driver.get("https://www.setgame.com/set/puzzle")
    # driver.implicitly_wait(time_to_wait=2)
    arr = []
    table = {}
    for i in range(1, 13):  # internal code on the page starts with 1 instead of 0 for some reason
        scuffed_tuple = tuple([driver.execute_script(f'return board["theCards"][{i}]["shading"]'),
                               driver.execute_script(f'return board["theCards"][{i}]["symbol"]'),
                               driver.execute_script(f'return board["theCards"][{i}]["color"]'),
                               driver.execute_script(f'return board["theCards"][{i}]["number"]')])
        table[scuffed_tuple] = i
        arr.append(scuffed_tuple)

    for i in solve(arr):
        for card_tuple in i:
            driver.execute_script(f'board.cardClicked({table[card_tuple]})')
            # driver.implicitly_wait(time_to_wait=2)

    query = ""
    while query != "y":
        query = input("quit? ")

    print("Exiting")
    driver.quit()


if __name__ == "__main__":
    main()
