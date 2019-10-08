from cs50 import get_float

while True:
    change_owed = get_float("Change owed: ")
    if change_owed > 0:
        break


# convert change_owed into cents
cents = round(change_owed * 100)

# list available coins
coins = [25, 10, 5, 1]

minimum_coins = 0

# Iterate over coins list
for coin in coins:
    # If the change_owed matches the coin
    if cents == coin:
        minimum_coins += 1
        break
    # else take the integer-divion and remainder to find the num of coins required
    elif cents > coin:
        division = cents // coin
        minimum_coins += division if division > 0 else 0
        cents = cents % coin

print(minimum_coins)