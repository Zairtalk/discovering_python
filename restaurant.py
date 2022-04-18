import random as r
import re

class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_retaurant(self):
        return (self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print("We're open!")

restaurant1 = Restaurant('Asta la vista','wtf')
restaurant2 = Restaurant('La casa','De papa')
restaurant3 = Restaurant('De mama','Mamu meow')
# print(restaurant3.describe_retaurant())
# print(restaurant2.describe_retaurant())
# print(restaurant1.describe_retaurant())
restaurant1.open_restaurant()


# for i in user_id():
#     print(i)
class User:

    def user_id_gen(lenght=4):
        n = '0'*lenght
        while len(n) <= lenght:
            yield n
            n = int(n)+1
            n = '0'*(lenght-len(str(n)))+str(n)
        return

    user_id = iter(user_id_gen(5))

    def __init__(self,first_name:str,last_name:str):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = User.user_id.__next__()

    def describe_user(self):
        print(f'id: {self.user_id}; Name: {self.first_name}, Last name: {self.last_name}')

    def greet_user(self):
        print(f'Privit {self.first_name}')


u1 = User('Dan','Lem')
u2 = User('Zair','talk')
u3 = User('Mari','ia')

u1.describe_user()
u2.describe_user()
u3.describe_user()

def f1():
    f = []
    for i in range(10):
        fn = r.choice()
        ln = r.choice()
        f.append('aaa')
    return f

f = f1()
print(f)
