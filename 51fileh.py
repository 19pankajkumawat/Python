with open('main.txt3', 'r') as f:
 print(type(f))

f.seek(10)

data = f.read(5)
print(data)