#!/usr/bin/env python3

import random as r
import os
import json


class User:

    @staticmethod
    def _user_id_gen(lenght=4):
        n = '0'.zfill(lenght)
        while len(n) <= lenght:
                yield n
                n = int(n)+1
                n = str(n).zfill(lenght)
        return

    _user_id = iter(_user_id_gen())

    def __init__(self,first_name:str,last_name:str):
        self.first_name = first_name
        self.last_name = last_name
        try:
            self.user_id = User._user_id.__next__()
        except StopIteration as e:
            raise e
    def describe_user(self):
        print(f'id: {self.user_id}; Name: {self.first_name}, Last name: {self.last_name}',end='\n')

    def _return_credentials(self):
        return self.user_id + ';' + self.first_name + ';' + self.last_name

    def greet_user(self):
        print(f'Privit {self.first_name}')


class UserEncoder(json.JSONEncoder):

    def default(self,obj):
        if isinstance(obj,User):
            return {'id':obj.user_id,'Name':obj.first_name,'Last name':obj.last_name}
        else:
            return super().default(obj)


def generate_random_users(num=10):
    f = []
    for i in range(num):
        fn = chr(r.randint(65,90)) + ''.join(list(chr(r.randint(97,122)) for i in range(0,r.randint(3,7))))
        ln = chr(r.randint(65,90)) + ''.join(list(chr(r.randint(97,122)) for i in range(0,r.randint(3,7))))
        f.append(User(fn,ln))
    return f

def print_users(f):
    for i in f:
        i.describe_user()

def save_users(user_list,file='users.dat'):
    with open(file,'tw') as f:
        for user in user_list:
            f.write(user._return_credentials() + '\n')

def load_users(file='users.dat'):
    users = []
    loaded_users = []
    with open(file,'tr') as f:
        for line in f:
            user = line.strip()
            user = list(user.split(';'))
            users.append(user)
    for user in users:
        loaded_users.append(User(user[1],user[2]))
    return loaded_users

def save_users_json(user_list,file='users.json'):
    '''Converting list of User instances to proper json file'''
    with open(file,'tw') as f:
        data = '['
        for user in user_list:
            data += json.dumps(user,cls=UserEncoder,indent=4,separators=(',',': ')) + ',\n'
        else:
            data = data[:-2] #remove last ,
            data += ']'
        f.write(data)

def load_users_json(file='users.json'):
    '''Reads json file and returns a list with User instances'''
    loaded_users = []
    with open(file,'tr') as f:
        users = json.load(f)
        for user in users:
            loaded_users.append(User(user['Name'],user['Last name']))
    return loaded_users
# def menu():
#     l = input('Do you wish to generate new users ?')

# l = generate_random_users(num=100)
# save_users_json(l)
l = load_users_json()
print_users(l)
