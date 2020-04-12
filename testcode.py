import pandas as pd
import numpy as np
from datetime import datetime
import random

df = pd.read_csv(r"D:\MFE Prep\PDSND\Project2 Files\bikeshare-2\chicago.csv")

df['Month'] = pd.to_datetime(df['Start Time']).dt.month
df['Day'] = pd.to_datetime(df['Start Time']).dt.day

# df2 = df[df['Month'] > 1]
# df2 = df2[df2['Month'] < 3]

df2 = df[(df.Month == 2)]
df2 = df2[(df2.Day == 6)]

x = [2, 3, 4, 1, 7, 8, 10]

random_int = random.randrange(len(df))

#x = 'january'
#x_date = datetime.strptime(x, '%b').month
#print(x_date)
#df['Concat'] = pd.concat(df, keys = ['Month', 'Day'])