import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

np.random.seed(100)
tf.random.set_seed(100)

# 데이터를 DataFrame 형태로 불러옴
df = pd.read_csv("data/Advertising.csv")

# DataFrame 데이터 샘플 5개 출력
print('원본 데이터 샘플 :')
print(df.head(),'\n')

# 의미없는 변수 삭제
df = df.drop(columns=['Unnamed: 0'])

X = df.drop(columns=['Sales'])
Y = df['Sales']

# 학습용 테스트용 데이터 분리
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.3)

# Dataset 형태로 변환합니다.
train_ds = tf.data.Dataset.from_tensor_slices((train_X.values, train_Y))
train_ds = train_ds.shuffle(len(train_X)).batch(batch_size=5)


# keras를 활용하여 신경망 모델 생성
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, input_shape=(3,)),
    tf.keras.layers.Dense(1)
    ])


"""
1. 학습용 데이터를 바탕으로 모델의 학습을 수행
    
step1. compile 메서드를 사용하여 최적화 모델 설정
       loss는 mean_squared_error, optimizer는 adam으로 설정
       
step2. fit 메서드를 사용하여 Dataset으로 변환된 학습용 데이터를 학습
       epochs는 100으로 설정
"""
model.compile(loss='mean_squared_error', optimizer='adam')
history = model.fit(train_ds, epochs=100, verbose=2)
