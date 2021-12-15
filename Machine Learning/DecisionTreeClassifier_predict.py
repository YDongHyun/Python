import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree

# sklearn에 저장된 데이터를 불러옴
X, Y = load_iris(return_X_y = True)

# DataFrame으로 변환
df = pd.DataFrame(X, columns=['꽃받침 길이','꽃받침 넓이', '꽃잎 길이', '꽃잎 넓이'])
df['클래스'] = Y

X = df.drop(columns=['클래스'])
Y = df['클래스']
    
# 학습용 평가용 데이터로 분리
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.2, random_state = 42)

# DTmodel에 의사결정나무 모델을 초기화 하고 학습
DTmodel = DecisionTreeClassifier()
DTmodel.fit(train_X, train_Y)


# test_X에 대해서 예측
pred_X = DTmodel.predict(test_X)
print('test_X에 대한 예측값 : \n{}'.format(pred_X))
