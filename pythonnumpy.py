import numpy as np

pr = np.array([1, 2, 3, 4, 5])
print(pr)

b = np.array([[[2, 3], [3, 4], [4, 5]]])
print(b)

c = np.arange(1, 11).reshape(2, 5)
print(c)

d = np.zeros((3, 4))   # ✅ shape must be inside double brackets
print(d)
e=np.linspace(-10,10,10)
print(e)
f=np.identity(3)
print(f)
print(b.ndim)
print(b.itemsize)