import shelve

db = shelve.open('class_shelve')

sue = db['sue']
sue.give_raise(.25)
db['sue'] = sue

tom = db['tom']
tom.give_raise(.2)
db['tom'] = tom

db.close()
