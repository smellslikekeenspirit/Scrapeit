#! usr/bin/env python3

import praw

reddit = praw.Reddit(client_id='CqiynT5VPsxU1g',
                     client_secret='L2YlibTaGa6NVb8PKWR8h4hWddU',
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
