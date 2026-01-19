import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('excel.xlsx')

print(df)

plt.bar(df['name'], df['age'])
plt.title('Ages of Individuals')
plt.xlabel('Person')
plt.ylabel('Age')
plt.show()