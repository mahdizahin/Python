class new:
    def __init__(self,h67):
        self.__h67=h67


    def display(self):
        print(self.__h67, "This is n12")

class nw(new):
    pass

n=new(34)
n.display()
nw1=nw(22)
nw1.display()