import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

current_path = os.path.join(os.path.dirname(__file__))
print(current_path)
file_path = current_path + '\个人碳足迹因子库.csv'
print(file_path)

data= pd.read_csv(file_path)
data.set_index(keys='Index', inplace=True)
print(data)
# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])
# print(chart_data)
# print(type(chart_data))



def calculate(item_name: str, value: int or float):
    return _calculate(item_name, value)


def _calculate(item_name: str, value: int or float):
    factor = _SearchFactor(item_name)

    return factor * value


def _SearchFactor(item_name: str):
    f = data.loc[item_name, '碳排放因子']

    return f
