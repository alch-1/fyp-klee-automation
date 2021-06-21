#!/usr/bin/python3
import subprocess
import pycparser
import os
import json
import glob
import time

from annotate_JSON_v2 import annotate
from compile_JSON_v2 import clang
from termcolor import colored


CUR_DIR = os.getcwd()

#Import data from JSON file
JSON_PATH = "/home/klee/JSON/config.json"
INFO = colored("[i]", "cyan")
WARN = colored("[!]", "red")

with open(JSON_PATH) as f:
  data = json.load(f)

filepath = "/home/klee/pycparser/utils/fake_libc_include/"

print_output = []
array_list = []

# check existing fake headers
print(INFO + " Checking existing fake headers")
existing_h = []
with open("/home/klee/FYP/KLEENOTATION/ls.out", "r") as f:
  existing_h = f.readlines()
  existing_h = [line.strip() for line in existing_h]

# run gcc command for each file indicated in JSON
for filename, functions in data.items():
   
    ## HANDLE HEADERS ##
    header_files = []

    #get header name
    print(INFO + " Handling file headers of " + filename)
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
            print(INFO + " Missing headers located. Now generating headers for pycparser")
            # create the fake headers
            #print(os.getcwd())          
            with open(os.path.join(filepath, header), "w") as f:
                #print(os.getcwd())
                to_write = '#include "_fake_defines.h"\n#include "_fake_typedefs.h"\n'
                f.write(to_write)

    ## Comment out SCANF & gets ##
    #content = []
    #print("[*] Commenting out scanf and gets occurances in " + filename + " [*]")
    #with open(filename, "r") as f:
        #lines = f.readlines()
        #for line in lines:
            #if "scanf(" in line and "/*" not in line:
                #content.append("/*" + line.rstrip("\n") + "*/\n")
            #elif "gets(" in line and "/*" not in line:
                #content.append("/*" + line.rstrip("\n") + "*/\n")
            #else:
                #content.append(line)

    #with open(filename, "w") as f:
        #for line in content:
            #f.write(line)

    content = []
    comment_lines = input("Are there any scanf occurances in the code to comment out? (Y/N): ")

    if comment_lines.upper() == "Y":
        line_num = input("Please indicate the line number(s) to comment out seperated by commas [e.g. 12,50,123]")
        numbers = line_num.split(",")
        with open(filename, "r") as f:
            lines = f.readlines()
            count = 0
            for line in lines:
                count += 1
                if str(count) in numbers and "/*" not in line:
                    content.append("/*" + line.rstrip("\n") + "*/\n")
                else:
                    content.append(line)

        with open(filename, "w") as f:
            for line in content:
                f.write(line) 
            

    #run gcc command for file indicated in JSON
    #gcc -nostdinc -E -I/home/klee/pycparser/utils/fake_libc_include -I/home/klee/cb-multios/include -I/home/klee/cb-multios/challenges/Palindrome/lib service.c > service_PP.c
    process = filename.split("/")
    print(INFO + " Running gcc command for " + filename)
    command = "gcc -nostdinc -E -I/home/klee/pycparser/utils/fake_libc_include " + filename + " > " + filename[:-2] + "_PP.c"
    os.system (command)
    
    #extract relevant lines
    try:
        print(INFO + " Attempting to run pycparser on " +  process[-1])
        ast = pycparser.parse_file(filename[:-2] + "_PP.c")
        ast_text = ast.show(showcoord=True, buf=open(filename[:-2] + "_testout.txt", "w+"))
        ast_lines = []
        with open(filename[:-2]+ "_testout.txt", "r") as f:
            ast_lines = f.readlines()
        pycparser_passed = True

    except Exception as e:
        print(e) 
        pycparser_passed = False
        function_found = False
        print("pycparser failed to parse " + process[-1])

    #start of line number detection
    for i in functions:
        for function, arguments in i.items():
            #filter by function
            filtered_lines = []
            if pycparser_passed == True:
                for index, line in enumerate(ast_lines):
                    if "FuncDef:" in line:
                        next_line = ast_lines[index + 1]
                        if (function + ",") in next_line:
                            # remove the other lines before this line
                            function_found = True
                            filtered_lines = ast_lines[index + 1:]
                            break # efficiency
                        else:
                            print("Trying to locate " + function + " in "+ filename + "...")
                            function_found = False
                            

            #for each variable if unable to locate, user specifies line number
            for argument in arguments:
                is_array = False
                if function_found == False or pycparser_passed == False: 
                    line_number = input("Please specify the line number in the code for " + argument + " in " + function + ": ")
                    is_array = input("Is " + argument + " an array? (True/False): ")
                    if is_array == "True":
                        is_array = True
                    else:
                        is_array = False
                    print_output.append([filename, function, argument, is_array, line_number])

                else:
                    found = False
                   #filtered = [line for line in ast_lines if argument in line]
                    search_decl = "Decl: " + argument + ","
                    decl = []
                    #check if argument is an array
                    for index, line in enumerate(filtered_lines):
                        if search_decl in line:
                            found = True
                            decl.append(line)
                            #print(argument + " found at index " + str(index))
                            next_line = filtered_lines[index + 1]
                            #print("Checking next line after " + argument + " declaration... (index: " + str(index) + ")")
                            #print(next_line)
                            if "ArrayDecl" in next_line:
                                array_list.append(argument)
                
                    if found == False: 
                        print("Unable to locate " + argument + " in " + function + " due to unconventional declaration")
                        line_number = input("Please specify the line number in the code for " + argument + ": ") 
                        is_array = input("Is " + argument + " an array? (True/False): ")
                        if is_array == "True":
                            is_array = True
                        else:
                            is_array = False    
                    else:
                        #get line number of the argument
                        line = decl[0]
                        line_number = line.split(":")[2]
                        confirmation = input(argument + " is found in line " + str(line_number) + " of " + filename + " confirm [Y/N]?: ")

                        if confirmation.upper() == "N":
                            line_number = input("Please specify the line number in the code for " + argument + " instead: ")
                            if is_array == "True":
                                is_array = True
                            else:
                                is_array = False
         
         
                    if argument in array_list and found == True:
                        is_array = True


                    print_output.append([filename, function, argument, is_array, line_number])

