
class School:
  def __init__(self, name, level, numberofstudents):
    self.name = name
    self.level = level
    self.numberofstudents = numberofstudents
  
  def __repr__(self):
    return "A {level} school named {name} with {numberofstudents} students".format(level= self.level, name = self.name, numberofstudents=self.numberofstudents)

  def getname(self):
    return self.name
  
  def getlevel(self):
    return self.level
  
  def getnumberofstudents(self):
    return self.numberofstudents

  def setnumberofstudents(self, newnumberofstudents):
    self.numberofstudents = newnumberofstudents

mySchool = School("Codecademy", "High", 100)
print(mySchool)
print(mySchool.getname())
print(mySchool.getlevel())
mySchool.setnumberofstudents(200)
print(mySchool.getnumberofstudents())

class PrimarySchool(School):
  def __init__(self, name, numberofstudents, pickuppolicy, level = 'primary'):
    super().__init__(self,name,numberofstudents)
    self.pickuppolicy = pickuppolicy
  
  def getpickuppolicy(self):
    return self.pickuppolicy

  def __repr__(self):
    parentRepr = super().__repr__(self)
    return parentRepr + "The pickup policy is {pickuppolicy}.".format(pickuppolicy=self.pickuppolicy)
    
testSchool = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(testSchool.getpickuppolicy())
#print(testSchool.getlevel)
#print(testSchool)

class HighSchool(School):
     def init(self, name, numberOfStudents, sportsTeams):
      self.name = name
      self.numberOfStudents = numberOfStudents
      self.sportsTeams = sportsTeams

     def get_sports_teams(self):
      return self.sportsTeams
c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])

print(c.getname())
print(c.getlevel())
print(c.getnumberofstudents())
