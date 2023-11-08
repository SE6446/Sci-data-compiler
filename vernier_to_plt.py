import matplotlib.pyplot as plt
import numpy as np
import pandas
from math import isnan
from statistics import mean
from json import dump
import re
from os import mkdir, chdir, getcwd
class CsvToPlt():
    def __init__(self,csv_path:str,split:int=2,abs:bool = False) -> None:
        self.csv_list = self.__csv_to_list(csv_path,split)
        self.abs = abs


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
        for h in range(0,number_ds):
            temp_list =[]
            for i in range(0,len(data)):
                temp_dict = {}
                row = data[i].astype(np.float_)
                for j in range(0,len(row)):
                    temp_dict[self.columns[j]] = row[j]
                j = 0
                temp_list.append(temp_dict)
            i = 0
            new_data.append(temp_list)
        assert len(new_data) != 0#* To ensure list is not empty (Which would be bad)
        return new_data
    
    #? This name is no longer relevant, should I rename the function?
    def list_to_scatter(self,title:str,x_label,y_label,column_for_y:int = 1,lobf:bool = False,cobf:bool = False,save:bool = False,save_name:str|None = None,show:bool = True,dataset:int = 0,colour:str = "r"):
        x,y = self._dataset_to_coords(dataset,column_for_y)
        plt.scatter(x,y,color=colour)
        try:
            #*line of best fit
            if lobf:
                a,b = np.polyfit(x,y,1)
                self.gradient = a
                self.y_intercept = b
                self.function = f"y={a}x+{b}"
                plt.plot(x,a*x+b,color=colour)
            #*curve of best fit
            elif cobf:
                print("[SYS NOTE] Be sure you have the correct degrees inputted")
                model = np.poly1d(np.polyfit(x, y, 2))
                polyline = np.linspace(x[0]-1, x[len(x)-1]+1)
                plt.plot(polyline, model(polyline), color=colour)
                self.gradient = np.nan
                self.y_intercept = np.nan
                self.function = model
        except:
            print("[ERROR] graph failed, skipping...")
            plt.clf()
            return None
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.grid()
        if save:
            plt.savefig(save_name+".png")
        if show:
            #* show figure
            plt.show()


    def find_mean_and_range(self,idx,dataset:int = 0):
        liste = self.csv_list[dataset]
        column = []
        for i in liste:
            if not isnan(i[self.columns[idx]]):
                column.append(i[self.columns[idx]])
        try:
            return mean(column), max(column) - min(column)
        except:
            print("[ERROR] mean failed... returning none.")
            return None
    

    def compile_all_data(self,output_file,subject:str = "null",dataset:int=0,lobf:bool=True,colour:str='b'):
        try:
            mkdir(f"{getcwd()}\\{output_file}")
        except:
            print("[ERROR] Directory already exists...")
        chdir(f"{getcwd()}\\{output_file}")
        file = open(output_file+".🧪.json","w")
        temp_list = []
        for i in range(1,len(self.columns)):
            save_name = f"{self.columns[i].replace('/','')}_over_{self.columns[0]}"
            self.list_to_scatter(f"{self.columns[i]} over {self.columns[0]} graph of {subject}",
                                 self.columns[0],
                                 self.columns[i],
                                 i,
                                 lobf= lobf,
                                 cobf= not lobf,
                                 show= False,
                                 save= True,
                                 save_name= save_name,
                                 dataset=dataset,
                                 colour=colour
                                 )
            plt.clf()
            self.plot_line(
                f"{self.columns[i]} over {self.columns[0]}",
                self.columns[0],
                self.columns[i],
                i,
                True,
                save_name + "_line",
                False,
                dataset,
                colour
            )
            plt.clf()
            temp_list.append({"figure_location":getcwd()+save_name+".png","mean_and_range":self.find_mean_and_range(i),"gradient":self.gradient,"y-intercept":self.y_intercept,"function":self.function})
        dump([temp_list,self.csv_list],file)


    def plot_line(self,title:str,x_label,y_label,column_for_y:int=1,save:bool = False,save_name:str|None = None,show:bool=True,dataset:int=0,colour:str = 'b'):
        x,y = self._dataset_to_coords(dataset,column_for_y=column_for_y)
        plt.plot(x,y,color=colour)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.grid()
        if save:
            plt.savefig(save_name+".png")
        if show:
            #* show figure
            plt.show()
    def _dataset_to_coords(self,dataset:int=0,column_for_y:int=1):
                liste = self.csv_list[dataset]
                x_axis = []
                y_axis = []
                for i in liste:
                    if not isnan(i[self.columns[column_for_y]]) and self.abs == False:
                        y_axis.append(float(i[self.columns[column_for_y]]))
                        x_axis.append(float(i[self.columns[0]]))
                    elif not isnan(i[self.columns[column_for_y]]) and self.abs == True:
                        y_axis.append(abs(float(i[self.columns[column_for_y]])))
                        x_axis.append(abs(float(i[self.columns[0]])))
                #* convert to numpy
                x = np.array(x_axis)
                y = np.array(y_axis)
                return x,y


if __name__ == "__main__":
    data = CsvToPlt(input("Input CSV file: "),4,False)
    data.list_to_scatter("test","time","?",2,dataset=0,cobf=True)
    #data.compile_all_data(input("Input name of output file: "),lobf=False,colour='r')