# CO_PROJECT_2023 - Rohan, Pritha, Swara, Vikranth

# opcode (predefined)
opcode={"add": "00000","sub": "00001","mov": "00010","mov": "00011","ld": "00100","st": "00101","mul": "00110","div": "00111","rs": "01000","ls": "01001","xor": "01010","or": "01011","and": "01100","not": "01101","cmp": "01110","jmp": "01111","jlt": "11100","jgt": "11101","je": "11111","hlt": "11010"}

# registers (predefined) and default values = 0
register={"R0": "000","R1": "001","R2": "010","R3": "011","R4": "100","R5": "101","R6": "110","FLAGS": "111"}
register_value={"R0":0,"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0,"FLAGS":"0000000000000000"}

# flags (predefined)
flags={"V": "0000000000001000","L": "0000000000000100","G": "0000000000000010","E": "0000000000000001"}

# list of variable names
variable={} # variable should consist of variable names as keys and values as memory addresses
variable_values={}

# list of labels names
labels={} # labels should consist of labels as keys and value as thier memory addresses

# input from file
with open("input.txt") as fin:
    l=[]
    for i in fin:
        if i.split()!=[]:
            l.append(i.split())

# final output
output=[]

# decimal to binary
def dec_to_bin(n):
    if n == 0:
        return '0'
    val = ''
    while n > 0:
        val = str(n%2)+val
        n//=2
    val = (7-len(val))*"0"+val
    return val

# final instructions to be executed
instructions_with_pc={}

# things to check, intruction name, instruction size, register names, (operation on registers) result values , immediate value range, flags at place of register
# TYPE A FUNCTIONS
def check_error_type_A(instruction):
    return 1

def print_type_A(instruction):
    output.append("Type A")


# TYPE B FUNCTIONS
def check_error_type_B(instruction):
    imm_val=instruction[2][1:]
    if len(instruction)!=3:
        print("General Syntax Error",end="")
        return 0
    elif instruction[1] not in register:
        print("Typos in instruction name or register name",end="")
        return 0
    elif instruction[1]=="FLAGS" or instruction[2]=="FLAGS":
        print("Illegal use of FLAGS register",end="")
        return 0
    elif imm_val<0 or imm_val>127:
        print("Illegal Immediate values (more than 7 bits)")
    else:
        return 1
    
def print_type_B(instruction):
   imm_val=instruction[2][1:]
   imm_val_final=dec_to_bin(int(imm_val))
   output.append(opcode[instruction[0]]+"0"*1+ register[instruction[1]]+imm_val_final)


# TYPE C FUNCTIONS
def check_error_type_C(instruction):
    return 1

def print_type_C(instruction):
    output.append("Type C")


# TYPE D FUNCTIONS
def check_error_type_D(instruction):
    return 1

def print_type_D(instruction):
    output.append("Type D")



# TYPE E FUNCTIONS
def check_error_type_E(instruction):
    return 1

def print_type_E(instruction):
    output.append("Type E")



#TYPE F FUNCTIONS
def check_error_type_F(instruction):
  if len(instruction)!=1:
      print("General Syntax Error",end="")
      return 0
  else:
      return 1


def print_type_F(instruction):
    output.append(opcode[instruction[0]] + "0"*11 )
    

# error flag and error line
error=0
error_line=-1

# hlt code count (only 1 allowed in code)
htl_count=0

# program counter
program_counter=0

# checking errors in input and making final instructions list and creating variables
for j in range(0,len(l)):
    i = l[j]

    # Invalid Codes
    if i[0] not in opcode.keys() and i[0] != "var" and ":" not in i[0]:
        print("General Syntax Error, line "+str(program_counter+1))
        error=1
        error_line=program_counter+1
        break

    # hlt not used at last
    if i[-1]=="hlt" and j!=len(l)-1:
        print("hlt not being used as the last instruction, line "+str(program_counter+1))
        error=1
        error_line=program_counter+1
        break

    # missing hlt instruction-1
    if i[-1]=="hlt" and j==len(l)-1:
        htl_count+=1
        error_line=program_counter+1

    # Variable defining not at beginning
    if i[0]=="var" and program_counter==0:
        # adding vairable names in a dictionary
        variable_values[i[1]]=0
    # else:
        # program_counter+=1

    # adding labels
    if ":" in i[0]:
        # labels[(i[0].split(":"))[0]]="0"*(7-len(dec_to_bin(program_counter)))+dec_to_bin(program_counter)
        labels[(i[0].split(":"))[0]]=dec_to_bin(program_counter)

    if i[0]=="var" and program_counter!=0:
        print("Variables not declared at the beginning, line "+str(program_counter+1))
        error_line=program_counter+1
        error=1
        break

    # making final instructions
    if i[0]!="var":
        if ":" in i[0]:
            instructions_with_pc[(i[0].split(":"))[0]]=i[1:]
            program_counter+=1
        else:
            instructions_with_pc[program_counter]=i
            program_counter+=1

for i in variable_values.keys():
    variable[i]=dec_to_bin(program_counter)
    program_counter+=1

# missing hlt instruction-2
if htl_count==0 and error==0:
    print("Missing hlt instruction")
    error=1

# print(error)
# if error==0:
#   for i in instructions_with_pc:
#     print(str(i)+str(instructions_with_pc[i]),end="\n")
#   for i in variable_values.keys():
#     print(i,variable_values[i])
#   for i in labels.keys():
#     print(i,labels[i])


program_counter=1

if error==0:

    for keys in instructions_with_pc:

        if instructions_with_pc[keys][0] == "add" or instructions_with_pc[keys][0] == "sub" or instructions_with_pc[keys][0] == "mul" or instructions_with_pc[keys][0] == "xor" or instructions_with_pc[keys][0] == "or" or instructions_with_pc[keys][0] == "and":
            # print("A")
            if(check_error_type_A(instructions_with_pc[keys])==1):
                print_type_A(instructions_with_pc[keys])
            else:
                print(", line = ",program_counter)
                break

        elif instructions_with_pc[keys][0]=="rs" or instructions_with_pc[keys][0]=="ls" or (instructions_with_pc[keys][0] == "mov" and instructions_with_pc[keys][2] not in register_value):
            # print("B")
            if(check_error_type_B(instructions_with_pc[keys])==1):
                print_type_B(instructions_with_pc[keys])
            else:
                print(", line = ",program_counter)
                break

        elif instructions_with_pc[keys][0] == "mov" or instructions_with_pc[keys][0] == "div" or instructions_with_pc[keys][0] == "not" or instructions_with_pc[keys][0] == "cmp":
            # print("C")
            if(check_error_type_C(instructions_with_pc[keys])==1):
                print_type_C(instructions_with_pc[keys])
            else:
                print(", line = ",program_counter)
                break

        elif instructions_with_pc[keys][0] == "ld" or instructions_with_pc[keys][0] == "st":
            # print("D")
            if(check_error_type_D(instructions_with_pc[keys])==1):
                print_type_D(instructions_with_pc[keys])
            else:
                print(", line = ",program_counter)
                break

        elif instructions_with_pc[keys][0] == "jmp" or instructions_with_pc[keys][0] == "jlt" or instructions_with_pc[keys][0] == "jgt" or instructions_with_pc[keys][0] == "je":
            # print("E")
            if(check_error_type_E(instructions_with_pc[keys])==1):
                print_type_E(instructions_with_pc[keys])
            else:
                print(", line = ",program_counter)
                break

        elif instructions_with_pc[keys][0] == "hlt":
            # print("F")
            if(check_error_type_F(instructions_with_pc[keys])==1):
                print_type_F(instructions_with_pc[keys])
            else:
                print(", line = ",program_counter)
                break

        else:
            print("Typos in instruction name or register name, line = ",program_counter)

        program_counter+=1
            
# Printing Output
for i in output:
    print(i)