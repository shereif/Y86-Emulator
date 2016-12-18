# Shereif Saleh
# y86emul.py
# Rutgers University Computer Architecture

import y86
import sys
import re

inputfile = sys.argv[1]

global Emulator
Emulator = y86.emulate(inputfile)

global Register
Register = {
'r1': 0,
'r2': 0,
'r3': 0,
'r4': 0,
'r5': 0,
'r6': 0,
'r7': 0,
'r8': 0
}

def CreateMemoryBlock():

    MemoryBlock = [str(Emulator.getRegisterInit())]*Emulator.getSize() # Create my list aka 'MemoryBlock'
    return MemoryBlock

def FillInMemoryBlock(Block): # Probably requires a rework but algo works

    Long = Emulator.getLong()
    Byte = Emulator.getByte()
    Instructions = Emulator.getTextInstructions()
    Splitby2 = [Instructions[x:x+2] for x in range(0, len(Instructions), 2)]
    Instructions = Splitby2
    counter = 0
    #print(Instructions)

    for i in range(0,len(Instructions)):
        Block[i] = Instructions[i]

    try:
        for i in Long:
            Block[i[0]] = i[1]
    except:
        print("No long detected")

    try:
        for j in Byte:
            Block[j[0]] = j[1]
    except:

        print("No byte detected")

    return Block


def ShowMessage(Block):

    l = ['0',0 ]
    s = ''

    for item in Block:
        if item not in l:
            a = int(item,16)
            converted = chr(a)
            s += converted
    print(s)

def PrintMemoryBlock(Block):
    print(Block)

def Instructions(Block):



    #Splitby2 = [Instructions[x:x+2] for x in range(0, len(Instructions), 2)]

    #Instructions = Splitby2
    #print(Block)
    #print(Instructions)
    #print('\n')
    L = ['1']
    counter = 0
    NewB = []
    while counter < len(Block) :
        #NewB = []
        if Block[counter] == '30':
            NewB = Block[counter:counter+6]
            print(NewB)
            temp = ''.join(NewB)
            if temp[3] == '1':
                Register['r1'] = temp[3:4]
            elif temp[3] == '0':
                Register['r0'] = temp[3:4]
            elif temp[3] == '2':
                Register['r2'] = temp[3:4]
            elif temp[3] == '3':
                Register['r3'] = temp[3:4]
            elif temp[3] == '4':
                Register['r4'] = temp[3:4]
            elif temp[3] == '5':
                Register['r5'] == temp[3:4]
            elif temp[3] == '6':
                Register['r6'] == temp[3:4]
            elif temp[3] == '7':
                Register['r7'] == temp[3:4]
            elif temp[3] == '8':
                Register['r8'] = temp[3:4]
            counter += 6
        if Block[counter] == '20':
            print("hit")
            NewB = Block[counter:counter+2]
            print(NewB)
            temp = ''.join(NewB)

            ValueofFirstRegister = 0
            #temp
            #print("temp is ",temp[2],temp)
            #print("temp postion 2 ",temp[2],temp)

            if temp[2] == '0':
                ValueofFirstRegister = Register['r0']
            elif temp[2] == '1':
                ValueofFirstRegister = Register['r1']
            elif temp[2] == '2':
                ValueofFirstRegister = Register['r2']
            elif temp[2] == '3':
                ValueofFirstRegister = Register['r3']
            elif temp[2] == '4':
                ValueofFirstRegister = Register['r4']
            elif temp[2] == '5':
                ValueofFirstRegister = Register['r5']
            elif temp[2] == '6':
                ValueofFirstRegister = Register['r6']
            elif temp[2] == '7':
                ValueofFirstRegister = Register['r7']
            elif temp[2] == '8':
                ValueofFirstRegister = Register['r8']
            if temp[3] == '0':
                Register['r0'] = ValueofFirstRegister
            elif temp[3] == '1':
                Register['r1'] = ValueofFirstRegister
            elif temp[3] == '2':
                Register['r2'] = ValueofFirstRegister
            elif temp[3] == '3':
                Register['r3'] = ValueofFirstRegister
            elif temp[3] == '4':
                Register['r4'] = ValueofFirstRegister
            elif temp[3] == '5':
                Register['r5'] = ValueofFirstRegister
            elif temp[3] == '6':
                Register['r6'] = ValueofFirstRegister
            elif temp[3] == '7':
                Register['r7'] = ValueofFirstRegister
            elif temp[3] == '8':
                Register['r8'] = ValueofFirstRegister


        counter += 2
    print(Register)




"""
    #for i,line in enumerate(Block):
    #    print(type((line)),line)
    #    if line == '30':
    #        a = Block[i:i+6]
    #        print(a)
            #Temp = []
            #Temp.append(Instructions[i:i+6])
            #print(Temp)
"""
if __name__ == '__main__':


    MemoryBlock = CreateMemoryBlock()
    FillInMemoryBlock(MemoryBlock)
    #ShowMessage(MemoryBlock)
    #print(MemoryBlock)
    Instructions(MemoryBlock)

    #PrintMemoryBlock(MemoryBlock)
