import json
from difflib import get_close_matches

data = json.load(open("data_source/data.json"))
# print(data)

def translate(word):
    # parse input into lower case before it checks on data
    word = word.lower()
    if word in data:
        return data[word]

    # Get similar words
    elif len(get_close_matches(word, data.keys())) > 0:
        # string format %s will be replaced by var at the end
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "Invalid entry."

    else:
        return "The word doesn't exist. Please double check it."

input_word = input("Enter word: ")

# store output.
output = translate(input_word)

# remove the list braces '[]'.
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output) # if it's a string