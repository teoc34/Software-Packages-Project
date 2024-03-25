# import the necessary libraries
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.discriminant_analysis import StandardScaler
import statsmodels.api as sm
graduates = pd.read_csv('data/Graduates.csv',delimiter=';', index_col=0)
registered = pd.read_csv('data/Registered.csv', delimiter=';', index_col=0)
labs = pd.read_csv('data/Labs.csv', delimiter=';', index_col=0)
population = pd.read_csv('data/Population.csv', delimiter=';', index_col=0)
dropout_rate = pd.read_csv('data/Dropout_rate.csv', delimiter=';', index_col=0)
poverty = pd.read_csv('data/Poverty.csv', delimiter=';', index_col=0)

