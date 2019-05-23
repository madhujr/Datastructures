class node:
    def __init__(self,d):
      self.data=data
      self.nextt=None
class sll:
    def __init__(self):
        self.head=None

    def insertAtBeg(self,data):
        temp=node(data)
        if slo.head!=None:
             temp.nextt=slo.head
             slo.head=temp
        else:
            slo.head=temp

    def delAtBeg(self):
        temp=self.head
        self.head=self.head.nextt
        temp.nextt=None
    def printlist(self):
        temp=self.head
        while temp!=None:
            print(temp.data,"==>")
            temp=temp.nextt
        print("none")    
slo=sll()
ch=0
while ch!=4:
    print("1.insertion 2.deletion 3.print4.exit")
    ch=int(input())
    if ch==1:
        print("enter the value")
        data=input()
        slo.insertAtBeg(data)
        slo.printlist()
    elif ch==2:
       slo.delAtBeg()
       slo.printlist()
    elif ch==3:
       slo.printlist()
    
