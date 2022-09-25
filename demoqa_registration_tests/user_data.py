from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    History = 'History'
    Maths = 'Maths'
    Physics = 'Physics'


class Hobby(Enum):
    Sports = '1'
    Reading = '2'
    Music = '3'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


@dataclass
class User:
    gender: Gender
    name: str
    last_name: str = 'Smirnov'
    email: str = 'gugugeguguge@gmail.com'
    mobile: str = '8889991011'
    birth_day: str = '10'
    birth_month: str = 'May'
    birth_year: str = '1989'
    subjects: Tuple[Subject] = (Subject.History, Subject.Maths)
    current_address: str = 'Somewhere here'
    hobbies: Tuple[Hobby] = (Hobby.Sports,)
    picture_file: str = '22460.jpg'
    state: str = 'NCR'
    city: str = 'Gurgaon'


gosha = User(name='Gosha', gender= Gender.Male)
