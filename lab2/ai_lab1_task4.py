# WAP for an inventory management system for a retail store. Utilize classes and inheritance to represent different types of products 
# (e.g., electronics, clothing, groceries) with attributes such as name, price, quantity, etc. Implement methods to add products to the inventory, 
# update quantities, and calculate the total value of the inventory. Ensure encapsulation by using private attributes where appropriate.

class inventory:
    def __init__(self):
        self.inventry_list = []
    def add_product(self,id,product,qty,price,type):
        product_detail=[id,product,qty,price,type]
        self.inventry_list.append(product_detail)
        print(f'product added successfully = {self.inventry_list}')
    def update_qty(self,id,qty):
        for i in range(len(self.inventry_list)):
            if self.inventry_list[i][0]==id:
                self.inventry_list=[i][2]=qty
    def total_value(self):
        total=0
        for i in range(len(self.inventry_list)):
            a=self.inventry_list[i][2] * self.inventry_list[i][2]
            total+=a
            print(f'total value of inventry is {total}')


class electronic_inventory(inventory):
    def __init__(self):
        self.inventry_list=[]

    def __str__(self):
        return(str(self.inventry_list))

class clothing(inventory):
    def __init__(self):
        self.inventry_list=[]
    def __str__(self):
        return(str(self.inventry_list))
class groceries(inventory):
    def __init__(self):
        self.inventry_list=[]
    def __str__(self):
        return(str(self.inventry_list))

e=electronic_inventory()
e.add_product(1,'fan',3,2000,'electronic')
e.add_product(2,'laptop',3,2500,'electronic')
print(e)
c=clothing()
c.add_product(1,'cotton cloth',3,2000,'cloth')
c.add_product(2,'cotton cloth',4,200,'cloth')
print(e)
g=groceries()
g.add_product(1,'rice',3,2000,'grocery')
g.add_product(2,'sugar',4,200,'grocery')
print(g)

