def sphereCalculator(ray):
    pi = 3.14159
    return ((4/3.0) * pi * (ray ** 3))

ray = float(input())
result = sphereCalculator(ray)
print(f"VOLUME = {result:.3f}")