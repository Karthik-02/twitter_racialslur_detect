import re

# define the set of words indicating racial slurs
racial_slurs = {'nigger', 'chink', 'spic', 'kike', 'wetback','black'}

# read the file of Twitter tweets
with open('tweets.txt', 'r') as f:
    tweets = f.readlines()

# define a function to calculate the degree of profanity for a tweet
def calculate_profanity(tweet):
    # split the tweet into words
    words = re.findall(r'\w+', tweet)
    # count the number of racial slurs in the tweet
    num_racial_slurs = sum([1 for word in words if word.lower() in racial_slurs])
    # calculate the degree of profanity based on the number of racial slurs
    if num_racial_slurs == 0:
        profanity = 'Low'
    elif num_racial_slurs <= 2:
        profanity = 'Medium'
    else:
        profanity = 'High'
    return profanity

# calculate the degree of profanity for each tweet
for tweet in tweets:
    profanity = calculate_profanity(tweet)
    print(tweet.strip() + ': ' + profanity)
