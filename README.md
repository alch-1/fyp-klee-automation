# Final Year Cybersecurity Project
Final year Cybersecurity project for SMU's Information Systems course

# Project Outline
We are to build a python tool that automates the instrumenting of a batch of programs provided by DARPA. Our tool 
then makes use of KLEE to perform symbolic execution on a batch of programs to generate a set of test cases which allows 
the user to find bugs in these programs.  
- KLEE is a dynamic symbolic execution engine built on top of the LLVM compiler infrastructure that can find bugs 
during execution.  
Additionally, we will perform analysis on the output of KLEE.  
- We will explore if the bugs identified can potentially be used as vulnerabilities, and if yes, what kind of vulnerabilities, 
and its severity.  
- Analyse the accuracy of KLEE’s ability to identify bugs from DARPA repository. 

# Tools used
1. KLEE: Primary software our tool will be built for. 
2. Docker: Part of our development and testing environment. 
3. GitHub: Version control tool. 
4. Python: The programming language our team will be using to build the tool. 
5. Pycparser: Python library for C program parsing.
