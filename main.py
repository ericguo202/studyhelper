import random
import sys
import json
import os
import platform

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

# Functions to add terms to the list
def add_terms():
    global terms
    terms = read_from_json("terms.json") # converts the terms json file into a list for the script to work with
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
        print(f"{term['term']}: {term['definition']}", "\n --------------------------------")
    welcome_screen()

def write_mode(objects_array): # simulated quizlet write mode
    global score
    global num_questions
    rand_num = random.randint(0, len(objects_array) - 1)
    print(objects_array[rand_num]['definition'])
    name = input("What is this term? Type 'stop' to exit the program. ")
    if name.lower() == "stop":
        print(f"Your accuracy for this game is {score / num_questions * 100}%. You correctly answered {score} out of {num_questions} questions")
        sys.exit()

    clear_console() # improve UI
    if name.lower() == objects_array[rand_num]['term'].lower(): 
        print("You are correct!")
        score += 1
        num_questions += 1
        print(f"Your accuracy is {score / num_questions * 100}% \n")
        begin_practice()
    else:
        print(f"Incorrect. The correct answer was {objects_array[rand_num]['term']}")
        num_questions += 1
        print(f"Your accuracy is {score / num_questions * 100}% \n")
        begin_practice()

def get_random_choice(objects_array, index1, index2, index3): # necessary for MCQ portion
    # print(f"The first index is {index1}")
    # print(f"The 2nd index is {index2}")
    # print(f"The 3rd index is {index3}")
    rand = random.randint(0, len(objects_array) - 1)
    # print(f"the random index we got is {rand}")
    if ((rand != index1) and (rand != index2) and (rand != index3)): # checks for duplicate indices
        # print(rand)
        return rand
    else: # if there is a duplicate index
        # print(f"Duplicated index {rand}")
        return get_random_choice(objects_array, index1, index2, index3)

# prompts user for choice and finds matching answer
def get_matching_answer(answers_list): 
    choice = input("(Press q to quit) Which letter choice is correct? ")

    for answer in answers_list:
        if answer['index'] == choice.lower():
            return answer
        if choice.lower() == "q":
            sys.exit()
        
    return get_matching_answer(answers_list)

def multiple_choice(objects_array): # simulates quizlet MCQ
    global score
    global num_questions
    rand_num = random.randint(0, len(objects_array) - 1)
    print(objects_array[rand_num]['term'])
    # MCQ randomness logic here
    # step 1: correct definition
    correct_def = objects_array[rand_num]['definition']
    # step 2: get incorrect answers
    wrong_index1 = get_random_choice(objects_array, rand_num, -1, -1)
    wrong_index2 = get_random_choice(objects_array, rand_num, wrong_index1, -1)
    wrong_index3 = get_random_choice(objects_array, rand_num, wrong_index1, wrong_index2)

    answers = [{'correct': True, 'answer': correct_def}, {'correct': False, 'answer': objects_array[wrong_index1]['definition']}, {'correct': False, 'answer': objects_array[wrong_index2]['definition']}, {'correct': False, 'answer': objects_array[wrong_index3]['definition']}]
    # shuffles the answers so the correct one will appear at a random index
    random.shuffle(answers)
    new_answers = [] # new list for making choosing easier - abcd method
    new_answers.append({'index': 'a', **answers[0]}) 
    new_answers.append({'index': 'b', **answers[1]})
    new_answers.append({'index': 'c', **answers[2]})
    new_answers.append({'index': 'd', **answers[3]})
    for answer in new_answers:
        print(f"{answer['index']}). {answer['answer']}")

    # checks if choice is correct
    if get_matching_answer(new_answers)['correct'] == True: 
        score += 1 # only if right answer
        clear_console() # improve UI
        print("Correct!")
    else:
        clear_console() # improve UI
        print(f"Incorrect. The correct answer was {correct_def}")

    num_questions +=1 # basically catch all
    print(f"Your accuracy is {score / num_questions * 100}% \n")
    begin_practice()

# clears console for better UI
def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    if platform.system() == "Darwin" or platform.system() == "Linux": # Darwin is MacOS
        os.system("clear")

def begin_practice():
    global terms
    terms = read_from_json("terms.json")

    if len(terms) >= 4:
        num = random.randint(0, 1)
        if num == 1:
            write_mode(terms)
        else:
            multiple_choice(terms)
    else:
        write_mode(terms)
    

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


