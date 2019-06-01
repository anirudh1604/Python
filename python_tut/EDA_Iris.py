import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
iris=pd.read_csv("iris.csv")
#print (iris.shape)
#print(iris.columns)
#print(iris["species"].value_counts())
#iris.plot(kind='scatter',x='sepal_length',y='sepal_width')
#sns.set_style("ticks")
#sns.FacetGrid(iris,hue='species',size=4) \
 #   .map(plt.scatter,"sepal_length","sepal_width") \
  #      .add_legend()
#plt.show()
sns.set_style("ticks")
sns.pairplot(iris,hue='species',height=3)
plt.show()
