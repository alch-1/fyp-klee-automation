#!/usr/bin/python3
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import json
import os
import sys
sys.path.insert(0, "/home/klee/FYP/parser")

#setting the prep files for config_template.json
file_tests = {}
# file_tests_list = []
# test_dict = {}
# var_list = []

klee_flags = {}
class Subwindow:

    def __init__(self):
        self.var_list = []
        self.file_tests_list = []
        self.test_dict = {}
        # self.file_tests = {}
        # global var_list
        # global file_tests_list
        # global test_dict
        global file_tests
        global klee_flags
        self.window = tk.Toplevel()
        # self.window.geometry("300x300+1000+200")
        # self.window.geometry("300x300")
        self.window.title("Add test")
        self.window.wm_attributes("-topmost", 1)

        tk.Label(self.window, text="Adding a new test... Close window to cancel.").pack(anchor=tk.W,padx=6, pady=4)

        #Spacing
        self.lbl = tk.Label(self.window, text = "")
        self.lbl.pack()
        
         #---------- SEPARATOR----------------------
        self.separator = ttk.Separator(self.window, orient='horizontal')
        self.separator.pack(fill='x')

        #---------------------FILE PATH--------------------------#
        tk.Label(self.window, text="Add file path").pack(anchor=tk.CENTER)
        # self.label_count = 0
        self.open()
        self.file_path = tk.Label(self.window, text='No file path selected yet')
        self.file_path.pack()
        
        #Spacing
        self.lbl = tk.Label(self.window, text = "")
        self.lbl.pack()

         #---------- SEPARATOR----------------------
        self.separator = ttk.Separator(self.window, orient='horizontal')
        self.separator.pack(fill='x')
        #----------------------FUNCTION-----------------------------#
        
        #for function
        tk.Label(self.window, text="Specify function to be referenced").pack(anchor=tk.CENTER)

        self.inputfunc = tk.Entry(self.window)
        self.inputfunc.pack()
        self.func = tk.Label(self.window, text = 'No function selected yet')
        self.func.pack()
        
        #Button Creation for function
        self.cfmfuncButton = tk.Button(self.window, text = "Confirm function", command = self.printFunc)
        self.cfmfuncButton.pack()

        #Spacing
        self.lbl = tk.Label(self.window, text = "")
        self.lbl.pack()
         #---------- SEPARATOR----------------------
        self.separator = ttk.Separator(self.window, orient='horizontal')
        self.separator.pack(fill='x')

        


         #for variable
        tk.Label(self.window, text="Add variable name to make symbolic").pack(anchor=tk.CENTER)
        tk.Label(self.window, text="Separate multiple variables with a comma (,)").pack(anchor=tk.CENTER)

        self.inputvar = tk.Entry(self.window)
        self.inputvar.pack()
        self.sym_var = tk.Label(self.window, text = 'No variable selected yet')
        self.sym_var.pack()
        
        #Button Creation for variable
        self.cfmButton = tk.Button(self.window, text = "Confirm variable", command = self.printVar)
        self.cfmButton.pack()

        #Spacing
        self.lbl = tk.Label(self.window, text = "")
        self.lbl.pack()

         #---------- SEPARATOR----------------------
        self.separator = ttk.Separator(self.window, orient='horizontal')
        self.separator.pack(fill='x')


        #---------------KLEE command-----------------------------#
        
        #for KLEE command
        tk.Label(self.window, text="Set KLEE Command flags for this program").pack(anchor=tk.CENTER)
        tk.Label(self.window, text="Separate your flags by space, e.g. --flag1 --flag2").pack(anchor=tk.CENTER, padx=6, pady=4)
        #tk.Label (self.window, text="").pack(anchor=tk.CENTER)
        self.v = tk.StringVar(self.window, value = "--external-calls=all")
        self.inputkleecomm = tk.Entry(self.window, textvariable = self.v)
        self.inputkleecomm.pack()
        
        self.sym_kleecomm = tk.Label(self.window, text = 'Default flag used: "--external-calls=all" ', wraplength=300, justify="center")
        self.sym_kleecomm.pack(padx=6, pady=4)
        
        
        #Button Creation for use existing flags
        self.exflagButton = tk.Button(self.window, text = "Click to use existing", command = self.useExisting, state=tk.DISABLED)
        self.exflagButton.pack()
        #Button Creation for variable
        self.cfmButton = tk.Button(self.window, text = "Confirm KLEE Flags", command = self.printKLEECommand)
        self.cfmButton.pack()

        #Spacing
        self.lbl = tk.Label(self.window, text = "")
        self.lbl.pack()

         #---------- SEPARATOR----------------------
        self.separator = ttk.Separator(self.window, orient='horizontal')
        self.separator.pack(fill='x')


        #---------------------------PRINT JSON TO CONFIRM-------------------

        #Button Creation for json
        self.cfmjsonButton = tk.Button(self.window, text = "Confirm Add Test", command = self.prep_json)
        self.cfmjsonButton.pack()

        #Spacing
        self.lbl = tk.Label(self.window, text = "")
        self.lbl.pack()

        self.window.mainloop()

    #-----------------FUNCTIONS--------------------------------#

    def printVar(self):
        # inp = self.inputvar.get(1.0, "end-1c")
        inp = self.inputvar.get()
        if inp.strip() != "":
            self.sym_var.config(text = "Making variable(s): "+inp+ " symbolic")
   
    def printKLEECommand(self):
        # inp = self.inputvar.get(1.0, "end-1c")
        inp = self.inputkleecomm.get()
        if inp.strip() != "":
            self.sym_kleecomm.config(text = "KLEE flags: "+inp)

    
    
    def printFunc(self):
        # inp = self.inputfunc.get(1.0, "end-1c")
        inp = self.inputfunc.get()
        if inp.strip() != "":
            self.func.config(text = "Entering function: "+inp)

    def add_file(self):
        filename = tk.filedialog.askopenfilename()
        if filename:
            # print('Selected:', filename)
            self.file_path['text']= filename
            self.checkExisting()
            return filename
        else:
            self.window.destroy()
    def open(self):
        buttons = tk.Frame(self.window)
        tk.Button(self.window, text="Select File", command=self.add_file).pack(in_=buttons, side="left")
        buttons.pack()

    def checkExisting(self):
        if self.file_path['text']:
            filepath = self.file_path['text']
            if '/src' in filepath:
                index_src = filepath.find('/src')
                self.trimmed_path = filepath[:index_src]
            else:
                index_parent = filepath.rfind('/')
                self.trimmed_path = filepath[:index_parent]
        if klee_flags.get(self.trimmed_path)!=None:
            #print(klee_flags.get(trimmed_path))
            self.exflagButton['state']=tk.NORMAL
        else:
            self.exflagButton['state']=tk.DISABLED
    def useExisting(self):
            existing_flags_list = klee_flags[self.trimmed_path][0]['klee_flags']
            existing = ""
            for flag in existing_flags_list:
                existing += flag + " "
            existing = existing.strip()
            #print(existing)
            self.v.set(existing)
            #self.inputkleecomm.delete(0,END)
            #self.inputkleecomm.insert(0,existing)
         #else:
             #send a message saying not set yet
               

    def prep_json(self):
        function = self.inputfunc.get()
        variable = self.inputvar.get()
        file_path = self.file_path['text']
        # print("function: "+ function)
        # print("variable: "+ variable)
        # print("file_path: "+ file_path)
        key = file_path
        # self.var_list.append(variable)
        # self.test_dict[function]= self.var_list
        # # print(self.test_dict)
        # self.file_tests_list.append(self.test_dict)
        # global file_tests

        #---------------------------
        if "," in variable:
            variables = variable.split(",")
            for eachVar in variables:
                self.var_list.append(eachVar)
        elif "," not in variable:
            self.var_list.append(variable)

        self.test_dict[function] = self.var_list
        self.file_tests_list.append(self.test_dict)
        # file_tests[key].append(self.file_tests_list) #can't append to non list/init if does not exist
        
        if file_tests.get(key)==None:
            file_tests[key] = self.file_tests_list
        else:
            for file_test in file_tests[key]:
                # print('file test', file_test)
                if file_test.get(function) != None: # function exists so we append
                    print("appending", variable, "to", file_test[function])
                    file_test[function].append(variable)
                    break
            else:
                print("appending", self.test_dict, "to", file_tests[key])
                file_tests[key].append(self.test_dict)
            
        #-----------making klee_command.json----------------
        #for darpa only
        if '/src' in file_path:
            index_src = file_path.find('/src')
            trimmed_path = file_path[:index_src]
            #print(trimmed_path)
            flags = self.inputkleecomm.get()
        
        #consider non darpa
        else:
            index_parent = file_path.rfind('/')
            trimmed_path = file_path[:index_parent]
            flags = self.inputkleecomm.get()

        if flags != None:
                klee_flags[trimmed_path] =[{'klee_flags':[flags] }]
        print("Printing from config.json...")
        print(file_tests)
        print("Printing from klee_command.json...")
        print(klee_flags)
       # if klee_flags.get(trimmed_path)!=None:
            #the existing flags should show on GUI
        #    existing_flags_list = klee_flags[trimmed_path][0]['klee_flags']
        #    existing = ""
        #    for flag in existing_flags_list:
        #        existing += flag + " "
        #        #(that variable).append (flag + " ")
        #        self.inputkleecomm.config(textvariable=existing.strip())
        #-----------end of making klee_command.json----------------
        

        self.done()
    
    def done(self):
        #print("From Subwindow: ")
        #print(file_tests)
        save_path = '/home/klee/JSON'
        json_file = 'config.json'
        complete_json_file = os.path.join(save_path, json_file)
        config = open(complete_json_file, 'w')
        json.dump(file_tests, config)
        config.close()
        klee_file = 'klee_command.json'
        complete_klee_file = os.path.join(save_path, klee_file)
        klee = open(complete_klee_file, 'w')
        json.dump(klee_flags, klee)
        klee.close()
        self.window.destroy()
   


