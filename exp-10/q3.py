class product:
    def __init__(self,product_id,product_name,price,quantity,total_amount):
      self.product_id=product_id
      self.product_name=product_name
      self.price=price
      self.quantity=quantity
      self.total_amount=total_amount
      
    def member(self):
        self.total_amount=self.price*self.quantity
    def disp(self):
        print(self.product_id)
        print(self.product_name)
        print(self.price)
        print(self.quantity)
        print(self.total_amount)
        
product_name=input("enter the name of the product:")
product_id=int(input("enter the productid:"))
price=int(input("enter the price:"))
quantity=int(input("enter the quantity:"))
total=int(input("enter the total:"))

obj= product(product_name,product_id,price,quantity,total)
obj.member()
obj.disp()
            
      