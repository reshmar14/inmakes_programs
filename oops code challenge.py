class computer:
    def __init__(self,mouse_name, keyboard_name):
     self.mouse_name=mouse_name
     self.keyboard_name=keyboard_name
    def getspecs(self):
        self.width=input("enter width:")
        self.height=input("enter height:")
    def displayspecs(self):
        print(self.width,self.height)
        
class desktop(computer):
    def __init__(self,tab,apps):
        self.tab=tab
        self.apps=apps
    def getdata(self):
        self.tab=input("enter tab name")
        self.apps = input("enter apps name")
    def printdata(self):
        print(self.tab,self.apps)
class laptop(computer):
    def __init__(self,weight):
       self.weight= weight
    def putdata(self):
        self.weight= input("enter lap weight")
    def outdata(self):
        print(self.weight)

obj=desktop("","")
obj.getspecs()
obj.displayspecs()
obj.getdata()
obj.printdata()
obj=laptop("")
obj.putdata()
obj.outdata()



