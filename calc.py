def clac(s):
    nums=map(int,s.split("+"))
    print("nums=",nums)
    return sum(nums)
print(clac("1+2"))