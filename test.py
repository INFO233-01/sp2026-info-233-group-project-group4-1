# test_part1.py
import dating_profile

# this tests the age 
print("testing validate_age")
result = dating_profile.validate_age("25")
print(result)

result = dating_profile.validate_age("abc")
print(result)

result = dating_profile.validate_age("10")
print(result)

result = dating_profile.validate_age("200")
print(result)

# tests the name
print("testing validate_name")
result = dating_profile.validate_name("Alex")
print(result)

result = dating_profile.validate_name("")
print(result)

# test tests bio
print("testing validate_bio")
result = dating_profile.validate_bio("I like hiking")
print(result)

result = dating_profile.validate_bio("")
print(result)

# tests the profile 
print("testing create_profile")
my_profile = dating_profile.create_profile()
dating_profile.display_profile(my_profile)

import dating_profile
from random_profiles import get_random_users