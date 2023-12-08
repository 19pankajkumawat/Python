class Person:
 def __init__(self,n,o):
  self.name = n
  self.occ = o
 def coo(self):
  print(f"{self.name}\n{self.occ}")
a = Person("zoro","swordman")
b = Person("Luffy D","Monkey")
a.coo()
b.coo()