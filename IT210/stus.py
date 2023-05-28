'''This example defines a class called "Student", where each Student object
has attributes called first, last, techID, major, credits, and gpts.
Currently the only method in the class are the constructor (_init_), a method
to format some of the attribute value into a string (_str_), and a method to
compute GPA for a student (gpa). The code in main demonstrates how each
of these methods is used and how to begin formatting a list of Student
objects.'''

class Student:
    def __init__(self, firstName, lastName, techID, maj, creds, pts):
              #the instance variable of the class are called first, last, techID, credits, gpts
              self.first = firstName
              self.last = lastName
              self.techID = techID
              self.major = maj
              self.credits = creds
              self.gpts = pts

    def __str__(self):
            #This method makes one big string from the values of the instance
            #variables and returns it to the caller. It is useful for
            #printing out the contents of an object.
            printStr = self.first + " " + self.last + "has tech id" + self.techID + "and major" + self.major
            return printStr

    def gpa(self):
        gradePt = self.gpts / float(self.credits)
        return gradePt


def main():
    #create a couple of students to demonstrate how all this works.  This
    #will invoke our contructor, or the __init__ method
    stu1 = Student("Joe", "Dokes", "12345678", "CIT", 30, 94)
    stu2 = Student("Jane", "Doe", "87654321", "CHEM", 25, 80)
    stu3 = Student("Rumman", "Ahmed", "00906009", "IT", 1, 10)

    #we can print out the entire content of an object.  This will invoke
    #our __str__ method
    print (stu1)
    print (stu2)
    print (stu3)

    #now let's see if we can just print the name from out here
    #We'll use the syntax of object name, followed by a period, followed
    #by attribute name to do this
    print ("The name of student 1 is")
    print (stu1.first)
    print (stu1.last)

    #now let's look at the syntax for using the "gpa" method
    avg = stu1.gpa()
    print ("the gpa for ",stu1.last, "is ", avg)

    avg = stu2.gpa()
    print ("the gpa for ", stu2.last, "is ", avg)

    avg = stu3.gpa()
    print ("the gpa for ", stu3.last, "is:", avg)


    #Can we also change the value of an instance variable from outside the class?
    #stu1.first = "Homer"
    #print (stu1.first)


    #Finally, let's put the 2 objects we created into a list of objects.
    stuList = []
    stuList = stuList + [stu1]
    stuList = stuList + [stu2]
    stuList = stuList + [stu3]
    print (stuList[2])
    
main()
