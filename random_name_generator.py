from faker import Faker

# Create an instance of the Faker class
def generate(gender):
    fake = Faker('en')

    # Generate a random Canadian name
    if gender == 'male':
        random_name = fake.name_male()
    elif gender == 'female':
        random_name = fake.name_female()
    else:
        random_name = fake.name()

    split_name = random_name.split()

    # Extract the first name and last name
    first_name = split_name[0].replace(".", "")
    last_name = split_name[1].replace(".", "")
    return first_name, last_name

# print(generate('male'))