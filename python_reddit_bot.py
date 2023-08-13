import praw
import re
import os

# Configure PRAW with your Reddit application's new credentials
reddit = praw.Reddit(
    client_id="jJE9XhQOg6LvXOyh95FOmA",
    client_secret="ly6xOm8HX3flEMiayGGqJcL-4Ib-GA",
    username="brokencontroller9645",
    password="hungrygamer435!",
    user_agent="PythonLover Bot:v1.0 (by /u/PythonLover)"
)

# Check for Existing Replied Posts
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read().split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# Access Subreddit
subreddit = reddit.subreddit('pythonforengineers')

# Your bot's logic comes after the PRAW configuration
for submission in subreddit.new(limit=5):
    if submission.id not in posts_replied_to:
        if "I love Python" in submission.title:
            submission.reply("Me too!")
            print("Bot replying to:", submission.title)
            posts_replied_to.append(submission.id)
            with open("posts_replied_to.txt", "w") as f:
                for post_id in posts_replied_to:
                    f.write(post_id + "\n")

for comment in subreddit.comments(limit=5):
    if "I hate Python" in comment.body:
        comment.reply("Sorry to hear that! If you need help, feel free to ask at /r/learnpython.")
        print("Bot replying to comment:", comment.body)
