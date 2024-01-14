import json
from collections import Counter
import string


def lambda_handler(event, context):
    # Extract inputs from the event
    inputA = event.get('inputA', '')
    inputB = event.get('inputB', '')

    # Function to preprocess text and remove punctuation
    def preprocess_text(text): return text.lower().translate(
        str.maketrans("", "", string.punctuation)).split()

    # Preprocess the input texts
    wordsA = preprocess_text(inputA)
    wordsB = preprocess_text(inputB)

    # Find common words and count their occurrences
    common_words = set(wordsA) & set(wordsB)
    occurrencesA = Counter(wordsA)
    occurrencesB = Counter(wordsB)

    result_list = []

    for word in common_words:
        result_list.append(
            f"{word}: Resume ({occurrencesA.get(word, 0)} times), Job Description ({occurrencesB.get(word, 0)} times)"
        )

    # Join the list elements with newline characters and print as a single string
    result_string = "\n".join(result_list)

    # Return result as JSON
    return {
        'statusCode': 200,
        'body': json.dumps('Your result is ' + str(result_list))

    }

    # # Prepare result
    # resultString = "\n".join([
    # f"{word}: Resume ({occurrencesA.get(word, 0)} times), Job Description ({occurrencesB.get(word, 0)} times)"
    # for word in common_words
    # ])

    # resultStringFinal = resultString.split('\n')

    # # Return result as JSON
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Your result is ' + str(resultStringFinal))

    # }
