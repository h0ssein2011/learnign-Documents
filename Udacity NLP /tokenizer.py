"""Splitting text data into tokens."""

import re


def sent_tokenize(text):
    """Split text into sentences."""

    # TODO: Split text by sentence delimiters (remove delimiters)
    text = text.split()
    # TODO: Remove leading and trailing spaces from each sentence
    text_list = [word.strip() for word in text]
    pass  # TODO: Return a list of sentences (remove blank strings)
    return list(filter(None, text_list))


def word_tokenize(sent):
    """Split a sentence into words."""

    # TODO: Split sent by word delimiters (remove delimiters)
    sent = sent.split(' ')
    # TODO: Remove leading and trailing spaces from each word
    sent_list = [se.strip() for se in sent]
    pass  # TODO: Return a list of words (remove blank strings)
    return list(filter(None, sent_list))


def test_run():
    """Called on Test Run."""

    text = "The first time you see The Second Renaissance it may look boring. Look at it at least twice and definitely watch part 2. It will change your view of the matrix. Are the human people the ones who started the war? Is AI a bad thing?"
    print("--- Sample text ---", text, sep="\n")

    sentences = sent_tokenize(text)
    print("\n--- Sentences ---")
    print(sentences)

    print("\n--- Words ---")
    for sent in sentences:
        print(sent)
        print(word_tokenize(sent))
        print()  # blank line for readability


test_run()


x = -120
print(str(x).reverse())
