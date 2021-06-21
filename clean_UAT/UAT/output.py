#!/usr/bin/python
import os
REFERENCE_DICT = {"memory error: out of bound pointer" : "Buffer Overflow Vulnerability"}

def analyse(dir = None):
  ## start with klee-last (the most recent klee file)
  CUR_DIR = os.getcwd()

  ## initialise the variables
  count = 0
  lst = []
  text = ""
  errors = []


  if dir == None: 
    print("You didn't specify any directory... Using default dir")
    dir = CUR_DIR + "/klee-last/"

  # get list of files in directory, as a python list
  lst = os.listdir(dir)
  #print(lst)

  for file in lst:
    if file[-4:] == ".err": # if there is an error in the folder
      with open(dir + "/" + file, "r") as f: # read the file
        errors.append(f.read()) # append error to errors list

  ## handle klee-out-n, where n is a number
  while True:
    dir = CUR_DIR + "/klee-out-" + str(count)

    try:
      lst = os.listdir(dir)
    except Exception as e:
      break

    for file in lst:
      if file[-4:] == ".err": # if there is an error in the folder
        with open(dir + "/" + file, "r") as f: # read the file
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

  for error_list in error_list_raw:
    for line in error_list:
      #print("Printing line: ")
      #print(line)
      # check for everything in one iteration, then load to dict later
      if "File: " in line:
        # extract the filename
        filename = line.split(": ")[1]
        #print("f", line)
      elif "Error: " in line:
        error = line.split(": ")[1]
        #print("e", line)
      elif "Line: " in line:
        line_no = line.split(": ")[1]
        #print("l", line)
    to_insert = [line_no, error]
    # check if file is already a key in the dictionary
    if file not in error_processed:
      error_processed[filename] = [to_insert] # make new list
    elif file in error_processed:
      error_processed[filename].append(to_insert) # append to existing list

    print(error_processed)
    print(type(error_processed))

    # Analyse output
    keys = error_processed.keys()
    errors_count = {}
    for key in keys:
        errors_lst = error_processed[key]
        for errorl in errors_lst:
            print(errorl, type(errorl))
            error = errorl[1]
            lineNo = errorl[0]
            if error not in errors_count.items():
              errors_count[error] = 1
            elif error in errors_count.items():
              errors_count[error] += 1
        print(errors_count)
        for error in errors_count.keys():
          #if True:
          if error in REFERENCE_DICT.keys():
            output = "[!] In file " + key + ", the following errors have occured: \n"
            count = errors_count[error]
            output += error + ": Appears " + str(count) + " times. \n"
            if count <= 1:
              risk = "low"
            elif count <= 3:
              risk = "medium"
            else:
              risk = "high"
            output += "There is a " + risk + " risk that there is a " + str(REFERENCE_DICT.get(error))
          else:
            output = "[!] No dangerous error found in " + key      
        print(output)
analyse()
