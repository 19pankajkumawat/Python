class Person:
 def __init__(self,id,name):
   self.name = name
   self.id = id

 def Details(self):
  print(f"the name of  {self.id} is {self.name}")

class Programer(Person):
 def showDetails(self):
  print(f"The Name our other detail of other thing is ")

a = Person(401,"rajesh")
a . Details()

b = Person(501,"ravi")
b.Details()

a. showDetails()
a. showDetails()


# class Student:
#  def __init__(self,name,ied,clase,year):
#   self.name  =  name
#   self.year  =  year
#   self.ied   =  ied
#   self.clase =  clase
#  def Details(self):
#   print(f"{self.name}\n{self.ied}\n{self.year}\n{self.clase}")
# a = Student("pankaj Kumawat",3012,3,3)
# a.Details()
#
# b = Student("Ravi",3011,3,3)
# b.Details()