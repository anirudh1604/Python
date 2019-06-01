import pandas as pd
from statsmodels import robust
import numpy as np
from matplotlib  import pyplot as plt #matplotlib.pyplot
import seaborn as sns

haber=pd.read_csv("haberman.csv")

def function_haber() :
    print(haber.shape) # Get rows and Columns
    print(haber.columns) # Get Name of Columns
    print(haber['status'].value_counts())
    print(haber['status'].value_counts(normalize=True))
    
    #print(haber['nodes'].value_counts())
    #print(haber['year'].value_counts())
    #print(haber.info())
    #print(list(haber['status'].unique()))
    print(haber.describe())
    '''print("For 1st as Status")
    haber_status_1=haber[haber['status']==1]
    print(haber_status_1.describe())
    print("\nFor 2nd as Status")
    haber_status_2=haber[haber['status']==2]
    print(haber_status_2.describe())
    '''
def pairplots() :
    sns.set_style("whitegrid")
    sns.pairplot(haber,hue='status',vars=['nodes','age','year']).add_legend()
    #sns.FacetGrid(haber,hue='status',size=4) \
     #   .map(plt.scatter,"nodes", "age" ) \
      #      .add_legend()
    plt.show()


def OneDScatter () :    
    sns.set_style("whitegrid")
    sns.FacetGrid(haber,hue='status',size=4) \
        .map(sns.distplot,"nodes" ) \
            .add_legend()
    plt.show()


def getPDF_CDF() :
    counts,bin_edges = np.histogram (haber["nodes"],bins=10,density=True) 
    pdf=counts/(sum(counts))
    print(pdf)
    cdf=np.cumsum(pdf)
    plt.plot(bin_edges[1:],pdf)
    plt.plot(bin_edges[1:],cdf)
    plt.show()

def box_Plot() :
    sns.boxplot(x='status',y='nodes',data=haber)
    #sns.boxplot(x='status',y='age',data=haber)
    #sns.boxplot(x='status',y='year',data=haber)
    plt.show()
    
def violin_Plot() :
    sns.violinplot(x='status',y='nodes',data=haber,height=8.0)
    plt.show()

def getMax_Nodes() :
    print(haber[haber.nodes == haber.nodes.max()].to_string(index=False))
    

class Haberman :
    choice = input("ENTER")
    choice=int(choice)
    if choice ==1 :
        function_haber()
    elif choice == 2 :
        getPDF_CDF()
    elif choice == 3 :
        box_Plot()
    elif choice ==4 :
        violin_Plot()
    elif choice ==5 :
        OneDScatter()
    elif choice ==6 :
        pairplots()       
    elif choice == 7:
        getMax_Nodes()

