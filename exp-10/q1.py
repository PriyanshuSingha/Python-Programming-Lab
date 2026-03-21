class Employee:
     def __init__(self,empid,name,basicpay):
       self.empid=empid
       self.name=name
       self.basicpay=basicpay
       self.ta=0
       self.da=0
       self.grosspay=0
     def calc(self):
         self.ta=0.1*self.basicpay
         self.da=0.4*self.basicpay
         self.grosspay=self.basicpay+self.ta+self.da
         
     def disp(self):
         print("name:",self.name)
         print("empid:",self.empid)
         print("basicpay:",self.basicpay)
         print("ta:",self.ta)
         print("da:",self.da)
         print("grosspay:",self.grosspay)
         
empid=int(input("enter the empid:"))
name=input("enter the name:")
basicpay=float(input("enter the basicpay:"))
     
     
emp=Employee(empid,name,basicpay)
emp.calc()
emp.disp()          
     
     