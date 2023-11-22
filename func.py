from models import *

db.connect()
# names = ['Зернова','Кахановская','Шацкова','Никулина']
# for name in names:
#     Kl_ruk.create(name=name)

# for kl in Kl_ruk.select():
#     Klass.create(name=f'{kl.id+6}', ruk=kl)

for klass in Klass.select():
    print(klass.name, klass.ruk.name)