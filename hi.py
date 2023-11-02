import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Importing Data
df = pd.read_csv("D:\dataset.csv")
#Data exploration
print("Return first 5 rows.","\n")
df.head()
print("Return last 5 rows.","\n")
df.tail()
df.info()
