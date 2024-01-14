from collections import Counter
import string


def common_word_occurrences(inputA, inputB):
    # Function to preprocess text and remove punctuation
    def preprocess_text(text):
        text = text.lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        return text.split()

    # Preprocess the input texts
    wordsA = preprocess_text(inputA)
    wordsB = preprocess_text(inputB)

    # Find common words and count their occurrences
    common_words = set(wordsA) & set(wordsB)
    occurrencesA = Counter(wordsA)
    occurrencesB = Counter(wordsB)

    # Display results
    print("Common words and their occurrences:")
    for word in common_words:
        print(
            f"{word}: A({occurrencesA[word]} times), B({occurrencesB[word]} times)")


# input_file_name = 'attlassian2.txt'

# all_schemas = {}

# for file in schema_files:
#     opened_file = open(
#         '/Users/ocangoz/Documents/wm_git/LLM testing/7-llm-driven-data-engineering/schemas/' + file, 'r')
#     all_schemas[file] = opened_file.read()

# {all_schemas[input_file_name]}



# Example usage:
inputA = "This is a sample text for testing the function."
inputB = "The function tests whether it finds common words in two texts."
common_word_occurrences(inputA, inputB)
