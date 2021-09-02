from faker import Faker
faker = Faker()


def factory_thanos():

    return {
        "name": faker.name(),
        "aliases": "MM",
        "age": 3000,
        "team": "Ordem QA  --- > Ninja",
        "active": True
    }
