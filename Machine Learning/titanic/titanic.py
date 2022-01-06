#데이터 분석 연습

import pandas as pd

titanic_df=pd.read_csv('G:\\python\\test\\titanic_train.csv')
#print(titanic_df.head(3))

#print(titanic_df.shape)

#print(titanic_df.info)

print(titanic_df['Survived'].value_counts())

print(titanic_df['Survived'].count())

titanic_df.head()
titanic_df['Age_0'] = 2
print(titanic_df.head())

for dataset in train_test_data:
    dataset["Age"].fillna(dataset["Age"].mean(), inplace=True)

for dataset in train_test_data:
    dataset['Embarked'].fillna('S', inplace=True)
