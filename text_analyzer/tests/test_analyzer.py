from analyzer import(
    count_lines,
    count_words,
    unique,
    often,
    max_length,
    average, 
    frequency
)

with open("sample_data/text.txt") as file:
    text = file.read()

words = text.split()

def test_count_lines():
    assert count_lines(text)==3 

def test_count_words():
    assert count_words(text) == 7

def test_unique():
    assert unique(words) == 5