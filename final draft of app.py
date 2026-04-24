# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 23:32:37 2026

@author:loganpuentes
"""


import requests
import random

# profile class 
class Profile:
    def __init__(self, name, age, gender, bio, interests):
        self.name = name
        self.age = age
        self.gender = gender
        self.bio = bio
        self.interests = interests

    def display(self):
        print("\n")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Bio: {self.bio}")
        print(f"Interests: {', '.join(self.interests)}")
        print("\n")



# validation functions
#this function just makes sure that our users are of a reasonable age and not something impossbile. 
def validate_age(age_input):
    try:
        age = int(age_input)
    except ValueError:
        print("Error: Age must be a number.")
        return None

    if age < 18:
        print("Error: You must be at least 18.")
        return None
    if age > 120:
        print("Error: Please enter a valid age.")
        return None

    return age

#prevents empty inputs.
def validate_notempty(text, field_name):
    if text.strip() == "":
        print(f"Error: {field_name} cannot be empty.")
        return False
    return True

#how would anyone know your name if this didnt exist.
def validate_name(name):
    if name.strip() == "":
        print("Error: Name cannot be empty.")
        return False
    if not all(c.isalpha() or c.isspace() for c in name):
        print("Error: Name must contain letters only.")
        return False
    return True


# create profile
def create_profile():
    print("\n---Create Your Profile---")

    name = input("Enter your name: ").strip()
    while not validate_name(name):
        name = input("Enter your name: ").strip()

    age_input = input("Enter your age: ").strip()
    age = validate_age(age_input)
    while age is None:
        age_input = input("Enter your age: ").strip()
        age = validate_age(age_input)

    gender = input("Enter your gender: ").strip()

    bio = input("Enter your bio: ").strip()
    while not validate_notempty(bio, "Bio"):
        bio = input("Enter your bio: ").strip()

    interests_input = input("Enter your interests in between commas: ")
    interests = [i.strip() for i in interests_input.split(",") if i.strip()]

    profile_summary = {
        "name": name,
        "age": age,
        "gender": gender,
        "bio": bio,
        "interests": interests
    }
    print("\nProfile Summary:", profile_summary)

    profile = Profile(name, age, gender, bio, interests)
    print("\nProfile created successfully!\n")
    return profile



# This pulls random users from our API
def get_random_users(n):
    try:
        data = requests.get(f"https://randomuser.me/api/?results={n}").json()
    except:
        print("Could not fetch profiles from the api.")
        return []
#random bio inputs to make it feel organic
    bio_options = [
        "I am a foodie what can I say!",
        "Looking for someone to go on adventures with!.",
        "I can do a backflip!",
        "Coffee lover.",
        "Dog person.",
        "Outdoorsman!",
        "Just moved to the city and looking for a local!",
        "Big fan of live music and road trips.",
        "I spend my weekends outdoors whenever I can.",
        "I love gaming!",
        "Work hard, play hard baby!",
    ]
#random interest options to make it feel organic
    interest_options = ["music", "movies", "travel", "gaming", "basketball",
                        "soccer", "hiking", "cooking", "reading", "photography",
                        "fitness", "art", "concerts", "cycling", "yoga","learning","surfing",]

    profiles = []
    for user in data["results"]:
        # puts first and last name together as a pair. 
        user_info = (f"{user['name']['first']} {user['name']['last']}", user["dob"]["age"])
        name = user_info[0]
        age = user_info[1]
        gender = user["gender"]
        #takes the random choices for bio and interests and allows them to be randomly combined.
        bio = random.choice(bio_options)
        interests = random.sample(interest_options, 3)
# makes everything look nice. 
        profiles.append(Profile(name, age, gender, bio, interests))

    random.shuffle(profiles)
    return profiles

# this lets us browse profiles and like dislike or quit.

def browse_profiles(profiles, liked, disliked):
    """Show profiles one at a time and like or pass!"""
    if not profiles:
        print("\nNo profiles available to browse.\n")
        return

    print("\nBrowsing Profiles ")
    print("Enter Y to Like, N to Pass, Q to Quit Browsing.\n")

    for profile in profiles:
        profile.display()

        choice = input("Like this profile? (Y/N/Q): ").strip().lower()

        while choice not in ["y", "n", "q"]:
            print("Invalid choice.")
            choice = input("Like this profile? (Y/N/Q): ").strip().lower()

        if choice == "y":
            liked.append(profile)
            print(f"You liked {profile.name}.\n")

        elif choice == "n":
            disliked.append(profile)
            print(f"You passed on {profile.name}.\n")

        elif choice == "q":
            print("Stopping browsing for now!\n")
            break


# We can view the users that we have assigned a like to with this. it also kicks us out if we havent liked anything yet. 
def view_likes(liked):
    if not liked:
        print("\nYou haven't liked any profiles yet.\n")
        return

    print("\nYour Liked Profiles")
    for p in liked:
        p.display()


# our main menu input option portion. this just lets us have a easy way to choose what the user wants to interact with. 
menu_input = ("1", "2", "3", "4")

def main_menu():
    user_profile = None
    liked_profiles = []
    disliked_profiles = []
    random_profiles = []

    while True:
        print("=== App Menu ===")
        print("1. Create My Profile")
        print("2. Browse Random Profiles")
        print("3. View Liked Profiles")
        print("4. Quit")

        choice = input("Choose an option: ").strip()

        if choice not in menu_input:
            print("Invalid option. Try again.\n")
            continue

        if choice == "1":
            user_profile = create_profile()
            user_profile.display()

        elif choice == "2":
            amount = input("How many profiles do you want to browse? ")
            try:
                amount = int(amount)
            except:
                print("invalid input, please enter a specific number of profiles you want to view. ")
                continue

            random_profiles = get_random_users(amount)
            browse_profiles(random_profiles, liked_profiles, disliked_profiles)

        elif choice == "3":
            view_likes(liked_profiles)

        elif choice == "4":
            print("Goodbye!")
            break



# this makes it run as a script with our needed context
if __name__ == "__main__":
    main_menu()