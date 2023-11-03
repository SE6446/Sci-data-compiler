import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
import pandas
from math import isnan
from statistics import mean
import json
import re

class CsvToPlt():
    def __init__(self,csv_path:str,split:int=2) -> None:
        self.csv_list = self.__csv_to_list(csv_path,split)
    #TODO Make functionanlity for more than one data set.
    #!####################################################
    #* Pseudo-code
    # [{output of code below, up to number of columns in DS},{},{}]
    # new param = number of columns in 1 DS
    # split columns into new param
    #!####################################################
    def __csv_to_list(self,csv_path,split:int) -> list:
        dataframes = pandas.read_csv(csv_path)
        columns = dataframes.columns
        new_columns = []
        for i in range(0,len(columns)):
            new_columns.append(re.sub(r'Data Set .:','',columns[i]))
        self.columns = new_columns           
        data = dataframes.values
        new_data = []
        number_ds = int(len(new_columns)/split)
        iteration = 0
        for h in range(0,number_ds):
            temp_list =[]
            for i in range(0,len(data)):
                temp_dict = {}
                row = data[i]
                for j in range(0,len(row)):
                    temp_dict[self.columns[j]] = row[j]
                j = 0
                temp_list.append(temp_dict)
            i = 0
            new_data.append(temp_list)
        return new_data
    

    def list_to_scatter(self,title:str,x_label,y_label,column_for_y:int = 1,lobf:bool = False,cobf:bool = False,save:bool = False,save_name:str|None = None,show:bool = True,dataset:int = 0):
        liste = self.csv_list[dataset]
        x_axis = []
        y_axis = []
        for i in liste:
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
        #*curve of best fit
        elif cobf:
            def func(x, a, b, c):
                return a * np.exp(-b * x) + c
            #raise NotImplementedError()
            # Plot the actual data  
            plt.plot(x, y, ".",)

            optimizedParameters, pcov = opt.curve_fit(func, x, y)

            # Use the optimized parameters to plot the best fit
            plt.plot(x, func(x, *optimizedParameters))
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
    

    def compile_all_data(self,output_file,subject:str = "null"):
        raise Exception()
        file = open(output_file+".🧪.json","w")
        temp_list = []
        for i in range(1,len(self.columns)):
            save_name = f"{self.columns[i].replace('/','')}_over_{self.columns[0]}"
            self.list_to_scatter(f"{self.columns[i]} over {self.columns[0]} graph of {subject}",
                                 self.columns[0],
                                 self.columns[i],
                                 i,
                                 lobf= True,
                                 show= False,
                                 save= True,
                                 save_name= save_name
                                 )
            plt.clf()
            self.plot_line(
                f"{self.columns[i]} over {self.columns[0]}",
                self.columns[0],
                self.columns[i],
                i,
                True,
                save_name + "_line",
                False
            )
            plt.clf()
            temp_list.append({"figure_location":save_name+".png","mean_and_range":self.find_mean_and_range(i)})
        json.dump([temp_list,self.csv_list],file)


    def plot_line(self,title:str,x_label,y_label,column_for_y:int = 1,save:bool = False,save_name:str|None = None,show:bool=True):
        raise Exception()
        x_axis = []
        y_axis = []
        for i in self.csv_list:
            if not isnan(i[self.columns[column_for_y]]):
                y_axis.append(float(i[self.columns[column_for_y]]))
                x_axis.append(float(i[self.columns[0]]))
        #* convert to numpy
        x = np.array(x_axis)
        y = np.array(y_axis)
        plt.plot(x,y)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        if save:
            plt.savefig(save_name+".png")
        if show:
            #* show figure
            plt.show()



if __name__ == "__main__":
    freefall = CsvToPlt(input("Input CSV file: "),split=5)
    freefall.list_to_scatter("test","time","?",1)
    #freefall.compile_all_data(input("Input name of output file: "))