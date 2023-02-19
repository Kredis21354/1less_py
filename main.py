class Person:
  name = "Dmytro "
  is_male = True
  age = 14
  height = 180
  weight = 60

  def __init__(self, surname):
    self.surname = surname
    print(self.name)

me = Person("Prokopets")
you = Person("Test")


print(me.surname)
print(me.surname)
  