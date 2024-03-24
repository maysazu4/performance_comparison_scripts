import time
import read_file as r
from draw_results import *

# Function to count word occurrences using a dictionary
def count_word_occurance_dict(text):
    """Counts the occurrences of each word in the text using a dictionary.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary where keys are words and values are their respective counts.
    """
    word_count = {}
    for word in text.split():
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# Function to count word occurrences by sorting the words first
def count_word_occurance_sorted(text):
    """Counts the occurrences of each word in the text by sorting the words first.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary where keys are words and values are their respective counts.
    """
    sorted_words = sorted(text.split())
    word_count = {}
    curr_word = None
    for word in sorted_words:
        if word != curr_word:
            word_count[word] = 1
            curr_word = word
        else:
            word_count[word] += 1
    return word_count

# Function to calculate execution time of word occurrence counting
def calculate_results(text, func):
    """Calculates the time taken to count word occurrences using the specified function.

    Args:
        text (str): The input text.
        func (function): The word occurrence counting function to be used.

    Returns:
        float: The total execution time in seconds.
    """
    start_time = time.perf_counter()
    func(text)
    end_time = time.perf_counter()
    total_time = round(end_time - start_time, 2)
    return total_time

if __name__ == "__main__":
    number = 1
    results1 = []
    results2 = []

    # Iterate through 7 different orders of magnitude (from 1 to 10000000)
    for i in range(7):
        number = number * 10
        filename = str(number) + ".txt"
        print(filename)
        # Read text from file
        text = r.read_file_into_string('texts/' + filename)
        # Calculate execution time for counting word occurrences using sorting
        time1 = calculate_results(text, count_word_occurance_sorted)
        results1.append((number, time1))
        # Calculate execution time for counting word occurrences using dictionaries
        time2 = calculate_results(text, count_word_occurance_dict)
        results2.append((number, time2))

    # Draw comparison graphs and save results to a CSV file
    draw_results(results1, results2, 'sorted count', 'dictionary count', 'count_word_occurance.csv')