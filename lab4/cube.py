import math

class Cube:
    def __init__(self, length ):
        self.length = length 
        
    def get_length (self):
        return self.length 
    
    def surface_area(self):
        return self.length ** 2
    
    def volume(self):
        return self.length ** 3
    
def main():
    length = float(input("Enter the length of the cube: "))
    cube = Cube(length)
    
    print(f"Radius: {cube.get_length()}\nSurface Area: {cube.surface_area():.2f}\nVolume: {cube.volume():.2f}")

if __name__ == "__main__":
    main()