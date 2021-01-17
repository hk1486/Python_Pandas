import pandas as pd
import warnings 
warnings.filterwarnings('ignore')

exam_data = {'이름': ['서준','우현','인아'],
            '수학' : [90,80,70],
            '영어' : [98,89,95],
            '음악' : [85,95,100],
            '체육' : [100,90,90]}
            
df = pd.DataFrame(exam_data)
print(df)
print('-'*40)

df4 = df[:]
df4['국어'] = 70
print(df4)