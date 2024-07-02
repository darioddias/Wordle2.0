# matching_algorithm.py

def find_matching_words(guess, answers):
    """
    Finds words from the answers list that match the criteria based on the user's guess.
    Returns a list of matching words.
    """
    matching_words = []
    for word in answers:
        if len(word) == 5 and len(set(word)) == 5:  # Assuming answers are valid 5-letter words with unique letters
            if all(guess[i] == word[i] for i in range(5)):
                matching_words.append(word)
    return matching_words
