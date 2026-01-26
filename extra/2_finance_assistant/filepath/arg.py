#python arg.py finance.xlsx
import sys
import pandas as pd

if len(sys.argv) < 2:
    print("Помилка: вкажіть шлях до Excel файлу")
    print("Приклад: python arg.py finance.xlsx")
else:
    file_path = sys.argv[1]
    df = pd.read_excel(file_path)
    print("Файл успішно зчитано:", file_path)
