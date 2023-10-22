def f (x,y,z):
    if x != 1:
        return x
    else:
        if y >= 2 and z == "Ulf":
            return y
        elif y >= 2 and z=="Bernd":
            return x
        elif y>0 and y<2:
            return y/2
        else:
            return 0
    

print(f(x=1,y=2,z="Ulf"))

def g(x,y):
    for i in range(10):
        result = i * x
    if result >= 20:
        result_1 = result/y
    else:
        result_1 = result * y
    result_2 = (y*x-40)**2
    return result_2/result_1

print(g(1,2))

    

 
