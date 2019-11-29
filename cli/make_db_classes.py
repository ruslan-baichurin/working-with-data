import shelve
from cli.manager import Manager
from cli.person import Person

bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manager('Tom Doe', 50, 50000)

db = shelve.open('class_shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()
