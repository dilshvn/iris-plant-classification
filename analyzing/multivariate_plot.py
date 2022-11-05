import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv('https://sololearn.com/uploads/files/iris.csv')

# build a dict mapping species to an integer code
inv_name_dict = {'iris-setosa': 0, 'iris-versicolor': 1, 'iris-virginica': 2}

# build integer color code 0/1/2
colors = [inv_name_dict[item] for item in iris['species']]

# scatter plot
scatter = plt.scatter(iris['sepal_len'], iris['sepal_wd'], c = colors)

plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')

## add legend
plt.legend(handles=scatter.legend_elements()[0], labels = inv_name_dict.keys())
plt.savefig("plot.png")
plt.show()