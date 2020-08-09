"""Understanding class & object"""


class cal:
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def __str__(self):
        return "value of a and b are " + str(self.a) +" , " + str(self.b)
    def add(self):
        x = self.a+self.b
        return x
    def sub(self,a,b):
        y= a-b
        return y


p = cal(8,4) # Created object p of class cal

print(p.add())
print(p.sub(2,1))

print ("Printing from str method -",p)

#Value of a  & b can also be assinged in object
p.a=100
p.b=120
print (p.add())