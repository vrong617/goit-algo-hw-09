def find_coins_greedy(amount, coins):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count
    return result


def find_min_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    coin_used = [-1] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin == -1:
            return {}
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


coins = [50, 25, 10, 5, 2, 1]
amount = 113
print(f"Монети: {coins}", f"Сума: {amount}", sep="\n")
greedy_result = find_coins_greedy(amount, coins)
print(f"Жадібний алгоритм: {greedy_result}")
dp_result = find_min_coins(amount, coins)
print(f"Динамічне програмування: {dp_result}")

coins = [10, 6, 1]
amount = 12
print(f"Монети: {coins}", f"Сума: {amount}", sep="\n")
greedy_result = find_coins_greedy(amount, coins)
print(f"Жадібний алгоритм: {greedy_result}")
dp_result = find_min_coins(amount, coins)
print(f"Динамічне програмування: {dp_result}")
