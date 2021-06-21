import os
import pycparser

#hardcoded for now 22 jan, to take input from parser file
line_number = 4
variable_name = "[s]"
input_file_name = "uat_test1.c"

#filename hardcoded,  this output filename should be same as input, which is already user specified at parser intake
with open(input_file_name, 'r') as file:
    # read a list of lines into data
    data2 = file.readlines()
    data = ""

data = '#include "/home/klee/klee_src/include/klee/klee.h"'

sign = '&'
if  variable_name[0] == '[':
    sign = ''
    variable_name = variable_name[1:len(variable_name)-1]
print(variable_name)

#data2[line_number] = 'klee_make_symbolic('+ sign + variable_name + ', sizeof( ' + variable_name + ' ), ' + '"{}"'.format($

data2[line_number] = 'klee_make_symbolic('+ sign + variable_name + ', sizeof( ' + variable_name + ' ), ' + '"{}"'.format(variable_name) + ");\n"



#filename is still very hardcoded. this should be same name as above also.
# and write everything back
output_file_name = input_file_name[:len(input_file_name)-2] + "_out.c"
with open(output_file_name, 'w') as file:
    file.writelines(data+'\n')
    file.writelines(data2)



