import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius
        
    def get_radius(self):
        return self.radius
    
    def surface_area(self):
        return 4 * math.pi * (self.radius ** 2)
    
    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)
    
def main():
    radius = float(input("Enter the radius of the sphere: "))
    sphere = Sphere(radius)
    
    print(f"Radius: {sphere.get_radius()}\nSurface Area: {sphere.surface_area():.2f}\nVolume: {sphere.volume():.2f}")

if __name__ == "__main__":
    main()