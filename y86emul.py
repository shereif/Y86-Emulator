#Author Shereif Saleh
#Y86 - Emulator
import y86

global Emulator
Emulator = y86.emulate('prog1.y86.txt')


def CreateMemoryBlock():
    MemoryBlock = [Emulator.getRegisterInit()]*Emulator.getSize() # Create my list aka 'MemoryBlock'
    return MemoryBlock


    
if __name__ == '__main__':
    print(CreateMemoryBlock())
