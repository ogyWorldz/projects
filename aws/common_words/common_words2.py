from collections import Counter
import re


def compare_texts(inputA, inputB):
    # Convert inputs to lowercase and split into words
    wordsA = re.findall(r'\b\w+\b', inputA.lower())
    wordsB = re.findall(r'\b\w+\b', inputB.lower())

    # Count the occurrences of each word in both inputs
    word_count_A = Counter(wordsA)
    word_count_B = Counter(wordsB)

    # Find common words and their frequencies
    common_words = set(wordsA) & set(wordsB)
    common_word_frequencies_A = {
        word: word_count_A[word] for word in common_words}
    common_word_frequencies_B = {
        word: word_count_B[word] for word in common_words}

    # Sort the common words by frequency in descending order
    sorted_common_words_A = sorted(
        common_word_frequencies_A.items(), key=lambda x: x[1], reverse=True)
    sorted_common_words_B = sorted(
        common_word_frequencies_B.items(), key=lambda x: x[1], reverse=True)

    # Calculate the percentage of words in inputA compared to inputB
    percentage_A_vs_B = (len(wordsA) / len(wordsB)) * 100

    # Print the results
    print("Common words and their frequencies in inputA:")
    for word, frequency in sorted_common_words_A:
        print(f"{word}: {frequency} times")

    print("\nCommon words and their frequencies in inputB:")
    for word, frequency in sorted_common_words_B:
        print(f"{word}: {frequency} times")

    print(
        f"\nPercentage of words in inputA compared to inputB: {percentage_A_vs_B:.2f}%")


# Example usage:
inputA = "This is a sample text with some common words."
inputB = "Another text with common words and additional content."
compare_texts(inputA, inputB)
