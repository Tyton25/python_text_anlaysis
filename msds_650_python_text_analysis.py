import operator, time, string
import re
from collections import defaultdict
import nltk
# nltk.download('gutenberg')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.corpus import gutenberg

FOLDER = 'C:\\Users\\tyben\\Documents\\Regis\\MSDS_653\\week6\\'
STOP = stopwords.words('english')
REMOVE_LIST = ['gutenberg',
               'ebook',
               'www',
               'online']
LONG_WORDS_REGEX = r'\w{14,}'


def main():
    copperfield = open(FOLDER + 'david_copperfield.txt', 'r').read()
    frankenstein = open(FOLDER + 'frankenstein.txt', 'r').read()
    copper = re.split(r'\W+', copperfield.lower())
    frank = re.split(r'\W+', frankenstein.lower())
    # print("First 50 words for David Copperfield:\n{}\n".format(copper[:50]))
    # print("First 50 words for Frankenstein:\n{}".format(frank[:50]))

    copper = [j for j in copper if j not in STOP]
    frank = [j for j in frank if j not in STOP]

    copper = [j for j in copper if j not in REMOVE_LIST]
    frank = [j for j in frank if j not in REMOVE_LIST]
    print("David Copperfield removed list:\n{}\n".format(copper[:50]))
    print("Frankenstein removed list:\n{}".format(frank[:50]))

    sorted_new_copper = get_sorted_words(copper)
    sorted_new_frank = get_sorted_words(frank)
    copper_words = most_popular_words(sorted_new_copper)
    frank_words = most_popular_words(sorted_new_frank)

    # Create list of common words used the most in each novel
    common_words = [w for w in copper_words if w in frank_words]
    print(common_words)

    # Words with over 14 letters in Frankenstein
    longest_frank_words = get_longest_words(frank)

    # Words with over 14 letters in David Copperfield
    longest_copper_words = get_longest_words(copper)
    print("Total long words for David Copperfield: {}".format(len(longest_copper_words)))
    print("Total long words for Frankenstein: {}".format(len(longest_frank_words)))

    # Print common words having at least 14 letters
    common_long_words = [w for w in longest_copper_words if w in longest_frank_words]
    print("Total long words in common for David Copperfield and Frankenstein: {}".format(len(common_long_words)))

    # Write longest popular words and longest words to files
    write_to_file('common_long_words.txt', common_long_words)
    write_to_file('david_copperfield_popular_words.txt', copper_words)
    write_to_file('frankenstein_popular_words.txt', frank_words)


def write_to_file(filename, input_list):
    output_filename = FOLDER + filename
    with open(output_filename, 'w') as f:
        for row in input_list:
            print(row)
            f.write(row + "\n")


def most_popular_words(book):
    npopular = 25
    x = range(npopular)
    y = []
    for pair in range(npopular):
        y = y + [book[pair][0]]
        print(book[pair])
    return list(y)


def get_sorted_words(book):
    new_book = {}
    for word in book:
        if word in new_book:
            new_book[word] += 1
        else:
            new_book[word] = 1
    sorted_new_book = sorted(new_book.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_new_book


def get_longest_words(words):
    long_words = re.compile(LONG_WORDS_REGEX, re.IGNORECASE)
    longest_words = [c for c in words if long_words.match(c)]
    longest_words = list(set(longest_words))
    longest_words.sort()
    for w in longest_words:
        print(w)
    return longest_words


if __name__ == '__main__':
    main()
