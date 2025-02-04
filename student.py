class Student:
	def __init__(self, name, grade):
		self.name = name
		self.grade = grade
	def __str__(self):
		return "My name is " + self.name + " I have a grade of " + self.grade

def main():
	student1 = Student("Raffy", "100")
	print(student1)

if __name__ == '__main__':
	main()
