from exp import Val,Add,Mul,Sub,Div

'''
def parse(s:str):
    num=int(s)
    return Val(num)


e=parse("123")
print(e)

s="123+456"
pos=s.find("+")
print("pos",pos)

s1=s[0:pos]
s2=s[pos+1:]
print(s,s1,s2)

s="1+2"
pos=s.find("+")
s1=int(s[0:pos])
s2=int(s[pos+1:])
print(s1+s2)
'''

def parse(s:str):

    if s.find("+")>0:
        pos=s.find("+")
        s1=s[0:pos]
        s2=s[pos+1:]
        return Add(parse(s1),parse(s2))
    if s.rfind("-")>0:
        pos=s.rfind("-")
        s1=s[0:pos]
        s2=s[pos+1:]
        return Sub(parse(s1),parse(s2))
    if s.find("*")>0:
        pos=s.find("*")
        s1=s[0:pos]
        s2=s[pos+1:]
        return Mul(parse(s1),parse(s2))
    if s.rfind("/")>0:
        pos=s.rfind("/")
        s1=s[0:pos]
        s2=s[pos+1:]
        return Div(parse(s1),parse(s2))
    return Val(int(s))

e=parse("8/4+2")
print(e,e.eval())