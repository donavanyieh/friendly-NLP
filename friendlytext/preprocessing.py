"""
Module to allow efficient pre-processing of text-based data 
"""

import string
import re
import nltk

try:
    # If not present, download NLTK stopwords.
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

from nltk.corpus import stopwords as nltk_en_stopwords
nltk_stopwords = set(nltk_en_stopwords.words("english"))

def remove_punctuation(s):
    """
    Removes all punctuation
    """
    return s.translate(str.maketrans('', '', string.punctuation))


def replace_digits(s):
    """
    Replaces all digits with whitespace.
    """
    return re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", s)

def remove_url(s):
    """
    Replaces all URLs with whitespace
    URLs: All text that starts with:
    - http://
    - https://
    """
    return re.sub('http[s]?://\S+', '', s)

def remove_hashtags(s):
    """
    Replaces all hashtags with whitespace
    Hashtags are any words that starts with '#'
    """
    return re.sub("#[A-Za-z0-9_]+"," ", s)

def standardize_lowercase(s):
    return s.lower()

def remove_stopwords(s, sw=nltk_stopwords):
    """
    Replaces all NLTK stopwords with whitespace 
    """
    pattern = re.compile(r'\b(' + r'|'.join(set(sw)) + r')\b\s*')
    s = pattern.sub(' ', s)
    return s

t = "this list has many stopwords like that."
print(remove_stopwords(t))




