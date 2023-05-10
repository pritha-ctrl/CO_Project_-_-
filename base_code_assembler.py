import sys

# opcode (predefined)
opcode={"add": "00000","sub": "00001","mov": "00010","mov": "00011","ld": "00100","st": "00101","mul": "00110","div": "00111","rs": "01000","ls": "01001","xor": "01010","or": "01011","and": "01100","not": "01101","cmp": "01110","jmp": "01111","jlt": "11100","jgt": "11101","je": "11111","hlt": "11010"}

# registers (predefined) and default values
register={"R0": "000","R1": "001","R2": "010","R3": "011","R4": "100","R5": "101","R6": "110","FLAGS": "111"}
register_value={"R0":0,"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0}

# flags (predefined)
flags={"V": "00000000000000001000","L": "00000000000000000100","G": "00000000000000000010","E": "00000000000000000001"}

# list of variable names
variable=[]

# list of labels names
labels=[]

program_counter=-1

# input from file
with open('input.txt') as fin:
    l=[]
    for i in fin:
        l.append(i.split())
# for i in l:
#     print(i,end="\n")

# final instructions to be executed
instructions=[]

# error flag and error line
error=0
error_line=-1

# hlt code count (only 1 allowed in code)
htl_count=0

# checking errors in input and making final instructions list and creating variables
for j in range(0,len(l)):
    i = l[j]

    # Invalid Codes
    if i[0] not in opcode.keys() and i[0] != 'var' and ':' not in i[0]:
        print("General Syntax Error, line "+str(program_counter+2))
        error=1
        error_line=program_counter+2
        break
    
    # hlt not used at last
    if i[-1]=='htl' and j!=len(l)-1:
        print("hlt not being used as the last instruction, line "+str(program_counter+2))
        error=1
        error_line=program_counter+2
        break
    
    # missing hlt instruction-1
    if i[-1]=='hlt' and j==len(l)-1:
        htl_count+=1
        error_line=program_counter+2
    
    # Variable defining not at beginning
    if i[0]=='var' and program_counter==-1:
        # adding vairable names in a list
        variable.append(i[1])
    else:
        program_counter+=1

    # adding labels
    if ':' in i[0]:
        labels.append((i[0].split(':'))[0])
    
    if i[0]=='var' and program_counter!=-1:
        print("Variables not declared at the beginning, line "+str(program_counter+2))
        error_line=program_counter+2
        error=1
        break
    
    # making final instructions
    if i[0]!='var' and i[-1]!='hlt' and ':' not in i[0]:
        instructions.append(i)
        program_counter+=1


# missing hlt instruction-2
if htl_count==0 and error==0:
    print("Missing hlt instruction")
    error=1

new_program_counter=0
new_error_line=0

# print(error)
# if error==0:
for i in instructions:
    print(i,end="\n")
# for i in variable:
#   print(i)
# for i in labels:
#   print(i)