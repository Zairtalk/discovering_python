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

    def _user_id_gen(lenght=4):
        n = '0'*lenght
        while len(n) <= lenght:
                yield n
                n = int(n)+1
                n = '0'*(lenght-len(str(n)))+str(n)

    _user_id = iter(_user_id_gen(5))

    def __init__(self,first_name:str,last_name:str):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = User._user_id.__next__()

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

def f1(num=10):
    f = []
    for i in range(num):
        fn = chr(r.randint(65,90)) + ''.join(list(chr(r.randint(97,122)) for i in range(0,r.randint(3,7))))
        ln = chr(r.randint(65,90)) + ''.join(list(chr(r.randint(97,122)) for i in range(0,r.randint(3,7))))
        f.append(User(fn,ln))
    return f

def f2(f):
    for i in f:
        i.describe_user()

f = f1(100)
# print(f)
f2(f)
