import re


def extract_hashtags_and_mentions(tweet):

    hashtags = re.findall(r'#\w+', tweet)
    mentions = re.findall(r'@\w+', tweet)

    return hashtags, mentions


tweet_text = "Excited to share my #Python project with @username! #CodingFun #DataScience"
hashtags, mentions = extract_hashtags_and_mentions(tweet_text)


print("Hashtags:", hashtags)
print("Mentions:", mentions)
