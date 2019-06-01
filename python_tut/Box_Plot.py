import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
iris=pd.read_csv("iris.csv")


sns.boxplot(x='species',y='petal_length',data=iris)
plt.show()


sns.violinplot(x='species',y='petal_length',data=iris)
plt.show()