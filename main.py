print("1. Operators")

print("1.1 Arithmetic")
a = 7
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b )
print(a // b) # integer division, floor
print(a % b)  # remainder
print(a ** b)

print("1.2 Assignment")
x = 10
x += 2
print(x)
x *= 3
print(x)

print("1.3 Comparison")
w, h, d = 20, 10, 5
print(w == 20)
print(h != 20)
print(w > h)
print(d <= 5)

print("1.4 Logical")
print((w > 0) and (h > 0))
print((w > 50) or (h > 0))
print(not (d==5))

print("1.5 Membership & Identity")
name = "bracket_mount_v2.stl"
print("v2" in name)
vals = [0.08, 0.12, 0.16, 0.2]
print(0.2 in vals)
a = [1, 2, 3]
b = [1,2,3]
print(a is b)
print(a == b)

print("1.6 Precedence & Grouping")
result = 2 + 3 * 4
print(result)
result = (2 + 3) * 4
print(result)

print("1.6 Type Conversion & Truthiness")
print(float("3.5"))
print(int(3.9))
print(bool([]))
print(bool([1]))

print("2. Comtrol flow")
print("2.1 if / elif / else")
density = 1.24   #g/cm3
volume = 12.5
mass = density * volume
if mass > 20:
    print("Heavy part")
elif mass > 5:
    print("Medium part")
else:
    print("Light part")

print("2.2 Loops (for / while)")
files = ["arm_v1.stl", "arm_v2.stl", "gear.stl"]
for f in files: 
    if not f.endswith(".stl"):
        continue
    print("STL:", f)
n=5
while n > 0:
    print(n)
    n -= 1

print("2.3 Range, enumerate, zip")
for i in range(5):
    print(i)

for i, f in enumerate (files, start=1):
    print(i, f)

width = [2,6,7]
height = [3,8,4]
for w, h in zip(width, height):
    print("area", w*h)

print("2.4 Comprehensions")
vals = [0.08, 0.09, 0.12, 0.2, 0.21]
allowed = [0.08, 0.12, 0.16, 0.2]
clean = [v for v in vals if v in allowed]
print(clean)


# Final project
filCost = 25/1000  #filament cosy per gram
partWeight = 120  #part weight in grams 
printCost = filCost * partWeight
print(f"Print cost: {printCost} \u20AC")

# unit conversion
length_mm = 25 
length_in = length_mm / 25.4
print(f"length = {length_in:.4f} in")

#filter
files = ["gear_v1.stl", "gear_v2.stl", "mount_v2.stl", "cover.stl"]
for f in files:
    if "v2" in f:
        print(f)

# Volume gate
dims_mm = [(40,20,55),(27,35,200), (80,45,88), (20,20,75), (440, 15,78)]
for dim_mm in dims_mm:
    dim_cm = tuple (a/10 for a in dim_mm)
    w,h,d = dim_cm
    if w*h*d > 100:
        print(dim_cm)

# Comprehension
vals = [0.08, 0.09, 0.12, 0.2, 0.21]
allowed = [0.08, 0.12, 0.16, 0.2]

filtered = [val for val in vals if val in allowed]
print(filtered)