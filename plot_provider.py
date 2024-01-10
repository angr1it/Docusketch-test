import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class TaskPlotProvider:
    def __init__(self, data: pd.DataFrame):
        sns.set(style="darkgrid")
        self.data = data

    def _get_diviations(self) -> list[pd.Series]:
        return [
            pd.Series(
                data=self.data["floor_min"] - self.data["ceiling_min"], name="min_diff"
            ),
            pd.Series(
                data=self.data["floor_max"] - self.data["ceiling_max"], name="max_diff"
            ),
            pd.Series(
                data=self.data["floor_mean"] - self.data["ceiling_mean"],
                name="mean_diff",
            ),
        ]

    def get_heatmap(self):
        fig, ax = plt.subplots()
        fig.set_size_inches(10, 10)

        sns.heatmap(self.data.iloc[:, 1:].corr().round(2), annot=True, ax=ax)

        return fig

    def get_grid(self):
        grid = sns.PairGrid(self.data.iloc[:, 3:])

        grid.map_diag(sns.histplot, kde=True)
        grid.map_lower(sns.scatterplot)
        grid.map_upper(sns.kdeplot, fill=True)

        return grid.figure

    def get_hists(self):
        n_rows, n_cols = 3, 3
        fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(20, 20))
        for i, column in enumerate(self.data.columns[3:]):
            data = self.data[column]
            data = data[data < np.percentile(data, 95)]
            sns.histplot(data, kde=True, ax=axes[i % n_rows, i // n_cols])

        return fig

    def get_diff_diviations(self):
        fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(20, 20))
        for i, series in enumerate(self._get_diviations()):
            sns.histplot(series, kde=True, log_scale=True, ax=axes[i])
        return fig
