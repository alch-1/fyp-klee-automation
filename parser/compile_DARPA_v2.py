import os
import subprocess
import json
import glob 
import time

CUR_DIR = os.getcwd()

def clang(unique_DARPA_programs):
    
    #load klee_command json
    JSON_PATH = "/home/klee/JSON/klee_command.json"

    with open(JSON_PATH) as f:
        data = json.load(f)

    #run build.sh to generate binary files:
    print("[*] Compiling DARPA codes... [*]")
    subprocess.Popen(["./build.sh"], cwd = "/home/klee/cb-multios")
    time.sleep(10*len(unique_DARPA_programs))

    #generate .bc files for each DARPA program:
    print("[*] Extracting .bc files for each DARPA program ... [*]")
    subprocess.Popen(["./extract-all-bc-files.sh"], cwd = "/home/klee/cb-multios")
    time.sleep(5)

    for program in unique_DARPA_programs:
        temp_list = program.split("/")
        print("[!] Running KLEE on:", temp_list[5], "...")
        

        #check for klee_flags specified in klee_command.json
        commands = ""
        for filename, flags in data.items():
            for i in flags:
                for name, flag in i.items():
                    if name == "klee_flags" and filename + "/" == program:
                        for item in flag:
                            commands += item
                        print("JSON ok")
                    else:
                        commands = temp_list[5] + ".bc"
        
        process = commands.split(" ")
        full_command = "klee"
        for item in process:
            full_command += " " + item
        #run KLEE on program
        program_path = "/home/klee/cb-multios/build64/challenges/" +  temp_list[5]
        print(program_path)
        print(full_command)
        subprocess.Popen(full_command, cwd = program_path, shell=True)

    return
