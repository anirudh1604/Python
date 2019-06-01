import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
iris=pd.read_csv("iris.csv")

iris_setosa=iris[iris.species=='setosa']

sns.jointplot(x='petal_length',y='petal_width',data=iris_setosa,kind='kde')
plt.show()

