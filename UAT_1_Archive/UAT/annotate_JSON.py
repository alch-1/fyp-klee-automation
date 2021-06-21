import os
import pycparser
import os.path


def annotate(filename, variable_name, is_array, line_number):
    #print(filename, variable_name, is_array, line_number)
    line_number = int(line_number)
    output_file_name = filename[:len(filename)-2] + "_annotated.c"

    if os.path.isfile(output_file_name):
        #print(1)
        with open(output_file_name, 'r') as file:
            # read a list of lines into data
            data2 = file.readlines()
            data = ""
    else:
        with open(filename, 'r') as file:
            #print(2)
            # read a list of lines into data
            data2 = file.readlines()
            #data = '#include "/home/klee/klee_src/include/klee/klee.h"
            data2.insert(0, '#include "/home/klee/klee_src/include/klee/klee.h"\n')
            with open(output_file_name, 'w+') as file:
                file.writelines(data2)

    # handle angled include
    for index, line in enumerate(data2):
        if (("#include" in line) and ("<" in line) and (">" in line)):
            print("Replacing " + line + "...")
            tmp = line.replace("<", '"', 1)
            tmp = tmp.replace(">", '"', 1)
            data2[index] = tmp

    sign = '&'
    if  is_array:
        sign = ''

    #data2[line_number] = 'klee_make_symbolic('+ sign + variable_name + ', sizeof(' + variable_name + '), \"' +  variable_name + '\");\n'
    data2.insert(line_number, 'klee_make_symbolic('+ sign + variable_name + ', sizeof(' + variable_name + '), \"' +  variable_name + '\");\n')

    #and write everything back
    with open(output_file_name, 'w+') as file:
        #file.writelines(data+'\n')
        file.writelines(data2)

    #command = " clang -I ../../include -emit-llvm -c -g -O0 -Xclang -disable-O0-optnone " + output_file_name
    #os.system(command)
