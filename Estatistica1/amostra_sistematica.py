import numpy as np
import pandas as pd
from math import ceil
from sklearn.model_selection import train_test_split

populacao = 150
amostra = 15
k = ceil(populacao/amostra)

r = np.random.randint(low = 1, high = k+1, size = 1)

k_means