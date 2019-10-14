class Val(object):
    __slots__=["value"]
    def __init__(self,value=0):
        self.value=value

    def eval(self):
        return self.value

    def __repr__(self):
        return f"Val({self.value})"

v=Val(1)
assert v.eval()==1
print(v)

class Add(object):
    __slots__=["left","right"]
    def __init__(self,a,b):
        self.left=a
        self.right=b
    def eval(self):
        return self.left.eval()+self.right.eval()

e=Add(Val(1),Val(2))
assert e.eval()==3
ee=Add(Val(1),Add(Val(2),Val(3)))
assert ee.eval()==6

print(e.eval())
print(ee.eval())

class Sub(object):
    __slots__=["left","right"]
    def __init__(self,a,b):
        self.left=a
        self.right=b
    def eval(self):
        return self.left.eval()-self.right.eval()

e=Sub(Val(2),Val(1))
assert e.eval()==1
print(e.eval())

class Mul(object):
    __slots__=["left","right"]
    def __init__(self,a,b):
        self.left=a
        self.right=b
    def eval(self):
        return self.left.eval()*self.right.eval()

e=Mul(Val(2),Val(2))
assert e.eval()==4
print(e.eval())