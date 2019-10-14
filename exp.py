class Expr(object):
    def eval(self):
        pass

class Binary(Expr):
    def __init__(self,left,right):
        self.left=Expr(left)
        self.right=Expr(right)
    def __repr__(self):
        classname=self.__class__.__name__
        return f'{classname}({self.left},{self.right})'

class Val(Expr):
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

class Add(Expr):
    __slots__=["left","right"]
    def __init__(self,a,b):
        if not isinstance(a,Expr):
            a=Val(a)
        if not isinstance(b,Expr):
            b=Val(b)
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

class Sub(Expr):
    __slots__=["left","right"]
    def __init__(self,a,b):
        self.left=a
        self.right=b
    def eval(self):
        return self.left.eval()-self.right.eval()

e=Sub(Val(2),Val(1))
assert e.eval()==1
print(e.eval())

class Mul(Expr):
    __slots__=["left","right"]
    def __init__(self,a,b):
        self.left=a
        self.right=b
    def eval(self):
        return self.left.eval()*self.right.eval()

e=Mul(Val(2),Val(2))
assert e.eval()==4
print(e.eval())

class Div(Expr):
    __slots__=["left","right"]
    def __init__(self,a,b):
        self.left=a
        self.right=b
    def eval(self):
        return self.left.eval()//self.right.eval()

e=Div(Val(7),Val(2))
assert e.eval()==3
print(e.eval())

assert isinstance(Val(1))
assert isinstance(Div(Val(7),Val(2)),Expr)