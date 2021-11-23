#1. replace를 사용하여 male -> 0, female -> 1로 변환

import pandas as pd


titanic = pd.read_csv('./data/titanic.csv')
print('변환 전: \n',titanic['Sex'].head())

titanic = titanic.replace({'male':0,'female':1})

print('\n변환 후: \n',titanic['Sex'].head())
    



#1. get_dummies를 사용하여 변환.

import pandas as pd


titanic = pd.read_csv('./data/titanic.csv')
print('변환 전: \n',titanic['Embarked'].head())

dummies = pd.get_dummiese(titanic[['Embarked']])

print('\n변환 후: \n',dummies.head())
