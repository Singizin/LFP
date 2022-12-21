from datetime import datetime
import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv('files/3-65-3N.csv', sep=';')
row = df.iloc[1]
print(row['date'] + ' ' + row['time'])
print(datetime.strptime(row['date'] + ' ' + row['time'], '%d.%m.%Y %H:%M:%S'))
list_of_df = []
new_df = pd.DataFrame(columns=df.columns)

current_cycle = 0

new_time = 0
for index in range(0, df.shape[0], 100):
    row = df.iloc[index]
    if row['cycle_1'] == 0:
        continue
    if row['cycle_1'] != current_cycle:
        new_time = datetime.strptime(row['date'] + ' ' + row['time'], '%d.%m.%Y %H:%M:%S')
        current_cycle = row['cycle_1']
        list_of_df.append(new_df)
        new_df = pd.DataFrame(columns=df.columns)
    if new_time:
        row['time'] = (datetime.strptime(row['date'] + ' ' + row['time'], '%d.%m.%Y %H:%M:%S') - new_time).seconds

    new_df = new_df.append(row, ignore_index=True)


print(list_of_df)

super_df = pd.concat(list_of_df)
super_df.to_csv('files/xxx.csv', sep=';')
