money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month = 0
percent = 1
while True:
    money_capital += salary - spend * percent
    percent += percent * increase
    if money_capital > 0:
        month += 1
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", month)
