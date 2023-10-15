# import numpy as np
# a=np.arange(1,10,3)
# b=np.arange(1,10,3)
# print(np.array_equiv(a,b))
import pandas as pd
import numpy as np
df = pd.DataFrame([['Татарников Иван Борисович','17', 'Введение в системы искусственного интеллекта']],columns=['ФИО','Возраст', 'Название курса'])
df.to_csv('tatarnikov.csv')