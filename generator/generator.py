from data.data import User
from faker import Faker

faker_en = Faker('En')


def generator_user():
    return User(
        email=faker_en.email(),
        password=faker_en.password()
    )
