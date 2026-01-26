#export FINANCE_FILE="../expenses.xlsx"
#python via_env.py
import os
import pandas as pd

file_path = os.getenv("FINANCE_FILE")

if file_path is None:
    print("Помилка: змінна середовища FINANCE_FILE не задана")
else:
    df = pd.read_excel(file_path)
    print("Файл успішно зчитано")
