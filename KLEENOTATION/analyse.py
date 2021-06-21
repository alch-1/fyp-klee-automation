#!/usr/bin/python3
import os
from termcolor import colored

def analyse():
  REFERENCE_DICT = {
    "memory error: out of bound pointer" : [
      "Buffer Overflow Vulnerability", 
      "Significant", 
      colored("[i]", "cyan") +  " Based on DARPA repository code analysis, out of 134 memory errors, there were 43 Buffer Overflows (Occurence rate: 32.09%)",
      "Strategy: Environment Hardening (CWE-120): \n \n When the set of acceptable objects, such as filenames or URLs, is limited or known, create a mapping from a set of fixed input values (such as numeric IDs) to the actual filenames or URLs, and reject all other inputs. \n \n Strategy: Compilation or Build Hardening (CWE-121): \n \n Run or compile the software using features or extensions that automatically provide a protection mechanism that mitigates or eliminates buffer overflows. For example, certain compilers and extensions provide automatic buffer overflow detection mechanisms that are built into the compiled code. Examples include the Microsoft Visual Studio /GS flag, Fedora/Red Hat FORTIFY_SOURCE GCC flag, and StackGuard."
    ],
  }
  EXCLAM = colored("[!]", "red")
  INFO = colored("[i]", "cyan")
  ## start with klee-last (the most recent klee file)
  CUR_DIR = os.getcwd()

  ## initialise the variables
  count = 0
  lst = []
  text = ""
  errors = []

  d = input(INFO + " Please enter directory where your klee-last folder is in").strip()
  if d == '':
    print("You didn't specify any directory... Using default dir")
    dir = CUR_DIR + "/klee-last/"
  else:
    dir = d + "/klee-last/"

  # get list of files in directory, as a python list
  lst = os.listdir(dir)
  #print(lst)

  for file in lst:
    if file[-4:] == ".err": # if there is an error in the folder
      with open(dir + "/" + file, "r") as f: # read the file
        errors.append(f.read()) # append error to errors list

  ## handle klee-out-n, where n is a number
  while True:
    dirl = dir[:-11] + "/klee-out-" + str(count)
    # print(dirl)

    try:
      lst = os.listdir(dirl)
    except Exception as e:
      break

    for file in lst:
      if file[-4:] == ".err": # if there is an error in the folder
        with open(dirl + "/" + file, "r") as f: # read the file
          errors.append(f.read()) # append error to errors list

    count += 1

  #print(errors)

  ## parse errors
  error_list_raw = []
  for error in errors:
    error_list_raw.append(error.split("\n"))

  #print(error_list_raw)

  ## loop through error list to get details
  error_processed = {}
  printed = []
  for error_list in error_list_raw:
    for line in error_list:
      #print("Printing line: ")
      #print(line)
      # check for everything in one iteration, then load to dict later
      if "File: " in line:
        # extract the filename
        filename = line.split(": ", 1)[1].strip()
        #print("f", line)
      elif "Error: " in line:
        error = line.split(": ", 1)[1].strip()
        #print("e", line)
      elif "Line: " in line:
        line_no = line.split(": ", 1)[1].strip()
        #print("l", line)
      if 'filename' in locals() and 'error' in locals() and 'line_no' in locals():
        toprint = "In {}, {} has occured on line {}. Please refer to later analysis to determine if the error is dangerous.".format(filename, error, str(line_no))
        if toprint not in printed: 
          print(EXCLAM + " " + toprint)
          printed.append(toprint)
    to_insert = [line_no, error]
    # check if file is already a key in the dictionary
    if file not in error_processed:
      error_processed[filename] = [to_insert] # make new list
    elif file in error_processed:
      error_processed[filename].append(to_insert) # append to existing list

    # print(error_processed)
    # print(type(error_processed))

  # Analyse output
  print("======== Analysis ========")
  keys = error_processed.keys()
  errors_count = {}
  for key in keys:
      errors_lst = error_processed[key]
      for errorl in errors_lst:
          # print(errorl, type(errorl))
          error = errorl[1]
          lineNo = errorl[0]
          if error not in errors_count.items():
            errors_count[error] = 1
          elif error in errors_count.items():
            errors_count[error] += 1
      # print(errors_count)
      for error in errors_count.keys():
        # print("error:", error)
        #if True:
        if error in REFERENCE_DICT.keys():
          output = EXCLAM + " In file " + key + ", the following errors have occured: \n"
          count = errors_count[error]
          output += error + ": Appears " + str(count) + " times. \n"
          if count <= 1:
            risk = "low"
          elif count <= 3:
            risk = "medium"
          else:
            risk = "high"
          output += EXCLAM + " There is a " + risk + " probability that there is a " + str(REFERENCE_DICT.get(error)[0]) + ". Impact: " + str(REFERENCE_DICT.get(error)[1]) + "\n" 
          output += str(REFERENCE_DICT.get(error)[2]) + "\n"
          output += INFO + " Remediation: \n \n" + str(REFERENCE_DICT.get(error)[3])
        else:
          output = INFO + " No dangerous error found in " + key      
      print(output)

  # ui
  choice = input(INFO + " Would you like to run kcachegrind on the latest klee output in klee-last? (Y/n)")
  if choice == 'y' or choice == "Y":
    command = "kcachegrind " + dir + "/run.istats"
    os.system(command)


analyse()
