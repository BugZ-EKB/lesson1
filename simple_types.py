a = 2.5
b  = 3.1
print(a + b)
a = 'Hello'
b = 'World'
print(a + ", " + b + "!")
c = f'{a}, {b}!'
print(c.upper())
print(len(c))

a = 'Прив3т т3б3'.replace('3', 'e')
print(a)

#chaining
a = 'ПриветЫ'.lower().replace('ы','').capitalize()
print(a)

a = 'learn.python.ru'
print(a.split('.'))