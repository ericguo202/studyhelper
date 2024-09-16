import csv
import random
import sys

# Function to convert CSV file to an array of objects (dictionaries)
def csv_to_object_array(file_path):
    objects_array = []

    # Open the CSV file
    with open(file_path, mode='r') as file:
        # Create a CSV DictReader to read the file
        csv_reader = csv.DictReader(file)

        # Convert each row into a dictionary and add it to the array
        for row in csv_reader:
            print(row)
            objects_array.append(row)

    return objects_array

score = 0
num_questions = 0

def run_program_recursively(objects_array):
    global score
    global num_questions

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
        run_program_recursively(objects_array)
    else:
        print(f"Incorrect. The correct answer was {objects_array[rand_num]['term']}")
        num_questions += 1
        print(f"Your accuracy is {score / num_questions * 100}%")
        run_program_recursively(objects_array)

# Example usage
if __name__ == "__main__":
    file_path = 'example.csv'  # Replace with your CSV file path
    objects_array = csv_to_object_array(file_path)

    run_program_recursively(objects_array)


