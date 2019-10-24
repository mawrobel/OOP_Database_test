class Person:
    def __init__(self, name, age, pay=0, job='none'):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastname(self):
        return self.name.split()[-1]

    def giveraise(self, amount):
        self.pay *= (1 + amount)

    def __str__(self):
        return "<%s => %s:%s,%s,%s>" % (self.__class__.__name__, self.name, self.age, self.pay, self.job)


class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, "manager")

    def giveraise(self, amount, bonus=0.1):
        Person.giveraise(self, amount + bonus)


