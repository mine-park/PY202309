import os, re
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def calculate_word_frequency(words):
    word_frequency = {} # dictionary for saving words
    for word in words:
        # If the word does not exist, assign the value 1 / If it exists, Increment the current frequency by 1.
        word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency

def get_word_frequency(quotes):
    all_text = ' '.join(quote.get_text() for quote in quotes) # separated by spaces.
    # The regular expression \b\w+\b is used to extract words that are at word boundaries / converts all text to lowercase.
    words = re.findall(r'\b\w+\b', all_text.lower())
    return calculate_word_frequency(words) # return dictionary containing the frequency of each word

url = 'https://quotes.toscrape.com/tag/life/'
html = ur.urlopen(url)
soup = bs(html.read(), 'html.parser')
quotes = soup.find_all('div', {"class": "quote"})

# calculate words frequencies
all_words = []
for quote in quotes:
    quote_texts = quote.find_all('span', {"class": "text"}) # Find elements in quotes where the class is 'text'
    for quote_text in quote_texts:
        words = re.findall(r'\b\w+\b', quote_text.get_text().lower())
        all_words.extend(words) # Add the words of the current quote to the overall list of words
word_frequency = calculate_word_frequency(all_words) # Use a function to calculate the frequency

# Print the top 5 words and their frequencies
top_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)[:5] # Return key-value pairs / Sort in descending order based on frequency
print("< Top 5 Words and Frequencies >")
for word, frequency in top_words: # Print the top 5 words and their frequencies
    print(f"{word}: {frequency}")