class Window:

    def __init__(self):
        # self.var_list = []
        # # self.file_tests = []
        # global var_list
        # global file_tests_list
        # global test_dict
        global file_tests

        self.window = tk.Tk()
        self.window.geometry("400x400")
        self.window.title("KLEENOTATION() GUI")
        tk.Label(self.window, text="\n\nWelcome to KLEENOTATION(). \n\nPlease click the 'Add New Test' button to add new tests. If you do not want to overwrite the existing config.json, please click Run KLEENOTATION() or Run KLEENOTATION() for DARPA instead.\n\nPlease ensure that a JSON directory has been created outside the KLEENOTATION folder. \n\nThis GUI will create config.json and klee_command.json in the JSON directory. A copy of the sample files can be found at KLEENOTATION/templates.", wraplength=300, justify="left").pack()
        
        tk.Label(self.window, text="").pack() #add a breakline

        #self.config_template = tk.Label(self.window, text = "Number of tests" + str(len(file_tests)))
        #self.config_template.pack()

        self.initialize()
        self.window.mainloop()

    def initialize(self):
        # title
        refresh = tk.Frame(self.window)
        tk.Button(self.window, text="Refresh JSON",command=self.refresh).pack(in_=refresh)
        buttons = tk.Frame(self.window)
        runbuttons = tk.Frame(self.window)
        tk.Button(self.window, text="Add New Test", command=self.start).pack(in_=buttons, side="left")
        tk.Button(self.window, text="Exit", width=5, command=self.close).pack(in_=buttons, side="left")
        # buttons.place(relx=0.97, rely=0.95, anchor=tk.SE)
        refresh.pack()
        tk.Label(self.window, text="").pack()
        tk.Button(self.window, text="Run KLEENOTATION()", command=self.run).pack(in_=runbuttons)
        tk.Button(self.window, text="Run KLEENOTATION() for DARPA", command=self.rundarpa).pack(in_=runbuttons)
        buttons.pack()
        tk.Label(self.window, text="").pack()
        runbuttons.pack()

    def run(self):
        import parser_JSON_v2

    def rundarpa(self):
        import parser_DARPA_v2

    def close(self):
        self.window.destroy()
        quit()
    def refresh(self):
        save_path = '/home/klee/JSON'
        json_file = 'config.json'
        complete_json_file = os.path.join(save_path, json_file)
        config = open(complete_json_file, 'w')
        json.dump({}, config)
        config.close()
        klee_file = 'klee_command.json'
        complete_klee_file = os.path.join(save_path, klee_file)
        klee = open(complete_klee_file, 'w')
        json.dump({}, klee)
        klee.close()

    def start(self):
        Subwindow()
        # file_tests_list = []
        # test_dict = {}
        # var_list = []
        # self.config_template.config(text = len(file_tests))


Window()

