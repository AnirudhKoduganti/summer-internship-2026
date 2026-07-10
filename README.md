# summer-internship-2026

What I built:

I built a book explorer which analyzes five books and gives statistics about each of them. It first loads in popular texts from Project Gutenberg and then cleans out those texts by removing punctuation, stop words, and keeping everything lower case. 

By calling the common_freq(book) method, you will be able to count the top 20 most common words in a book you choose from the five. 

Next, by calling the compare_books(book1, book2) method, you are able to see which two books you choose are the most similar in vocabulary. 

You can also see which book has the largest unique word vocabulary by printing out the length of unique_words(book) function. 

Next, you can calculate and find out which book has the highest word diversity by calling the calculate_word_diversity(book) method. 

Lastly, you can use a search tool which takes a word or phrase and returns the top 3 books where it appears most frequently as well as the number of times in those books it appears. To use this feature, you simply call search("any word", book). 


How to run: 
To run this program you need to call the methods and print out those methods to the console to see the results. For example, if I wanted to see which book has the highest word diveristy, I would print out the following: 

print("Frankenstein:", calculate_word_diversity(frankText))
print("Alice:", calculate_word_diversity(aliceText))
print("Moby Dick:", calculate_word_diversity(mobyText))
print("Pride and Prejudice:", calculate_word_diversity(prideText))
print("Sherlock Holmes:", calculate_word_diversity(sherlockText))

I can then run the code and see based on the results which book has the highest word diversity. I have all the print statements inside my code, so you can delete them and test them yourself. 

3 interesting things: 
I found... 
Moby Dick has the largest unique vocabulary 
Alice has the highest word diversity 
Moby Dick and Pride and Prejudice share the most words in common



