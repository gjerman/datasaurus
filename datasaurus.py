import pandas as pd

class Datasaurus():
    def __init__(self):
        self.data = pd.read_csv("data/DatasaurusDozen.tsv", sep='\t')
    
    @property
    def dataset_names(self):
        return list(self.data.dataset.unique())
    
    def plot(self, dataset_name):
        if dataset_name in self.dataset_names:
            fig = self.data.loc[self.data.dataset==dataset_name].plot.scatter(x="x", y="y")
            return fig
        else:
            raise ValueError(f"Invalid dataset name, avaible dataset are: {self.dataset_names}")
        
    def plot_all(self):
        for dataset in self.dataset_names:
            self.plot(dataset)
    
    def get_dataset(self,dataset_name):
        if dataset_name in self.dataset_names():
            return self.data.loc[self.data.dataset==dataset_name]
        else:
            raise ValueError(f"Invalid dataset name, avaible dataset are: {self.dataset_names}")
        
    @property
    def all_datasets(self):
        return self.data
    
    @property
    def summary_stats(self):
        for dataset in self.dataset_names:
            data = self.data.loc[self.data.dataset==dataset]
            print(f"Dataset: {dataset}\n")
            print(data.describe().loc[["mean","std"]].round(decimals=3))
            print(f"Corr.{data.x.corr(data.y,method='pearson', min_periods=1).round(decimals=3)}")
            print("\n")
