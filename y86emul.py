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
'r0': 0,
'r1': 0,
'r2': 0,
'r3': 0,
'r4': 0,
'r5': 0,
'r6': 0,
'r7': 0
}

global SF
SF = 0

global ZF
ZF = 0

global OF
OF = 0


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

def bigEndian(aList):
    rev = aList[::-1]
    outString = ""
    for el in rev:
        outString += el + ""
    return outString

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
    global ZF, SF, OF
    counter = 0
    NewB = []
    while counter < len(Block) :
        #NewB = []
        if Block[counter] == '30': # irmov
            print('\n')
            print('________________________')
            print("Detected instruction 30")
            NewB = Block[counter:counter+6]
            print(NewB)
            newSplitted = bigEndian(NewB[2:])
            Splitted = int(newSplitted,16)
            temp = ''.join(NewB) # This is the full line
            print(temp)
            Flipped = (temp)

            #ConvertedDisplacement = int(Flipped,16)
            #print(ConvertedDisplacement)
            if temp[3] == '0':
                Register['r0'] = Splitted
            elif temp[3] == '1':
                Register['r1'] = Splitted
            elif temp[3] == '2':
                Register['r2'] = Splitted
            elif temp[3] == '3':
                Register['r3'] = Splitted
            elif temp[3] == '4':
                Register['r4'] = Splitted
            elif temp[3] == '5':
                Register['r5'] == Splitted
            elif temp[3] == '6':
                Register['r6'] == Splitted
            elif temp[3] == '7':
                Register['r7'] == Splitted
            elif temp[3] == '8':
                Register['r8'] = Splitted
            counter += 6
            print( Register )
            continue

        if Block[counter] == '20': #rrmovl
            print('\n')
            print('________________________')
            print("Detected instruction 20")
            NewB = Block[counter:counter+2]

            print(NewB)

            temp = ''.join(NewB)
            ValueofFirstRegister = 0

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
            print(Register)
            counter += 2
            continue


        if Block[counter] == 'e0': #movsbl
            print('\n')
            print('________________________')
            print("Detected instruction e0")
            NewB = Block[counter:counter+6]
            print(NewB)
            newSplitted = bigEndian(NewB[2:])
            PushedValue = 0
            Splitted = int(newSplitted,16)
            temp = ''.join(NewB) # This is the full line


            PushedValue = temp[4:]


            if temp[3] == '0':
                PushedValue = Register['r0'] + int(temp[4:])
            elif temp[3] == '1':
                PushedValue = Register['r1'] + int(temp[4:])
            elif temp[3] == '2':
                PushedValue = Register['r2'] + int(temp[4:])
            elif temp[3] == '3':
                PushedValue = Register['r3'] + int(temp[4:])
            elif temp[3] == '4':
                PushedValue = Register['r4'] + int(temp[4:])
            elif temp[3] == '5':
                PushedValue = Register['r5'] + int(temp[4:])
            elif temp[3] == '6':
                PushedValue = Register['r6'] + int(temp[4:])
            elif temp[3] == '7':
                PushedValue = Register['r7'] + int(temp[4:])

            if temp[2] == '0':
                Register['r0'] = PushedValue
            elif temp[2] == '1':
                Register['r1'] = PushedValue
            elif temp[2] == '2':
                Register['r2'] = PushedValue
            elif temp[2] == '3':
                Register['r3'] = PushedValue
            elif temp[2] == '4':
                Register['r4'] = PushedValue
            elif temp[2] == '5':
                Register['r5'] = PushedValue
            elif temp[2] == '6':
                Register['r6'] = PushedValue
            elif temp[2] == '7':
                Register['r7'] = PushedValue



            print(Register)
            print('\n')
            #print(temp[2])

            counter += 6
            continue

        if Block[counter] == '65': #cmpl
            Register1 = ''
            Register2 = ''
            print('\n')
            print('________________________')
            print("Detected instruction 65")
            NewB = Block[counter:counter+2]
            print(NewB)
            temp = ''.join(NewB)

            print("first reg ", temp[2])
            print("second reg ", temp[3])

            if temp[2] == '0':
                Register1 = Register['r0']
            elif temp[2] == '1':
                Register1 == Register['r1']
            elif temp[2] == '2':
                Register1 = Register['r2']
            elif temp[2] == '3':
                Register1 = Register['r3']
            elif temp[2] == '4':
                Register1 = Register['r4']
            elif temp[2] == '5':
                Register1 = Register['r5']
            elif temp[2] == '6':
                Register1 = Register['r6']
            elif temp[2] == '7':
                Register1 = Register['r7']

            if temp[3] == '0':
                Register2 = Register['r0']
            elif temp[3] == '1':
                Register2 == Register['r1']
            elif temp[3] == '2':
                Register2 = Register['r2']
            elif temp[3] == '3':
                Register2 = Register['r3']
            elif temp[3] == '4':
                Register2 = Register['r4']
            elif temp[3] == '5':
                Register2 = Register['r5']
            elif temp[3] == '6':
                Register2 = Register['r6']
            elif temp[3] == '7':
                Register2 = Register['r7']

            if (Register1 > Register2):
                OF = 1
            elif (Register1 < Register1):
                SF = 1
            elif (Register1 == Register2) == True:
                ZF = 1

            else:
                print("No Change")
            counter += 2
            continue

        if Block[counter] == '73': #je
            print('\n')
            print('________________________')
            print("Detected instruction 73")
            NewB = Block[counter:counter+5]
            print(NewB)

            temp = ''.join(NewB)
            Flipped = bigEndian(temp[2:])
            #print(Flipped)
            ChangedToInt = int(Flipped,16)

            if ZF == 1:
                #counter = ChangedToInt
                print(ChangedToInt)
            else:
                print("Not Touched")
            print("Counter is ", counter)
            #set the displacement equal to counter.

            counter+= 5
            continue


        if Block[counter] == 'd0': #movsbl
            print('\n')
            print("Detected instruction d0")
            NewB = Block[counter:counter+6]
            print(NewB)

            temp = ''.join(NewB)
            print(temp)
            Splitted = temp[4:]
            print(Splitted)

            #print what my register has and add the displacement
        counter += 6
        continue




if __name__ == '__main__':
    MemoryBlock = CreateMemoryBlock()
    FillInMemoryBlock(MemoryBlock)
    Instructions(MemoryBlock)
    #print(MemoryBlock)
    #print(MemoryBlock[67])
    print('\n')
    print("Updated registers")
    print(Register)
    print('\n')
    print("SF value = ",SF)
    print("ZF value = ",ZF)
    print("OF value = ",OF)
    #print(bigEndian(aList))
    #print(type(a))
    #print(''.join(a))
