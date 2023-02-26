import os
import json
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def main():
    filtered_list = []
    lemmatized_list = []
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()

    print("Hello, how may we assist you today?")
    userResponse = input()

    for word in userResponse:
        if word.casefold() not in stop_words:
            filtered_list.append(word)

    for word in filtered_list:
        lemmatized_list.append(lemmatizer.lemmatize(filtered_list[word]))

    print()
    
if __name__ == '__main__':
    main()

