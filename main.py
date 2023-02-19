class Person:
  name = "Dmytro "
  is_male = True
  age = 14
  height = 180
  weight = 60
  hobby = "Learning Python"

  def __init__(self, surname):
    self.surname = surname
    #print(self.name)
  
  
  def do_my_thing(self):
    print("I love", self.hobby)



me = Person("Prokopets")
#you = Person("Test")

me.do_my_thing()
me.hooby = "Study"

my_friend = Person("Petrushka")
my_friend.hooby = "Football"


