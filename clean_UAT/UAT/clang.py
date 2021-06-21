import os
import subprocess

def clang(FILE=None):
  if (FILE == None):
    raise "Error: file not specified"

#  command = "clang -I /home/klee/klee_src/include ./ -emit-llvm -c -g -O0 -Xclang -disable-O0-optnone"
  command = ["clang", "-I /home/klee/klee_src/include", "-emit-llvm", "-c", "-g", "-O0", "-Xclang", "-disable-O0-optnone", "-I ./"]

  extra_dir = input("Please enter the directory containing the required external libraries. If there are no external libraries, please type 'none'")
  extra_dir = extra_dir.strip()
  if extra_dir != 'none':
    command.append(" -I " + extra_dir)

#  filename = input("Please enter filename: ")
  command.append(FILE + "_annotated.c")

  clang_raw = subprocess.run(command, stdout=subprocess.PIPE)
  clang_parsed = clang_raw.stdout.decode('utf-8').strip()
  return clang_parsed
