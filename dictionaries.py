# from pprint import pprint
# product = {
#     "name": "iPhone 12",
#     "stock": 24,
#     "price": 65432.1
# }
# print(len(product))
# product['memory'] = 256
# print(product['price'])
# print(product.get('discount', 0))

# del product['stock']
# print(product)
# phones = ["iPhone 12", "Samsung Galaxy S21", "Xiaomi Mi11"]
# product['recommended'] = phones
# pprint(product)
# product["recommended"].append('iPhone 9')
# pprint(product)

# stock = [
#     {'name': 'iPhone 12 Plus', 'stock': 24, 'price': 65432.1, 
#        'recomended': ['Samsung Galaxy S21', 'iPhone 12']},
#     {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 5000},
#     {'name': 'Xiaomi Mi11', 'stock': 42, 'price': 38000.5}
# ]
# pprint(stock[0]['recomended'][0])
# print(type(stock))
# print(type(stock[0]))

weather = {"city": "Москва", "temperature": "20"}
print(weather["city"])
weather["temperature"] = int(weather["temperature"]) - 5
print(weather)
weather.get('country', 'Россия')
weather['date'] = '27.05.2019'
print(len(weather))