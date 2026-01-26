import pandas as pd

# Load Excel file
df = pd.read_excel("expenses.xlsx")

total_spent = 0
category_totals = {}

for index, row in df.iterrows():
    amount = row["amount"]
    category = row["category"]

    total_spent += amount

    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount

print("Загальні витрати:", total_spent)
print("Витрати по категоріях:", category_totals)
