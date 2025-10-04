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
b = a
print(a is b)
print(a == b)