import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
d = pd.read_csv('https://raw.githubusercontent.com/ondata/covid19italia/master/publication/provinceArchivio.csv')
df = pd.read_csv('cov.csv')

sns.barplot(data = df, x = df['provincia'], y = df['numero']);

plt.show()

print(df)





