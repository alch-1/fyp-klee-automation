import os
import subprocess
import json
import glob 
import time

CUR_DIR = os.getcwd()

def clang(unique_programs):
    #print(unique_programs)
    #load klee_command json
    JSON_PATH = "/home/klee/JSON/klee_command.json"

    with open(JSON_PATH) as f:
        data = json.load(f)

    #compile annotated c files:
    for program in unique_programs:
        os.chdir(program)    
        for file in glob.glob("*.c"):
            print(file)
            print("[*] Compiling C programs in " + program + " [*]")
            subprocess.Popen(["clang", "-I /home/klee/klee_src/include", "-emit-llvm", "-c", "-g", "-O0", "-Xclang", "-disable-O0-optnone", "-I ./", file], cwd = program)
    
            time.sleep(5)

            #run KLEE on .bc file
            print("[!] Running KLEE on:", file[:-2] + ".bc", "...")
        

            #check for klee_flags specified in klee_command.json
            commands = ""
            for filename, flags in data.items():
                for i in flags:
                    for name, flag in i.items():
                        if name == "klee_flags" and filename + "/" == program:
                            for item in flag:
                                commands += item
                            print("JSON ok")
                            check = file[:-2] + ".bc"
                            if check not in commands
                                commands += " " + file[:-2] + ".bc"
                        else:
                            commands = file[:-2] + ".bc"
        
            process = commands.split(" ")
            full_command = "klee"
            for item in process:
                full_command += " " + item
        
            #run KLEE on program
            program_path = program
            print(program_path)
            print(full_command)
            subprocess.Popen(full_command, cwd = program_path, shell=True)
            
    return
