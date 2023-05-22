import pandas as pd

# загрузка файла california_housing_test.csv с помощью pandas
df = pd.read_csv('california_housing_test.csv')

# вывод количества строк и столбцов в файле
print(f'Количество строк: {len(df.index)}')
print(f'Количество столбцов: {len(df.columns)}')

# определение типа данных имеющихся столбцов
print('Типы данных столбцов:')
for col in df.columns:
    print(f'{col}: {df[col].dtype}')

# проверка наличия пустых значений
if df.isnull().values.any():
    print('В файле есть пустые значения')
else:
    print('В файле нет пустых значений')
