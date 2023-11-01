import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import pandas
from math import isnan
from statistics import mean
import json
class CsvToPlt():
    def __init__(self,csv_path:str) -> None:
        self.csv_list = self.__csv_to_list(csv_path)

    def __csv_to_list(self,csv_path) -> list:
        dataframes = pandas.read_csv(csv_path)
        self.columns = dataframes.columns
        data = dataframes.values
        data2 = []
        for i in range(0,len(data)):
            row = data[i]
            temp_dict = {dataframes.columns[0]:row[0],dataframes.columns[1]:row[1],dataframes.columns[2]:row[2]}
            data2.append(temp_dict)
        return data2
    

    def list_to_scatter(self,title:str,x_label,y_label,column_for_y:int = 1,lobf:bool = False,cobf:bool = False,save:bool = False,save_name:str|None = None,show:bool = True):
        x_axis = []
        y_axis = []
        for i in self.csv_list:
            if not isnan(i[self.columns[column_for_y]]):
                y_axis.append(float(i[self.columns[column_for_y]]))
                x_axis.append(float(i[self.columns[0]]))
        #* convert to numpy
        x = np.array(x_axis)
        y = np.array(y_axis)
        plt.scatter(x,y)
        #*line of best fit
        if lobf:
            a,b = np.polyfit(x,y,1)
            plt.plot(x,a*x+b)
        elif cobf:
            #! Not implemented
            raise NotImplementedError()
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        if save:
            plt.savefig(save_name+".png")
        if show:
            #* show figure
            plt.show()
    def find_mean_and_range(self,idx):
        column = []
        for i in self.csv_list:
            if not isnan(i[self.columns[idx]]):
                column.append(i[self.columns[idx]])
        return mean(column), max(column) - min(column)
    def compile_all_data(self,output_file):
        file = open(output_file+".🧪.json","w")
        for i in range(1,len(self.columns)):
            save_name = f"column_{i}_over_column_0"
            self.list_to_scatter(f"{self.columns[i]} over {self.columns[0]}",
                                 self.columns[0],
                                 self.columns[i],
                                 i,
                                 lobf= True,
                                 show= False,
                                 save= True,
                                 save_name= save_name
                                 )
            plt.clf()
        json.dump({"figure_location":save_name+".png","mean_and_range":self.find_mean_and_range(i),"csv-data":self.csv_list},file)
    #TODO Make a subplot version of scatter.



if __name__ == "__main__":
    freefall = CsvToPlt("MT\csv-export-free-fall - Copy.csv")
    freefall.compile_all_data("Freefall_data")