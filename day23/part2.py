def mod(i):
    if i == 1: return 1000000
    else: return i-1

class Cup:
    def __init__(self, value):
        self.nextcup = None
        self.value = value
        self.prevvalues = [None, None, None, None]

class CupList:
    def __init__(self):
        self.pointer = None
        self.maxvalue = 0

    def addcup(self, value):
        self.maxvalue = max(self.maxvalue, value + 1)
        newcup = Cup(value)
        if self.pointer == None:
            newcup.nextcup = newcup
            newcup.prevcup = newcup
        else:
            newcup.prevcup = self.pointer
            newcup.nextcup = self.pointer.nextcup
            newcup.nextcup.prevcup = newcup
            self.pointer.nextcup = newcup
        self.pointer = newcup

    def loadprev(self):
        curcup = self.pointer
        while curcup.prevvalues[0] is None:
            compcup = curcup.prevcup
            while None in curcup.prevvalues:
                if (curcup.value - compcup.value) % self.maxvalue < 5:
                    curcup.prevvalues[(curcup.value - compcup.value) % self.maxvalue - 1] = compcup
                compcup = compcup.prevcup
            curcup = curcup.prevcup
        self.pointer = self.pointer.nextcup

    def rearrange(self):
        newvalue = (self.pointer.value - 1) % self.maxvalue
        temppointer = self.pointer
        movedvalues = []
        for i in range(3):
            temppointer = temppointer.nextcup
            movedvalues.append(temppointer.value)
        while newvalue in movedvalues: newvalue = (newvalue - 1) % self.maxvalue
        index = (self.pointer.value - newvalue - 1) % self.maxvalue

        leftpaste = self.pointer.prevvalues[index]
        rightpaste = leftpaste.nextcup
        leftcut = self.pointer.nextcup
        rightcut = leftcut.nextcup.nextcup.nextcup
        
        self.pointer.nextcup = rightcut
        rightcut.prevcup = self.pointer
        leftpaste.nextcup = leftcut
        leftcut.prevcup = leftpaste
        leftcut.nextcup.nextcup.nextcup = rightpaste
        rightpaste.prevcup = leftcut.nextcup.nextcup

        self.pointer = self.pointer.nextcup

    def getanswer(self):
        temppointer = self.pointer
        while temppointer.value != 1: temppointer = temppointer.nextcup
        print(temppointer.value, temppointer.nextcup.value, temppointer.nextcup.nextcup.value)

    def printvals(self):
        output = [self.pointer.value]
        temppointer = self.pointer.nextcup
        while temppointer != self.pointer:
            output.append(temppointer.value)
            temppointer = temppointer.nextcup
        print(output)

cupnums = [5, 3, 8, 9, 1, 4, 7, 6, 2]
cups = CupList()
for i in cupnums: cups.addcup(i)
for i in range(10, 1000000): cups.addcup(i)
cups.addcup(0)
cups.loadprev()
b = 1
for i in range(10000000):
    cups.rearrange()
cups.getanswer()
