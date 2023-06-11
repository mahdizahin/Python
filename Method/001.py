class x:
    def __init__(self,pop):
        self.pop=pop



    def display(self):
        print(self.pop)

    @classmethod
    def cm(cls):
        print("Neo Are you Okay")


x1=x("1200")
x1.cm()
x.cm()
#x1.display()