def greedy_algorithm(items, budget):
    # Сортування елементів за співвідношенням калорій до вартості
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = []

    for item, info in sorted_items:
        if info['cost'] <= budget:
            selected_items.append(item)
            budget -= info['cost']
            total_calories += info['calories']

    return selected_items, total_calories


def dynamic_programming(items, budget):
    # Створення таблиці для зберігання максимальних калорій для кожного бюджету
    dp = [0] * (budget + 1)
    item_list = [None] * (budget + 1)

    for item, info in items.items():
        cost, calories = info['cost'], info['calories']
        for current_budget in range(budget, cost - 1, -1):
            if dp[current_budget - cost] + calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - cost] + calories
                item_list[current_budget] = item

    total_calories = dp[budget]
    selected_items = []
    current_budget = budget

    while current_budget > 0 and item_list[current_budget] is not None:
        selected_items.append(item_list[current_budget])
        current_budget -= items[item_list[current_budget]]['cost']

    return selected_items, total_calories


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Виклик жадібного алгоритму
greedy_selected_items, greedy_total_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Обрані страви:", greedy_selected_items)
print("Калорії:", greedy_total_calories)

print('\n')

# Виклик алгоритму динамічного програмування
dp_selected_items, dp_total_calories = dynamic_programming(items, budget)
print("Динамічне програмування:")
print("Обрані страви:", dp_selected_items)
print("Калорії:", dp_total_calories)
