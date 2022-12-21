import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('files/xxx.csv', sep=';')
new_df = pd.DataFrame(columns=df.columns)
list_of_df = []
current_cycle = 1

len_of_cycle = []

for i in range(90):
    selected: pd.DataFrame = df.loc[df['cycle_1'] == i]
    list_of_df.append(selected)

for i in list_of_df[10:30]:
    plt.plot(i.iloc[:, [2]], i.iloc[:, [5]],linewidth=1)

# print(len_of_cycle)
plt.show()
