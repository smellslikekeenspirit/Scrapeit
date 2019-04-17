#! usr/bin/env python3

import praw
import base64

# We are already supplying the double base64 encoded string.
# The program will just decode it. :)
po = 'VERKWmJHbGlWR0ZIWVRaT1ZtSTRVRXRYVWpob05HaFhaR1JW'
pu = 'UTNGcGVXNVVOVlpRYzNoVk1XYz0='

def encrypted_knowledge(po):
    # Converting string to bytes, base64 accepts bytes like objects only
    popo = po.encode()
    # Double base64 decoding :D / No alt chars required
    popopo = base64.b64decode(base64.b64decode(popo, altchars=None))
    return(popopo.decode())

reddit = praw.Reddit(client_id=encrypted_knowledge(pu),
                     client_secret=encrypted_knowledge(po),
                     user_agent='scrapeit')

def main():
    postCount = 0;
    var = input("Which platform do you want promocodes for? (e.g. Uber, Grubhub): ")
    print("\n")
    for i in range(70):
        print("*", end="")
    print("\nThese are the latest posts in the promocodes subreddit for your query:")
    for i in range(70):
        print("*", end="")
    for submission in reddit.subreddit("promocodes").new():
        if var in submission.title or var.lower() in submission.title or var.capitalize() in submission.title:
            print("\n%d: " % (postCount) + submission.title)
            postCount += 1
        if postCount == 10:
            break

if __name__ == '__main__':
    main()
