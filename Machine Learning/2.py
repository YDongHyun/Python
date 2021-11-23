import pandas as pd

titanic = pd.read_csv('./data/titanic.csv')
print(titanic.info(),'\n')

"""
1. Cabin 변수 제거
"""
titanic_1 = titanic.drop(columns=["Cabin"])
print('Cabin 변수 제거')
print(titanic_1.info(),'\n')

"""
2. 결측값이 존재하는 샘플 제거
"""
titanic_2 = titanic_1.dropna()
print('결측값이 존재하는 샘플 제거')
print(titanic_2.info())
