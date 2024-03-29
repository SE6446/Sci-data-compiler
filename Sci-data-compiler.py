import matplotlib.pyplot as plt
import numpy as np
import pandas
from math import isnan
from statistics import mean
from json import dump
import re
from os import mkdir, chdir, getcwd
import argparse
from datetime import date
class CsvToPlt():
    def __init__(self,file_path:str,split:int=2,abs:bool = False) -> None:
        if file_path.endswith(".csv"):
            dataframe = pandas.read_csv(file_path)
            self.csv_list = self.__csv_to_list(dataframe,split)
        elif file_path.endswith(".xlsx"):
            dataframe = pandas.read_excel(file_path)
            self.csv_list = self.__csv_to_list(dataframe,split)
        else:
            raise Exception("Invalid file type selected.")
        self.abs = abs
        

    def __csv_to_list(self,dataframes,split:int) -> list:
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
    
    def plot_scatter(self,title:str,x_label,y_label,column_for_y:int = 0,lobf:bool = False,cobf:bool = False,save:bool = False,save_name:str|None = None,show:bool = True,dataset:int = 0,colour:str = "r",degree:int = 2,yerr:float = 0.01,xerr:float=0.01):
        if cobf == True and degree <= 1:
            raise Exception("[Error] Please input a degree over 1, if you want to use a degree of 1, please use ")
        x,y = self._dataset_to_coords(dataset,column_for_y)
        if yerr !=0 and xerr != 0:
            plt.errorbar(x,y,yerr,xerr,color=colour, fmt= "x", linewidth=2, capsize=6)
        else:
            plt.scatter(x,y,marker="x")
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
                model = np.poly1d(np.polyfit(x, y, degree))
                polyline = np.linspace(x[0]-1, x[len(x)-1]+1)
                plt.plot(polyline, model(polyline), color=colour)
                self.gradient = np.nan
                self.y_intercept = np.nan
                self.function = str(model)
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
    
    def barChart(self, title:str, ): #TODO make this
        raise NotImplementedError()

    def compile_all_data(self,title:str|None,output_file,subject:str = "null",dataset:int=0,lobf:bool=True,colour:str='b',degree:int = 2,xerror:float = 0,yerror:float=0):
        try:
            mkdir(f"{getcwd()}\\{output_file}")
        except:
            print("[ERROR] Directory already exists...")
        chdir(f"{getcwd()}\\{output_file}")
        file = open(output_file+".🧪.json","w")
        temp_list = []
        for i in range(1,len(self.columns)):
            save_name = f"{title}_{i}" if title != None else f"{self.columns[i].replace('/','')}_over_{self.columns[0]}"
            self.plot_scatter(title if title != None else f"{self.columns[i]} over {self.columns[0]} graph of {subject}",
                                 self.columns[0],
                                 self.columns[i],
                                 i,
                                 lobf= lobf,
                                 cobf= not lobf,
                                 show= False,
                                 save= True,
                                 save_name= save_name,
                                 dataset=dataset,
                                 colour=colour,
                                 degree=degree,
                                 xerr=xerror,
                                 yerr=yerror
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
        print(getcwd())
        dump([temp_list,self.csv_list],file)
        return getcwd()


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

parser = argparse.ArgumentParser("Sci-data-compiler")
parser.add_argument('filename',help="The path to the file in question")
parser.add_argument("-s","--split",help="How many datasets there are, defaults to 2.",default=2)
parser.add_argument('-a','--absolute',help="use absolute values",action="store_true",default=False)
parser.add_argument('-t','--title',help="Optional title of the information",default=None)
parser.add_argument('-o','--output_file',default="test_"+str(date.today()))
parser.add_argument('-i','--subject',help='subject of the data: i.e a bouncing ball. defaults to null')
parser.add_argument('--cobf',help='applies a curve of best fit to your graphs', action='store_false')
parser.add_argument('-x','--xerror',help='the absolute error on the x-axis',default=0)
parser.add_argument('-y','--yerror',help='the error on the y axis',default=0)
args = parser.parse_args()



data = CsvToPlt(args.filename,args.split,args.absolute)
data.compile_all_data(args.title,args.output_file,args.subject,args.cobf,colour='b',xerror=args.xerror,yerror=args.yerror)