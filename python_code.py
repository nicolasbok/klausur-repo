def f (x,y,z):
    if x == 1:
        if y >= 2:
            if z=="Ulf":
                return y
            elif z=="Bernd":
                return x
        elif y == 2:
            return -99
        elif y>0:
            if y<2:
                return y/2
            else:
                return y/4
        else:
            return 0
    else:
        return x

print(f(1,2,"Ulf"))

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

    

 