print(INFO + " Parser Module DONE parsing the target code(s), now calling Annotate Module")
print(print_output)

shifted = 1
unique_files = []
for item in print_output:
    if item[0] not in unique_files:
        unique_files.append(item[0])
        shifted = 1
    print(INFO + " Now annotating " + item[2] + " in " + item[0] + " [*]")
    annotate(item[0], item[2], item[3], shifted + int(item[4]))
    shifted += 1

#Extract directory for each program
unique_program = []

for item in unique_files:
    temp_list = item.split("/")
    program_directory = ""

    for i in temp_list[:-1]:
        program_directory += i + "/"

    if program_directory not in unique_program:
        unique_program.append(program_directory)

print("the programs selected are:")
print(unique_program)

#CLEANUP intermediary generated files
print(INFO + " Commencing intermediary file clean up before compiling target code(s)")
for program in unique_program:
    file_location = program 
    os.chdir(file_location)
    #REMOVE _PP.c
    for file in glob.glob("*_PP.c"):
       subprocess.Popen(["rm", file], cwd = file_location)
    
    #REMOVE AST txt file
    for file in glob.glob("*_testout.txt"):
        subprocess.Popen(["rm", file], cwd = file_location)

    #REMOVE OLD .c file
    for file in glob.glob("*.c"):
        if "annotated" in file:
            non_annotated_filename = str(file[:-12]) + ".c"
            subprocess.Popen(["rm", non_annotated_filename], cwd = file_location)

    #RENAME _annotated.c back to original .c file name
    for file in glob.glob("*.c"):
        if "annotated" in file:
            subprocess.Popen(["mv", file, file[:-12] + ".c"], cwd = file_location)

time.sleep(3)
#Finally, call compiler module:
#print(type(unique_program))
print(INFO + " Annotate Module DONE, calling Compile Module")
print(unique_program)
clang(unique_program)

