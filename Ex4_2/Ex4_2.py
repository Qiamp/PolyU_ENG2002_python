import pdb
x = 5
#x=5
pdb.set_trace()
mX = x #Line A
#x=5 , mx=5
def func():
    x = 900
    global mX
    mX = x #Line B
func()
# mx=900,x=5
x=10 #Line C
# mx=900,x=10