import pulp

model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable("Fruit_juice", lowBound=0, cat='Continuous')

model += lemonade + fruit_juice, "Total_Products"

model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
model += 1 * lemonade <= 50, "Sugar_Constraint"
model += 1 * lemonade <= 30, "Lemon_juice_Constraint"
model += 2 * fruit_juice <= 40, "Fruit_puree_Constraint"

model.solve()

if model.status == pulp.LpStatusOptimal:
    print(f"Оптимальна кількість 'Лимонаду' для виробництва: {lemonade.varValue}")
    print(f"Оптимальна кількість 'Фруктового соку' для виробництва: {fruit_juice.varValue}")
    print(f"Максимальна загальна кількість продуктів: {pulp.value(model.objective)}")
else:
    print("Неможливо знайти оптимальне рішення")
