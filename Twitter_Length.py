# Part one:
# Create a variable called tweet and put some text in it
#   maybe something like "Hear Me Code class was so much fun today!"

tweet = input("Enter your tweet here: ")
tweet_length = len(tweet)
#Measure the length of that tweet.

print("Good Tweet! It's length is", tweet_length, ". Good job.")
tweet_limit = 10
difference = abs(tweet_limit - tweet_length)

if tweet_length > tweet_limit:
    print("It's too long! Trim in order to meet the 140 characters", "remove" ,difference)
elif tweet_length < tweet_limit:
    print("You are witty! You have", difference, "characters remaining")
elif tweet_length == tweet_limit:
    print("This is at the limit at ", tweet_limit)


# Part two:
# Adjust the program to say how many characters you have remaining to use, or how many you need to trim by in order to meet the 140 character limit

# Part three:
# Twitter announced they are changing their character limit to 280, but they might change it again.
# Can you make your code flexible enough so that you don't have to replace the character limit in multiple places in your code?

