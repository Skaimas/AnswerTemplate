money_capital = 100000
salary = 40000
spend = 50000
increase = 0.05
amount_month = 0

while (money_capital - spend + salary - (spend * increase)) >= 0:
    if amount_month == 0:
        money_capital = money_capital - spend + salary
        amount_month += 1
    else:
        spend = spend + (spend * increase)
        money_capital = money_capital - spend + salary
        amount_month += 1

print(f"Количество месяцев без долгов = {amount_month}")
