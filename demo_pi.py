import numpy as np

def calculate_area(r):
    return np.pi * (r ** 2)

def calculate_volume(r):
    return (4 / 3) * (r ** 3) * np.pi

def main():
    r = int(input("Enter radius: "))
    A = calculate_area(r)
    V = calculate_volume(r)
    print("Radius: ", r)
    print("Area: ", round(A, 2))
    print("Volume: ", round(V, 2))

if __name__ == "__main__":
    main()
