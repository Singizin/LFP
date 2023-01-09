from datetime import datetime
import matplotlib.pyplot as plt

import pandas as pd

# states = {
#     1: "заряд батареи",
#     2: "разряд батареи в цикле",
#     3: "выдержка перед изменением напряжения (разряд)",
#     5: "выдержка перед изменением напряжения (заряд)",
#     6: "разряд батареи постонным током (измрительный)"
# }

states = {
    1: "charging",
    2: "discharge cycle",
    3: "held before discharge",
    5: "held before charge",
    6: "discharge measure"
}

columns = [
    'date', 'time',
    'cycle_1', 'status_1', 'U_1', 'I_1',
    'cycle_2', 'status_2', 'U_2', 'I_2',
    'cycle_3', 'status_3', 'U_3', 'I_3',
    'e'
]

add_columns = [
    'seconds',
    'charging',
    'discharge cycle',
    'held before discharge',
    'held before charge',
    'discharge measure',
]

file_path = 'D:/Тестирование LFP/Тестирование LFP/'

df = pd.read_csv(f'{file_path}3-65-3N.csv', sep=';', names=columns)

df[add_columns] = 0


list_of_df = []

new_df = pd.DataFrame(columns=df.columns)
current_cycle = 0


def to_datetime(row: pd.Series, str_format='%d.%m.%Y %H:%M:%S'):
    return datetime.strptime(row['date'] + ' ' + row['time'], str_format)


new_time = 0
for index, item in df.iloc[:50000].iterrows():
    row = item
    # print(row)
    if row['cycle_1'] == 0:
        continue
    if row['cycle_1'] != current_cycle:
        new_time = to_datetime(row)
        current_cycle = row['cycle_1']
        list_of_df.append(new_df)
        print('len list_of_df', len(list_of_df))
        new_df = pd.DataFrame(columns=df.columns)
    if new_time:
        row['seconds'] = (to_datetime(row) - new_time).seconds
        row[states.get(row['status_1'])] = 1

    new_df = new_df.append(row, ignore_index=True)
    # print('23',new_df)
# print(new_df.iloc[:,13:])
# exit(1)
for d in list_of_df[1]:
    plt.plot(d.loc([:,['U_1']]))
    plt.plot(d.loc(['I_1']))

plt.show()
exit(1)
super_df = pd.concat(list_of_df)
super_df.to_csv('files/xxx.csv', sep=';')
