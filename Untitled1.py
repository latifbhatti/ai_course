
# coding: utf-8

# In[17]:


def analayze_sentance(s):
    l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','t','x','y','z']
    a=0
    b=1
    for i in s:
        if i in l:
            a+=1
        elif (i==" "):
            b+=1
    return {"total words":b,'total charectors':a,'average word':a/b}
        
a="jfhkjdkj fd"
a=analayze_sentance()
print(a)


# In[45]:


import statistics
def data_analyze(data):
    mean=sum(data)/len(data)
    data.sort()
    if len(data)%2==0:
        a=(len(data)//2)
        median=(data[a-1]+data[a])/2
    else:
        a=(len(data)//2)
        median=data[a]
    abc=0
    abc=statistics.mode(data)
    print(f"mean = {mean} , median =  {median} , mode = {abc}")
data_analyze([1,2,3,4,1])


# In[71]:


class bank:
    def __init__(self):
        pass
    def manage_customer_detail(self):
        pass
    def manage_customer_account(self):
        pass
    
class customer:
    def __init__(self):
        pass
    def customer_detail(self):
        pass
class account:
    def __init__(self):
        pass
    def account_detail(self):
        pass
    def widhdraw(self):
        pass
    def deposit(self):
        pass
class transaction:
    def __init__(self):
        pass
    def transaction_detail(self):
        pass


# In[70]:


class book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
class fiction(book):
    def __init__(self,genre,title,author,price):
        self.genre=genre
        super().__init__(title,author,price)
    def book_info(self):
        print(f"this is fiction book = {self.title} , author name = {self.author}  , price = {self.price}")
        
class non_fiction(book):
    def __init__(self,subject):
        self.subject=subject
        
a=fiction("fiction class",'programming fundamental','mohammad latif',500)
a.book_info()

