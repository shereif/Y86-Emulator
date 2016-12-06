# Shereif Saleh
# y86emul.py
# Rutgers University Computer Architecture

import y86
import sys

inputfile = sys.argv[1]


global Emulator
Emulator = y86.emulate(inputfile)

def CreateMemoryBlock():
    MemoryBlock = [Emulator.getRegisterInit()]*Emulator.getSize() # Create my list aka 'MemoryBlock'
    return MemoryBlock

def FillInMemoryBlock(Block): # Probably requires a rework but algo worsks
    Long = Emulator.getLong()
    Byte = Emulator.getByte()
    counter = 0
    try:
        for i in Long:
            Block[i[0]] = i[1]
    except:
        print("No long detected")
        
    try:
        for j in Byte:
            Block[j[0]] = j[1]
            counter += 1
        print(counter)
    except:
        print("No long detected")
        
    return Block


def PrintMemoryBlock(Block):
    print(Block)

def Instructions():
    
    return Emulator.getTextInstructions()

if __name__ == '__main__':
    #MemoryBlock = CreateMemoryBlock()
    #FillInMemoryBlock(MemoryBlock)
    #PrintMemoryBlock(MemoryBlock)
    print(Instructions())
