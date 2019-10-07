import itertools

class DistributeurDeCapote():
    stock = True
    def allumer(self):
        while self.stock:
            yield "capote"


def creerGenerateur():
    mylist = range(3)
    for i in mylist:
        yield i*i


generateur = creerGenerateur()
print(generateur.__next__())
print(generateur.__next__())
print(generateur.__next__())


distributeur_en_bas_de_la_rue = DistributeurDeCapote()
distribuer = distributeur_en_bas_de_la_rue.allumer()

for c in distribuer:
    print(c)
    break

print("1--------")
d = DistributeurDeCapote().allumer()
generateur = itertools.chain("13245", d)
generateur = itertools.islice(generateur, 0, 12)
for x in generateur:
    print(x)


print("2--------")

gen = iter([1, 2, 3])
print(gen.__next__())


class MonIterableRienQuaMoi(object):
    def __iter__(self):
        yield 'Python'
        yield "ça"
        yield 'déchire'

gen = iter(MonIterableRienQuaMoi())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())

print("MonIterableRienQuaMoi:")
for x in MonIterableRienQuaMoi():
    print(x)









