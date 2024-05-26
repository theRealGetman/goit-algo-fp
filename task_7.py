import random
import matplotlib.pyplot as plt

# Функція для симуляції кидків кубиків


def roll_dice(num_rolls):
    # Масив для підрахунку частоти сум (0 і 1 не використовуються)
    results = [0] * 13

    for _ in range(num_rolls):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        results[roll_sum] += 1

    return results

# Функція для обчислення ймовірностей


def calculate_probabilities(results, num_rolls):
    probabilities = [count / num_rolls for count in results]
    return probabilities


# Кількість симуляцій
num_rolls = 1000000

# Симуляція кидків кубиків
results = roll_dice(num_rolls)

# Обчислення ймовірностей
probabilities = calculate_probabilities(results, num_rolls)

# Теоретичні ймовірності для порівняння
theoretical_probabilities = [0, 0, 1/36, 2/36, 3/36,
                             4/36, 5/36, 6/36, 5/36,
                             4/36, 3/36, 2/36, 1/36]

# Відображення результатів
sums = list(range(2, 13))
mc_probabilities = probabilities[2:13]

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.bar(sums, mc_probabilities, width=0.4,
        label='Monte Carlo', color='blue', alpha=0.6)
plt.bar([x + 0.4 for x in sums], theoretical_probabilities[2:],
        width=0.4, label='Theoretical', color='red', alpha=0.6)
plt.xlabel('Сума')
plt.ylabel('Ймовірність')
plt.title('Ймовірності сум при киданні двох кубиків')
plt.xticks(sums)
plt.legend()
plt.show()

# Виведення результатів у вигляді таблиці
print("Сума\tMonte Carlo\tТеоретична")
for sum_value in sums:
    print(f"{sum_value}\t{mc_probabilities[sum_value-2]*100:.2f}%\t\t{
          theoretical_probabilities[sum_value]*100:.2f}%")
