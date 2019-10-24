from DataBase import Person, Manager
import shelve

mick = Person("Michael Sparrow", 21, 3400, "software programist")
bob = Person("Bob Smith", 24, 5000, "architect")
tom = Manager("Thomas Mitnick", 42, 10000)

db = shelve.open('class-shelve')
db['mick'] = mick
db['bob'] = bob
db['tom'] = tom
db.close()
