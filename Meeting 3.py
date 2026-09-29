import random

first_names = ["Super", "Mighty", "Fantastic", "Electric", "Swift", "Newbie"]
last_names = ["Dragon", "Warrior", "Ninja", "Wizard", "Champion", "Master"]

first_name = random.choice(first_names)
last_name = random.choice(last_names)

random_number = random.randint(100, 1000)

nickname = first_name + last_name + str(random_number)
print(nickname)