#!/usr/bin/python3
import subprocess
import pycparser
import os
import json
from annotate_JSON import annotate
from clang import clang

# run the gcc command on c file
# gcc -nostdinc -E -I/home/rg/pycparser-master/utils/fake_libc_include test.c > testPP.c

#Import data from JSON file
with open('/home/klee/FYP/FYP/UAT/config_template.json') as f:
  data = json.load(f)


filepath = "/home/klee/pycparser/utils/fake_libc_include/"


print_output = []
array_list = []

# check existing fake headers
existing_h = []
with open("ls.out", "r") as f:
  existing_h = f.readlines()
  existing_h = [line.strip() for line in existing_h]

# run gcc command for each file indicated in JSON
for filename, functions in data.items():
   
    ## HANDLE HEADERS ##
    header_files = []

    #get header name
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "#include" in line:
                #print("#include found at line:" + line)
                if "<" in line:
                    header = line.split("<")[1].strip()[:-1]
                    header_files.append(header)
                elif '"' in line:
                    header = line.split('"')[1].strip()
                    header_files.append(header)
                elif "'" in line:
                    header = line.split("'")[1].strip()
                    header_files.append(header)
    
    for header in header_files:
        if header not in existing_h:
        # create the fake headers
            #fpath = filepath + header
            #print(os.getcwd())            
            with open(os.path.join(filepath, header), "w") as f:
                #print(os.getcwd())
                to_write = '#include "_fake_defines.h"\n#include "_fake_typedefs.h"\n'
                f.write(to_write)

    ## Comment out SCANF ##
    content = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "scanf" in line and "/*" not in line:
                content.append("/*" + line + "*/")
            else:
                content.append(line)
            
    with open(filename, "w") as f:
        for line in content:
            f.write(line) 
            


    #run gcc command for file indicated in JSON
    command = "gcc -nostdinc -E -I/home/klee/pycparser/utils/fake_libc_include " + filename + " > " + filename[:-2] + "_PP.c"
    os.system (command)
    
    #extract relevant lines
    ast = pycparser.parse_file(filename[:-2] + "_PP.c")
    ast_text = ast.show(showcoord=True, buf=open(filename[:-2] + "_testout.txt", "w+"))
    ast_lines = []
    with open(filename[:-2]+ "_testout.txt", "r") as f:
        ast_lines = f.readlines()


    #start of line number detection
    for i in functions:
        for function, arguments in i.items():
            #filter by function
            #if function == "main":
            filtered_lines = []
            for index, line in enumerate(ast_lines):
                if "FuncDef:" in line:
                    next_line = ast_lines[index + 1]
                    if (function + ",") in next_line:
                        # remove the other lines before this line
                        filtered_lines = ast_lines[index + 1:]
                        break # efficiency
            
            for argument in arguments:
               #filtered = [line for line in ast_lines if argument in line]
                search_decl = "Decl: " + argument + ","
                decl = []
                #check if argument is an array
                for index, line in enumerate(filtered_lines):
                    if search_decl in line:
                        decl.append(line)
                        #print(argument + " found at index " + str(index))
                        next_line = filtered_lines[index + 1]
                        #print("Checking next line after " + argument + " declaration... (index: " + str(index) + ")")
                        #print(next_line)
                        if "ArrayDecl" in next_line:
                            array_list.append(argument)


                #get line number of the argument
                line = decl[0]
                line_number = line.split(":")[2]

         
                is_array = False
                if argument in array_list:
                    is_array = True

                print_output.append([filename, function, argument, is_array ,line_number])

print(print_output)

## Annotate required C files and produce .bc from C files
shifted = 1
unique_files = []
for item in print_output:
    if item[0] not in unique_files:
        unique_files.append(item[0])
        shifted = 1
    annotate(item[0], item[2], item[3], shifted + int(item[4]))
    shifted += 1

## Produce .bc from C files
#unique_files = []
#for item in print_output:
    #if item[0] not in unique_files:
        #unique_files.append(item[0])

for file in unique_files:
    print(clang(file[:-2]))
#    klee_command = "clang -I /home/klee/klee_src/include  -emit-llvm -c -O0 -Xclang -disable-O0-optnone " + file[:-2] + "_annotated.c"
#    os.system(klee_command)


    

