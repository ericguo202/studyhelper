import random
import sys
import json

# variables
score = 0
num_questions = 0
terms = []

# Function to read the JSON file into a list of dictionaries
def read_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Function to write the list of dicts to a JSON file
def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def add_terms():
    global terms
    terms = read_from_json("terms.json") # converts the terms json file into a list for the script to work with
    print(terms)
    term = input("Term name: ")
    definition = input(f"Definition of {term}: ")

    terms.append({'term': term, 'definition': definition}) # adds to list a dict containing term and definition
    save_to_json(terms, "terms.json") # saves it to the JSON file so there is a record of what terms you have in case you want to access it in the future
    welcome_screen()

def list_terms(): 
    global terms
    terms = read_from_json("terms.json") # converts the terms json file into a list for the script to work with
    if len(terms) == 0:
        print("No terms yet.")
    for term in terms:
        print(f"{term['term']}: {term['definition']}")
    welcome_screen()

def begin_practice():
    global score
    global num_questions
    global terms

    terms = read_from_json("terms.json")
    objects_array = terms
    rand_num = random.randint(0, len(objects_array) - 1)
    print(objects_array[rand_num]['definition'])
    name = input("What is this term? Type 'stop' to exit the program. ")
    if name.lower() == "stop":
        print(f"Your accuracy for this game is {score / num_questions * 100}%. You correctly answered {score} out of {num_questions} questions")
        sys.exit()

    if name.lower() == objects_array[rand_num]['term'].lower(): 
        print("You are correct!")
        score += 1
        num_questions += 1
        print(f"Your accuracy is {score / num_questions * 100}%")
        begin_practice()
    else:
        print(f"Incorrect. The correct answer was {objects_array[rand_num]['term']}")
        num_questions += 1
        print(f"Your accuracy is {score / num_questions * 100}%")
        begin_practice()

def welcome_screen():
    choice = input("To add terms, type 'a'. To view a list of the terms, type 'b'. To begin practice, type 'c'. To delete all terms, type 'd'. To quit, type 'q': ")
    if choice.lower() == "a":
        add_terms()
    elif choice.lower() == "b":
        list_terms()
    elif choice.lower() == "c":
        begin_practice()
    elif choice.lower() == "d":
        save_to_json([], "terms.json")
        global terms
        terms = read_from_json("terms.json")
    elif choice.lower() == "q":
        sys.exit()
    else:
        print("Invalid choice. LOL.")
        sys.exit()


# Example usage
# if __name__ == "__main__":
#     file_path = 'example.csv'  # Replace with your CSV file path
#     objects_array = csv_to_object_array(file_path)

welcome_screen()
# run_program_recursively(objects_array)


