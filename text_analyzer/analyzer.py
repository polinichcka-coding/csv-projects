def count_lines(text):
    return len(text.splitlines())

def count_words(text):
    return len(text.split())

def unique(words):
    return len(set(words))

def often(words):
    o={}
    for word in words:
        if word in o:
            o[word]+=1
        else:
            o[word]=1
    result=sorted(o.items(), key=lambda x: x[1], reverse=True)[0]
    return result

def max_length(words):
    return max(words, key=len)

def average(words):
    i=0
    for word in words:
        i+=len(word)
    return i/len(words)

def frequency(words):
    char_freq = {}
    for word in words:
        for c in word:
            if c in char_freq:
                char_freq[c]+=1
            else:
                char_freq[c]=1

    result=sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
    return result


with open("sample_data/text.txt") as file:
    text = file.read()

words=text.split()
print(f"Lines: {count_lines(text)}")
print(f"Words: {count_words(text)}")
print(f"Unique words: {unique(words)}")
print(f"Most frequent word: {often(words)}")
print(f"Longest word: {max_length(words)}")
print(f"Average word length: {average(words):.2f}")
