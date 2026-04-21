# dating_profile.py

def validate_age(age_input):
    # make sure age is a number and is not impossible to be.
    if age_input.isdigit() == False:
        print("Error: Age must be a number.")
        return None
    age = int(age_input)
    if age < 18:
        print("Error: You must be at least 18.")
        return None
    if age > 120:
        print("Error: Please enter a valid age.")
        return None
    return age

#this just exists to have the name  not be empty and blow the program up
def validate_name(name):
    if name == "":
        print("Error: Name cannot be empty.")
        return False
    return True

#this just exists to have the bio not be empty and blow the program up
def validate_bio(bio):
    if bio == "":
        print("Error: Bio cannot be empty.")
        return False
    return True


# this is where profile gets created. 

def create_profile():
    print("--- Create Your Profile ---")

    # input a name
    name = input("Enter your name: ")
    while validate_name(name) == False:
        name = input("Enter your name: ")

    # input a age
    age_input = input("Enter your age: ")
    age = validate_age(age_input)
    while age == None:
        age_input = input("Enter your age: ")
        age = validate_age(age_input)

    # input a gender (prob delete ts)
    gender = input("Enter your gender: ")

    # input a bio (idk if this matters much either.)
    bio = input("Enter your bio: ")
    while validate_bio(bio) == False:
        bio = input("Enter your bio: ")

    # input a interest (idk if this also matters)
    interests_input = input("Enter your interests (separated by commas): ")
    interests = interests_input.split(",")  # this creates a list

    # sShoves it all into a dict
    profile = {
        "name": name,
        "age": age,
        "gender": gender,
        "bio": bio,
        "interests": interests
    }

    return profile


#this is just the printing of the profile

def display_profile(profile):
    print("--------------------")
    print("Name: " + profile["name"])
    print("Age: " + str(profile["age"]))
    print("Gender: " + profile["gender"])
    print("Bio: " + profile["bio"])
    print("Interests: " + str(profile["interests"]))
    print("--------------------")

