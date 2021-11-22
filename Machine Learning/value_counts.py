import pandas as pd 
import numpy as np

#Attend : 참석한 경우 1, 참석하지 않은 경우 0
#Name : 참석자의 이름
# example 데이터
example = pd.read_csv("example.csv")

"""
1. 도수 계산
"""

example_freq = example[example['Attend']==1]['Name'].value_counts()

print("도수분포표")
print(example_freq)
