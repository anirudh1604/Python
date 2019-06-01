import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
iris=pd.read_csv("iris.csv")
sns.FacetGrid(iris,hue='species',size=5) \
    .map(sns.distplot,"petal_length") \
        .add_legend()
#plt.show()
plt.show()
