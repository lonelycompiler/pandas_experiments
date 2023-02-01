from uuid import uuid4
from random import randint
num_people = 10
names = [
    'Olivia',
    'Emma',
    'Charlotte',
    'Amelia',
    'Ava',
    'Sophia',
    'Isabella',
    'Mia',
    'Evelyn',
    'Harper']
ids = [uuid4() for i in range(num_people)]
roles =  [
    'painter',
    'cook',
    'police officer',
    'programmer',
    'it help desk',
    'doctor',
    'scientist',
    'sales',
    'technician',
    'ceo'
]
ages = [randint(20,59) for i in range(10)]
all_companies = ['Google', 'Yahoo', 'Bing']
favorite_colors = 'orange yellow blue red green black white purple pink magenta'.split()
music = 'rock&roll rap country edm metal classical soundtrack'.split() + ['japanese type beat', 'heavy metal', 'indie']

def get_random_companies() -> list:
    return [all_companies[randint(0,len(all_companies)-1)] for i in range(num_people)]

num_dogs = [randint(0,5) for i in range(num_people)]
num_cats = [randint(0,10) for i in range(num_people)]
num_fish = [randint(0,100) for i in range(num_people)]
