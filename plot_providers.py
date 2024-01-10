import pandas as pd
import matplotlib.pyplot as plt


class TaskPlotProvider:
    def __init__(self, data: pd.DataFrame):
        try:
            pass
        except KeyError:
            print("Given dataframe is different from the one specified in the task.")
