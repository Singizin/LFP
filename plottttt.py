import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('files/xxx.csv', sep=';')
new_df = pd.DataFrame(columns=df.columns)
print(df.iloc[[1], [2, 5]])
list_of_df = []
current_cycle = 1


for i in range(20):
    selected = df.where(df['cycle_1'] == i)
    list_of_df.append(selected)

for i in list_of_df:
    plt.plot(i.iloc[:, [2]], i.iloc[:, [5]])
plt.show()
