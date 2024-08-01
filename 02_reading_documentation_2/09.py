## 09 - Type Error
tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)

# Type Error raised from attempt to add an integer to a string.
