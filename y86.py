# Shereif Saleh
# y86.py
# Rutgers University Computer Architecture

class emulate():
    def __init__(self,file,size = 0,text = 0,byte = None, long = None,instructions= 0):
        try:                       # Attempt read the file
            file_object = open(file,'r')
            self.file = file_object
        except IOError:            # Raise exception if error
            print("Wrong file or file path")
            return

        BYTE = ''
        LONG = ''
        INSTRUCTIONS = ''

        for i, line in enumerate(file_object):
            if line[0:5] == '.size':
                SIZE = line        # Set self.text
                self.size = SIZE
            if line[0:5] == '.text':
                TEXT = line        # Set self.size
                self.text = TEXT
            if line[0:5] == '.byte':
                BYTE += line
            if line[0:5] == '.long':
                LONG += line


        self.byte = BYTE
        self.long = LONG
        self.instructions = INSTRUCTIONS

    def getRegisterInit(self):     # Gives the Register Initial Size
        temp = self.text           # Copy of self.text
        return int(temp.partition('\t')[2].rpartition('\t')[0]) #Return my register initial size

    def getTextInstructions(self):
        temp = self.text           # Copy of self.text
        NewInstructions = ''
        PreFilteredInstructions = temp.partition('\t')[2].rpartition('\t')[2]

        for i in PreFilteredInstructions:
            if i != '\n':
                NewInstructions += i
        self.instructions = NewInstructions
        return self.instructions

    def getSize(self):              # Gets me the Size of my Register
        num = ['0','1','2','3','4','5','6','7','8','9']
        mySize = ''
        temp = self.size
        self.temporarySIZE = ''

        for i in temp:              # Adjust for formatting
            if i != '\t' and i != '\n':
                self.temporarySIZE += i
            elif i == '\t' or i == '\n':
                self.temporarySIZE += ' '

        for i in self.temporarySIZE: # Find my number
            if i in num:
                mySize += i

        self.size = int(mySize,16)   # Change my size into an an Integer
        return self.size

    def getByte(self):
        myByte = ''
        longByte = []
        splitByte = self.byte.split()
        for i in range(1,len(splitByte),1):
            longByte.append(splitByte[i])

        longByte = [x for x in longByte if x != '.byte'] # Remove .byte

        final = [[int(longByte[i],16),longByte[i+1]] for i in range(0,len(longByte),2)]
        print(final)
        self.byte = final
        if self.byte == [ ]:
            return None
        return self.byte

    def getLong(self):
        myLong = ''
        longList = [ ]
        splitLong = self.long.split()
        for i in range(1,len(splitLong),1):
                longList.append(splitLong[i])

        longList = [x for x in longList if x != '.long'] # Remove .long

        final = [[int(longList[i],16),longList[i+1]]for i in range(0,len(longList),2)]

        self.long = final
        if self.long == [ ]:
            return None

        return self.long





#if __name__ == '__main__':
#    e = emulate('prog1.y86.txt')
    #(e.getTextInstructions())
#    print(e.optcode())
#    print(e.getByte())
#    print(e.getLong())
