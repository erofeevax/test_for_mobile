class Client():

	maxId = 0

	def __init__(self, ioStrategy, id):
		self.io = ioStrategy
		self.id = id
		self.name = self.io.input("Input name: ")
		self.lastname = self.io.input("Input lastname: ")
		self.patronymic = self.io.input("Input patronymic: ")
		self.organization = self.io.input("Input name of your organization: ")
		self.homephone = self.io.input("Input your home phone: ")
		self.workphone = self.io.input("Input your work phone: ")

	def setName(self):
		self.name = self.io.input("Input name: ")
		self.io.output("Successful operation.")
	
	def setlastname(self):
		self.lastname = self.io.input("Input lastname: ")
		self.io.output("Successful operation.")

	def setpatronymic(self):
		self.patronymic = self.io.input("Input patronymic: ")
		self.io.output("Successful operation.")

	def setorganization(self):
		self.organization = self.io.input("Input name of your organization: ")
		self.io.output("Successful operation.")

	def sethomephone(self):
		self.homephone = self.io.input("Input your home phone: ")
		self.io.output("Successful operation.")

	def setworkphone(self):
		self.workphone = self.io.input("Input your work phone: ")
		self.io.output("Successful operation.")
	def show(self):
		self.io.output(self)

	def __str__(self):
		return (f"\nId: {self.id}\nName: {self.name}\nlastname:{self.lastname}\npatronymic:{self.patronymic}\n"
				f"organization:{self.organization}\nhomephone:{self.homephone}\nworkphone:{self.workphone}\n")

	def edit(self):
		text = ["Name", "Lastname", "Patronymic", "Organization", "Homephone", "Workphone"]
		actions = [self.setName, self.setlastname, self.setpatronymic, self.setorganization,
				   self.sethomephone, self.setworkphone]

		self.io.output("Available edit fields:")
		for i, item in enumerate(text):
			print("{0:1}. {1}".format(i, item))

		while True:
			act = int(self.io.input("Choose action:"))
			if act > len(actions) or act < 0:
				print("Invalid action")
				continue
			actions[act]()
			break
			
