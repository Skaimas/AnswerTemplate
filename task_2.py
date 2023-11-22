increase = 0.03
salary = 30000
spend = 45000
money_capital = 0

for i in range(10):
    if i == 0:
        money_capital = money_capital - salary + spend
        i += 1
    else:
        spend = spend + (spend * increase)
        money_capital = money_capital + spend - salary
        i += 1

print(f"Требуемая подушка "
      f"безопасности чтобы прожить 10 месяцев = {round(money_capital, 2)}")