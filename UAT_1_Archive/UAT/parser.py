#!/usr/bin/python3
import subprocess
import pycparser
import os

# run the gcc command on c file
# gcc -nostdinc -E -I/home/rg/pycparser-master/utils/fake_libc_include test.c > testPP.c

filename = input("Enter filename:").strip()
#outputname = input("Enter outputname")
variable = input("Enter variable name:").strip()
function = input("Enter function name:").strip()


# run gcc command
command = "gcc -nostdinc -E -I/home/klee/pycparser/utils/fake_libc_include " + filename + " > temp.c"
os.system(command)

#subprocess_raw = subprocess.run(["gcc", "-nostdinc", "-I/home/klee/pycparser/utils/fake_libc_include", filename, ">", "temp.c"], stdout=subprocess.PIPE)
#subprocess_output = subprocess_raw.stdout.decode('utf-8').strip()
#print(subprocess_output)

# extract relevant lines
ast = pycparser.parse_file("temp.c")

#ast_out = ''

# write ast to testout.txt
ast_text = ast.show(showcoord=True, buf=open("testout.txt", "w+"))

#print(ast_out)
#print(ast_text)

#ast_split = ast_text.split("\n")
#lines = [line for line in ast_split if variable in line]
#print(lines)
#variable = input("Enter variable name")

ast_lines = []
with open("testout.txt", "r") as f:
  ast_lines = f.readlines()


## HANDLE HEADERS ##
header_files = []

# get header name
with open(filename, "r") as f:
  lines = f.readlines()
  for line in lines:
    if "#include" in line:
      print("#include found at line:" + line)
      if "<" in line:
        header = line.split("<")[1].strip()[:-1]
        header_files.append(header)
      elif '"' in line:
        header = line.split('"')[1].strip()
        header_files.append(header)

print("Header files in file:")
print(header_files)

# check existing fake headers
existing_h = []
with open("ls.out", "r") as f:
  existing_h = f.readlines()
  existing_h = [line.strip() for line in existing_h]

#print(existing_h)

filepath = "/home/klee/pycparser/utils/fake_libc_include/"

# add if not in list
for header in header_files:
  if header not in existing_h:
    # create the fake header
    fpath = filepath + header
    with open(fpath, "w+") as f:
      to_write = '#include "_fake_defines.h"\n#include "_fake_typedefs.h"'
      f.write(to_write)

## SEARCH FOR VARIABLE LINE NUMBER IN AST
#filtered = [line for line in ast_lines if variable in line]

search_decl = "Decl: " + variable + ","
#decl = [line for line in filtered if search_decl in line]
decl = [] # put all lines with the variable that the user wants in here
arrayVars = [] # put all vars that are arrays in here

after = []
# find all lines after funcdef
for index, line in enumerate(ast_lines):
  if "FuncDef:" in line:
    next_line = ast_lines[index + 1]
    if (function + ",") in next_line:
      # remove everything before this line
      after = ast_lines[index + 1:]
      break # efficiency

for index, line in enumerate(after):
  if search_decl in line:
    decl.append(line) # add the line to the array
    print(variable + " found at index " + str(index))
    # handle arrays
    # find next line
    next_line = after[index + 1]
    print("Checking next line after " + variable + " declaration... (index: " + str(index) + ")")
    print(next_line)
    if "ArrayDecl" in next_line:
      arrayVars.append(variable)

line = decl[0]
line_number = line.split(":")[2]

#print("Filtered:")
#print(filtered)

#print("Decl:")
#print(decl)

print("Line number:")
print(line_number)

print("Array variables:")
print(arrayVars)
