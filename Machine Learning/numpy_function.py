#1. 넘파이를 통해 배열의 평균값 구하기.
import numpy as np

example = np.array([202,177,121,148,89,121,137,158])

"""
1. 평균계산
"""

example_mean = np.mean(coffee)

print("Mean :", round(example_mean,2)) #소수점 둘째자리까지 출력





# 2. stdev = 표준편차 계산
from statistics import stdev
import numpy as np

coffee = np.array([202,177,121,148,89,121,137,158])

"""
1. 표준편차 계산
"""
cf_std = stdev(coffee)

# 소수점 둘째 자리까지 반올림하여 출력합니다. 
print("Sample std.Dev : ", round(cf_std,2))
