# load texts 

with open("books/frankenstein.txt", "r", encoding="utf-8") as file: 
    frankText = file.read()

with open("books/alice.txt", "r", encoding="utf-8") as file: 
    aliceText = file.read()

with open("books/moby.txt", "r", encoding="utf-8") as file:
    mobyText = file.read()

with open("books/prideandprejudice.txt", "r", encoding="utf-8") as file:
    prideText = file.read()

with open("books/sherlock.txt", "r", encoding="utf-8") as file:
    sherlockText = file.read() 

stop_words = {
    "a", "about", "above", "after", "again", "against", "all", "am",
    "an", "and", "any", "are", "as", "at", "be", "because", "been",
    "before", "being", "below", "between", "both", "but", "by",
    "can", "could", "did", "do", "does", "doing", "down", "during",
    "each", "few", "for", "from", "further", "had", "has", "have",
    "having", "he", "her", "here", "hers", "herself", "him",
    "himself", "his", "how", "i", "if", "in", "into", "is", "it",
    "its", "itself", "just", "me", "more", "most", "my", "myself",
    "no", "nor", "not", "now", "of", "off", "on", "once", "only",
    "or", "other", "our", "ours", "ourselves", "out", "over", "own",
    "same", "she", "should", "so", "some", "such", "than", "that",
    "the", "their", "theirs", "them", "themselves", "then", "there",
    "these", "they", "this", "those", "through", "to", "too", "under",
    "until", "up", "very", "was", "we", "were", "what", "when",
    "where", "which", "while", "who", "whom", "why", "will", "with",
    "would", "you", "your", "yours", "yourself", "yourselves", "said", 
    "mr", "mrs", "one", "two", "last", "ye", "upon", "now", "yet", "come",
    "never", "must", "shall", "may", "might", "must", "could", "would",
    "see"
} 

books = {
        "Frankenstein": frankText, 
        "Alice": aliceText, 
        "Moby Dick": mobyText, 
        "Pride and Prejudice": prideText,
        "Sherlock Holmes": sherlockText
    }

def clean_text(book):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    lower = book.lower()
    
    lower = lower.split() 

    for word in range(len(lower)):
        for char in punctuation:
            lower[word] = lower[word].replace(char, "")

    for word in range(len(lower)):
        for stop_word in stop_words:
            if lower[word] == stop_word:
                lower[word] = ""

    cleaned_text = [] 
    for word in lower:
        if word != "":
            cleaned_text.append(word)

    return cleaned_text 


def word_freq(book):
    cleaned_text = clean_text(book)
    word_count = {}

    for word in cleaned_text:
        if word in word_count: 
            word_count[word] += 1  
        else:
            word_count[word] = 1 

    word_count = dict(sorted(word_count.items(), key = lambda item: item[1], reverse = True))

    return word_count


def common_freq(book):
    word_count = word_freq(book)

    common_words = {}
    counter = 0
    for word, count in word_count.items():
        common_words[word] = count
        counter += 1

        if(counter == 20):
            break

    return common_words



# similar means which two books have the most unique words in common 
def unique_words(book):
    word_count = word_freq(book)

    unique_words = set()

    for word in word_count: 
        unique_words.add(word)

    return unique_words 

def compare_books(book1, book2):
    unique_words1 = unique_words(book1)
    unique_words2 = unique_words(book2)

    shared = 0

    for word in unique_words1:
        if word in unique_words2:
            shared += 1

    return shared


def calculate_word_diversity(book):
    unique = unique_words(book)
    total_words = len(clean_text(book))

    word_diversity = len(unique) / total_words

    return word_diversity 

def search(query, books):

    query = query.lower()

    results = {}

    for title, text in books.items():
        results[title] = text.lower().count(query)

    results = dict(sorted(results.items(), key = lambda item: item[1], reverse = True))

    top = {}

    counter = 0

    for title, count in results.items():
        top[title] = count
        counter += 1

        if(counter == 3): 
            break 

    return top 

# after checking every pair, Moby Dick and Pride and Prejudice share the most words in common

print("Frankenstein vs Alice:", compare_books(frankText, aliceText), " shared words")
print("Frankenstein vs Moby Dick:", compare_books(frankText, mobyText), " shared words")
print("Frankenstein vs Pride and Prejudice:", compare_books(frankText, prideText), " shared words")
print("Frankenstein vs Sherlock Holmes:", compare_books(frankText, sherlockText), " shared words")

print("Alice vs Moby Dick:", compare_books(aliceText, mobyText), " shared words")
print("Alice vs Pride and Prejudice:", compare_books(aliceText, prideText), " shared words")
print("Alice vs Sherlock Holmes:", compare_books(aliceText, sherlockText), " shared words")

print("Moby Dick vs Pride and Prejudice:", compare_books(mobyText, prideText), " shared words")
print("Moby Dick vs Sherlock Holmes:", compare_books(mobyText, sherlockText), " shared words")

print("Pride and Prejudice vs Sherlock Holmes:", compare_books(prideText, sherlockText), " shared words")


# moby dick has the most unique words 
print("Frankenstein:", len(unique_words(frankText)), " unique words")
print("Alice:", len(unique_words(aliceText)), " unique words")
print("Moby Dick:", len(unique_words(mobyText)), " unique words")
print("Pride and Prejudice:", len(unique_words(prideText)), " unique words")
print("Sherlock Holmes:", len(unique_words(sherlockText)), " unique words")

# Alice has the highest word diversity 
print("Frankenstein:", calculate_word_diversity(frankText))
print("Alice:", calculate_word_diversity(aliceText))
print("Moby Dick:", calculate_word_diversity(mobyText))
print("Pride and Prejudice:", calculate_word_diversity(prideText))
print("Sherlock Holmes:", calculate_word_diversity(sherlockText))



print(search("love", books))
print(search("young man", books))