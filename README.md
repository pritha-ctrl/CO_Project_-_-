README

# Co_project
Assembler code using python language.

This program is an assembler for a custom ISA. The CPU has a limited set of instructions,
with each instruction being represented by a 5-bit opcode and 3 bit register/s or a 
7 bit immediate value.

The program reads input from a file named "stdin.txt", which contains a list of instructions to be executed. The program will decode the instructions, check for errors, and print the instructions in binary if no errors are found.The assembler can generate binary code upto 128 lines.


 # Instruction Format

There are six types of instructions that can be executed:
Type A Instructions (add , sub,mul,xor,or,and)
  <Opcode>     <Unused>   <reg 1>    <reg 2>   <reg 3>
   5 bits        2 bits     3 bits     3 bits     3 bits
  
Type B Instructions  (mov,ls,rs)
<Opcode>    <Unused>   <reg 1>    <Immediate>
  5 bits     1 bit     3 bits         7 bits
  
Type C Instructions (mov,div,not,cmp)
<Opcode>    <Unused>   <reg 1>    <reg 2>   
   5 bits     5 bits   3 bits      3 bits    
  
Type D Instructions  (ld,st)
<Opcode> <Unused>   <reg 1>   <Memory Address>
  5 bits    1 bit   3 bits         7 bits
  
Type E Instructions (jmp,jlt,je,jgt)
<Opcode>  <Unused>  <Memory Address>
  5 bits  4 bits       7 bits
  
Type F Instructions (hlt)
<Opcode>   <Unused> 
  5 bits    11 bits
  
  
 # Predefined Values
  
The program has predefined values for the opcode, registers, and flags, as well as default values of all registers i.e. 0.

  
 # Helping Dictionaries/Lists/Elements/Functions made
  
We made several dictionaries and lists in order to make code readable and easy to iterate. We made dictionaries for variables with their values and another one for their memory addresses. We also made a dictionary of all the final instructions for which we need to generate binary code. 
We created a list containing all the output that needs to put in the output file. Also we made a dictionary for labels with their memory addresses as their values.
We made functions to check the errors for different types of instructions and we also made functions to convert decimal to binary and to convert list elements into string elements.
We used a program counter as a variable  to keep track of the line, incase of error.

  
 # Output
  
The program will output the binary instructions that correspond to the input instructions, as well as any errors encountered during the process in the 
stdout.txt file .
  
  
 # Contributors

This program was created by Rohan, Pritha, Swara, and Vikranth as a collaborative project in 2023.
