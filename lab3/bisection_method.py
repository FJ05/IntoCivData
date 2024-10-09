def bisection_solver(x:int,a:int,b:int,c:int,d:int):
    return (a*(x**3) + b*(x**2) + c*x + d)

print("Enter the values for:\nf(x) = ax³ + bx² + cx + d\nto find f(x)")
print(bisection_solver(int(input("Enter the value for x: ")), int(input("Enter the value for a: ")), int(input("Enter the value for b: ")), int(input("Enter the value for c: ")), int(input("Enter the value for d: "))))