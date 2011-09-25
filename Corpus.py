#

import re, nltk, os
from lxml import html

# Looks first for abbreviations and decimals then for words with apostrophes then finishes with plain 
# boring words.
tokenexp = re.compile(r"([A-Za-z0-9]+\.[A-Za-z0-9]+\.?|[A-Za-z0-9-]+'[A-Za-z0-9-]+|[A-Za-z0-9-]+)")

def clean(direc='Docs'):
    """Iterates through files in the specified directory and uses lxml to extract raw text from the element with id 
    'bodyContent' and concatenates the results then writes them to 'corpus.txt'."""

    corpusfile = open('corpus.txt', 'w')
    for filename in os.listdir(direc):
        datafile = open(direc+'/'+filename, 'r')
        corpusfile.write(html.fromstring(datafile.read()).get_element_by_id('bodyContent').text_content())
        datafile.close()
    corpusfile.write('\n')
    corpusfile.close()

def tokenize(filename='corpus.txt'):
    """Uses the re.findall method and the regular expression 'tokenexp' (up the top) to tokenize the given file and 
    return the tokens."""

    infile = open(filename, 'r')
    results = re.findall(tokenexp, infile.read())
    infile.close()
    return results

def lexical_diversity(words):
    """Returns the ration of the number of unique words to the number of words overall as a floating point number
    (unique/normal)."""
    normal = []
    for word in words:
        normal.append(word.lower())
    # Conversion to a set removes all duplicate words.
    return len(set(words))/len(words)