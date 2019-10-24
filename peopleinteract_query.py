import shelve
from DataBase import Person,Manager

fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldnames)
db = shelve.open('class-shelve')
arg = True
while arg:
    key = input('\nKey? => ')
    if not key: break
    if key in db:
        record = db[key]
    else:
        record = Person(key)
    for field in fieldnames:
        print(field.ljust(maxfield), '=>', getattr(record, field))
