skills=["Programming logic", "Software Engineering", "OOP", "HTML", "CSS", "Binary Search", "Python Fundamentals", "Data structures", "Writing professionally"]
readSkills = ["Programming logic", "Writing professionally"]
allSkills = []
def Adding_skills(allSkills):
    
    x=input("Pleas select skill(0 for Programming logic, 1 for Software Engineering, 2 for OOP, 3 for HTML, 4 for CSS, 5 for Binary Search, 6 for Python Fundamentals, 7 for Data structures, 8 for Writing professionally): ")
    allSkills.append(skills[int(x)])
    print(allSkills)
    return allSkills

def indicate_skills_studied(allSkills):
    skillToIndicate = input("Please enter skill to indicate studied:")
    readSkills.append(skillToIndicate)
    return (readSkills)

def view_skills_studied():
    skills = readSkills
    print ("read skills are", readSkills)
    


def view_skills_not_studied():
        print ("unread skills are: ", allSkills)


def percent (readSkills, skills):
    readSkills = float(len(readSkills))
    skills= float(len(skills))
    percentage = '{0:.2f}'.format((readSkills / skills * 100))
    print (percentage, "%")
    

Adding_skills(allSkills)

indicate_skills_studied(allSkills)
view_skills_studied()
view_skills_not_studied()
percent (readSkills, skills)


    

