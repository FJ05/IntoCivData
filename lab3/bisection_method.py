def f(x:float,a:float,b:float,c:float,d:float):
    return (a*(x**3) + b*(x**2) + c*x + d)

def l(a:float,b:float,c:float,d:float):
    l = 0
    while f(l,a,b,c,d) >= 0:
        l -= 1
    return l

def r(a:float,b:float,c:float,d:float):
    r = 0
    while f(r,a,b,c,d) <= 0:
        r =+ 1
    return r

def bisection_method(l,r,f:float,t, coef:float):
    while (r, - 1) / 2.0 > t:
        c = (l + r) / 2.0
        fc = f(c, *coef)

        if abs(fc) <=  t:
            return c
        elif f(l, *coef) * fc < 0:
            r = c
        else:
            l = c
    return (l + r) / 2.0

print("Enter the values for:\nf(x) = ax³ + bx² + cx + d\nto find f(x)")
x,a,b,c,d = float(input("Enter the value for x: ")), float(input("Enter the value for a: ")), float(input("Enter the value for b: ")), float(input("Enter the value for c: ")), float(input("Enter the value for d: "))

print(f"f({x}) = {f(x,a,b,c,d)}")
l = l(a,b,c,d)
print(f"f({l}) < 0")
r = r(a,b,c,d)
print(f"f({r}) > 0")
aprox = bisection_method(l,r,f,0.001,(a,b,c,d))
print(f"An approximate solution of f(x) = 0 is f({aprox})\nf({aprox}) = {f(aprox, a,b,c,d)}")
