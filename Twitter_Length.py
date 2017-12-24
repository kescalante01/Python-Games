# Part one:
# Create a variable called tweet and put some text in it
#   maybe something like "Hear Me Code class was so much fun today!"

tweet = "Hear me code class was so much fun today!"
tweet_length = len(tweet)
#Measure the length of that tweet.

print("Good Tweet! It's length is", tweet_length, ". Good job.")

difference = abs(140 - tweet_length)

if tweet_length >= 140:
    print("It's too long! Trim in order to meet the 140 characters", "remove" ,difference)
elif tweet_length <= 140:
    print("You are witty! You have", difference, "characters remaining")


# Part two:
# Adjust the program to say how many characters you have remaining to use, or how many you need to trim by in order to meet the 140 character limit

