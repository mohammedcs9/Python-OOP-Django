class Human:
    def info(self, p_name, p_length, p_age):
        self.name = p_name
        self.length = p_length
        self.age = p_age
        print("Name =", self.name)
        print("Length =", self.length)
        print("Age =", self.age)

h1 = Human()
h2 = Human()
h1.info("ahmed", 180, 20)
h1.info("mohmmad", 170, 25)