# twitter Racial Slur Tweets Detection
A program that can indicate the degree of profanity for each sentence in the file. Write in python program that detects racial slur in twitter tweets.

# Problem Statement
Do read the following blog post before answering the questions https://medium.com/affinityanswers-tech/recruitment-how-not-to-answer-our-take-home-questions-57153d143447 Imagine there is a file full of Twitter tweets by various users and you are provided a set of words that indicates racial slurs. Write a program that can indicate the degree of profanity for each sentence in the file. Write in any programming language (preferably in Python) - make any assumptions, but remember to state them. Please place the code in GitHub with proper documentation and share.

# Possible Solution
One way to approach this problem is to create a Python program that reads in the file of Twitter tweets and the set of words indicating racial slurs. You can assume that the tweets are stored in a text file, with each tweet on a separate line. You can also assume that the set of words indicating racial slurs is provided in a separate file or as a list of words in the program.

The program can then iterate over each tweet and compare each word in the tweet with the set of words indicating racial slurs. If a racial slur is found in the tweet, the degree of profanity for that tweet can be incremented by a certain amount. The amount of increment can be based on how offensive the word is. For example, more offensive words can be assigned a higher increment than less offensive words.

Once the program has processed all the tweets, it can output the degree of profanity for each tweet. The degree of profanity can be a numerical value or a category, such as low, medium, or high.

# Program Logic
In this example code, we first define a set of words indicating racial slurs. We then read in a file of Twitter tweets using a with statement that automatically closes the file when we are done. We define a function called calculate_profanity that takes a tweet as input and calculates the degree of profanity based on the number of racial slurs in the tweet. We use a regular expression to split the tweet into words and then count the number of racial slurs using a list comprehension. Finally, we use if-else statements to categorize the degree of profanity based on the number of racial slurs. We then call this function for each tweet in the file and print out the result.

Note that this is just an example code and you may need to modify it depending on your specific requirements. Additionally, you should make sure to test the code thoroughly and handle any errors or edge cases that may arise.

# Screenshots
# tweets.txt
![image](https://user-images.githubusercontent.com/81423983/219327245-23525c1f-d75a-47b6-ac15-18dc649275bc.png)
# Program Output
![image](https://user-images.githubusercontent.com/81423983/219327403-d9095d46-1c87-4914-94e6-603a3c6fe494.png)
