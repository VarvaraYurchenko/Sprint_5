from faker import Faker

faker = Faker()


def generate_valid_registration_data():
    name = faker.name()
    email = faker.email()
    password = faker.password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=True)
    return name, email, password


def generate_registration_data_with_invalid_password():
    name = faker.name()
    email = faker.email()
    password = faker.password(length=3, special_chars=False, digits=True, upper_case=True, lower_case=True)
    return name, email, password