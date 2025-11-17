# 1-import the random module
import random
# 2- create subjects
subjects=[
    "Shahrukh khan", "Virat kohli","Nirmala Sitharaman","A mumbai cat","A group of monkeys","Prime minister Modi","Auto rickshaw driver from dehli"
]
actions=[
    "launches","cancels","dances with","eats","declares war on","orders","celebrates"
]
places_or_things=[
    "at red fort","in mumbai local train","a plate of samosa","inside parliament","at ganga ghat","during ipl"
]
# 3- start the head line genearation loop
while True:
    subject =random.choice(subjects)
    action = random.choice(actions)

    place_or_thing= random.choice(places_or_things)
    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)
    

    user_input =input("\nDo you want another headline? (yes/no)".strip().lower())
    if user_input !="yes":
        break

# print goodbye
print("Goodbye! Thank you for using the fake news headline generator.")