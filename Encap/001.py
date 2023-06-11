class new:
    def __init__(self,n1):
        self.__n1=n1


    def display(self):
        print(self.__n1, "This is n12")

class nw(new):
    pass

n=new(34)
n.display()
nw1=nw(22)
nw1.display()