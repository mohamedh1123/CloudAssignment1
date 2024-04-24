import nltk
from nltk.corpus import stopwords
from collections import Counter
import string



nltk.download('stopwords')
nltk.download('punkt')


stop_words = set(stopwords.words('english'))


def process_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

   
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()


    words = nltk.word_tokenize(text)


    filtered_words = [word for word in words if word not in stop_words]

   
    word_counts = Counter(filtered_words)

    return word_counts


if __name__ == '__main__':
    file_path = 'random_paragraphs.txt'
    frequencies = process_text(file_path)
    for word, count in frequencies.items():
        print(f'{word}: {count}')

