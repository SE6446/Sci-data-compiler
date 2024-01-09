# Sci_data_compiler
Turns Vernier csv data into matplotlib figures and json. I'm going to use this for my physics work. It can also be utilised on any datatable in a csv format. The exe can be used stand alone, no python required!

# README.txt
Contents:
1. Usage instructions
2. How to read .🧪.json files
3. License


## Usage instructions:
Upon starting the .exe file you'll be greeted with a plain alert box (This box has no presence in the task bar so you can't click off it without loosing it.) Be sure to have the .csv file on your clipboard (it doesn't matter if it is encased in quotes).

Enter the infomation as requested, more information about what each means below.
1. Enter .csv file path: enter the full path E.g C:\\Users\\{Your username}\\data\\experiment.csv (name of .csv file doesn't matter).
2. Enter number of columns: the number of columns in your data. As this program supports multiple datasets, it needs to know how many columns are in each. (it doesn't support non-regular dataset columns)
3. Enter output file name: the name of both the json file that is output and the directory it is stored in, you do NOT need to put in a file extension
4. Enter subject: the thing you did in the experiment. Purely an aesthetic variable to make the title look nice.
5. Use absolute?: tick if you want the program to read negative values as positive.

Press submit, if there is no error it should say "processed", you can now safely close the app (and the console window that is open)
Check for your folder named after the output file (it should be next to the folder the .exe is stored in) and voila! your data has been neatly compiled! The figures are saved as .png and other misc data is saved as .🧪.json (see below)

## How to read .🧪.json:
This file contains some other infomation that was processed such as: mean and range for the y-axis variable, gradient and y-intercept of the graph and some raw data from the .csv

When it is written by the program it will be seen as one line of data, mostly un-readable, you should format the file (such as using a website like: https://jsonformatter.org/)

From here you can read the data as needed.

## LICENSE:

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>

