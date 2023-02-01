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
