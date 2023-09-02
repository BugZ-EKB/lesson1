# print(type(print))

price = 100
discount = 5

def discounted(price, discount, max_discount=20):
    price = abs(price) #Значение по модулю
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

price_discounted = discounted(100,15)
print(price_discounted)
discounted(100,500)
discounted(-100,50)
discounted(100,-50)