# display_results.py

def display_matching_words(matching_words):
    """
    Displays the list of matching words to the user.
    """
    if matching_words:
        print("Potential Wordle solutions based on your guess:")
        for word in matching_words:
            print(word)
    else:
        print("No matching words found.")
