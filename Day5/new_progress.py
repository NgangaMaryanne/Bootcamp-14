class Progress (object):
	allSkills = []
	doneSkills = []
	undoneSkills = []
	def init (self):
		pass
	

	def addSkill (self):
		skill = input("Please input skill you would like to read: ")
		(self.allSkills).append (skill)
		return self.allSkills

	def view_all_skills(self):
		print ("All Skills are: ", self.allSkills)

	def indicate_skill_has_been_read(self):
		skill = input ("please input the skill you have read: ")
		if skill in self.allSkills:
			(self.doneSkills).append(skill)
		return self.doneSkills

	def view_all_done_skills(self):
		print("done skills are: ", self.doneSkills) 
		

	def view_skills_not_read (self):
		for skill in self.allSkills:
			if skill not in self.doneSkills:
				(self.undoneSkills).append(skill)

		print ("un done skills are: ", self.undoneSkills)

	def progress (self):
		results = len(self.doneSkills)/ len(self.allSkills) *100

		print (results, "%")

y = Progress()

y.addSkill()
y.addSkill()
y.addSkill()
y.addSkill()
y.addSkill()
y.addSkill()
y.view_all_skills()
y.indicate_skill_has_been_read()
y.indicate_skill_has_been_read()
y.view_all_done_skills()
y.view_skills_not_read(	)
y.progress()




