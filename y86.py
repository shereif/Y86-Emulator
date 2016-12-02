#Author Shereif Saleh
#Y86 - Emulator
class emulate():
    def __init__(self,file,size = 0,text = 0,byte = None):
        try: # Attempt read the file
            file_object = open(file,'r')
            self.file = file_object
        except IOError: # Raise exception if error
            print("Wrong file or file path")
            return
        
        seq = ''
        
        #for line in file_object:
#            if line[0:5] == '.byte':
#                byte = ''
#                byte += line
#        self.byte = list(byte)
        
        for i, line in enumerate(file_object):
            if line[0:5] == '.size':
                SIZE = line      # Set self.text
                self.size = SIZE
            if line[0:5] == '.text':
                TEXT = line      # Set self.size
                self.text = TEXT
        
                
    def getRegisterInit(self): # Gives the Register Initial Size
        temp = self.text # Copy of self.text
        return int(temp.partition('\t')[2].rpartition('\t')[0]) #Return my register initial size

    def getTextInstructions(self):
        temp = self.text # Copy of self.text
        NewInstructions = ''
        PreFilteredInstructions = temp.partition('\t')[2].rpartition('\t')[2]
        
        for i in PreFilteredInstructions:
            if i != '\n':
                NewInstructions += i
        return NewInstructions
    
    def getSize(self): # Gets me the Size of my Register
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
        print(self.byte)
    # def getLong(self): This must be implemented to get long from a file
#if __name__ == '__main__':
#    e = emulate('prog2.y86.txt')
    
