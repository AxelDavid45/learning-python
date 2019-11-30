i = 0.30  # Financial interest
n = 3  # Time
vp = 300000  # Amount

# Formula for interest
operation = (vp / ((((1 + i)**n) - 1) / (i * ((1 + i) ** (n - 1)))))

print(operation.__round__(3))  # We print the result rounded
