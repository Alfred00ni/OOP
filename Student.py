# Student Class - Defines the student object
class Student:

    Grade = 0
    PassingScore = 75
    AwardCridit = False


    #initilaizer sometime called a constructor
    def __init__(self, FirstName, LastName, Status):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = self.FirstName.lower() + self.LastName.lower() + '@weber.edu'
        self.Status = Status

    def PrintStudentInfo(self):
        print('STUDENT:', self.FirstName, self.LastName, '\nEMAIL:', self.Email, '\nSTATUS:', self.Status, '\nPassing',self.AwardCridit)

    def SetGrade(self, NewGrade):
        self.Grade = NewGrade
        if (self.Grade >= self.PassingScore):
            self.AwardCridit = True
        if (self.Grade < self.PassingScore):
            self.AwardCridit = False


scott = Student('Scott','Hadzik', 'Full-time')  #scott is an instance of the Student Class
camille = Student('Camille', 'Hadzik', 'Part-time') #calille is an instnace of the Student class 

scott.SetGrade (80)

print ('\n')

scott.PrintStudentInfo()
camille.PrintStudentInfo()