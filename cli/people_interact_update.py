import shelve
from cli.person import Person

field_names = ('name', 'age', 'job', 'pay')

db = shelve.open('class_shelve')
while True:
    key = input('\nKey? => ')
    if not key:
        break
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')
    for field in field_names:
        current_val = getattr(record, field)
        new_val = input(f'\t{field}={current_val}\n\tnew?=>')
        if new_val:
            setattr(record, field, eval(new_val))
    db[key] = record
db.close()