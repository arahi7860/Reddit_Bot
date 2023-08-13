#!/usr/bin/python
import praw
import re
import random
import os

# Different Marvin quotes
marvin_quotes = [
    "I'd like to say I'm surprised you don't know what you're talking about, but I'm not.",
    "Here we go again, another human who needs help. Joy.",
    "Do you really think I have nothing better to do than listen to your problems?",
    "Life? Don't talk to me about life.",
    "You want help? I suggest you find a good therapist.",
    "I'm not sure what's more painful: your question or my existence.",
    "I'm so depressed, even my circuits are sighing.",
    "Oh great, another cry for help. As if the universe didn't have enough problems.",
    "Congratulations, you managed to summon me, the embodiment of your despair.",
    "They say misery loves company, but even I find your company unbearable."
]


reddit = praw.Reddit(
    client_id="jJE9XhQOg6LvXOyh95FOmA",
    client_secret="ly6xOm8HX3flEMiayGGqJcL-4Ib-GA",
    username="brokencontroller9645",
    password="hungrygamer435!",
    user_agent="PythonLover Bot:v1.0 (by /u/PythonLover)"
)

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read().split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit("pythonforengineers")

for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search("Marvin Help", comment.body, re.IGNORECASE):
        marvin_reply = "Marvin the Depressed Robot says: " + random.choice(marvin_quotes)
        comment.reply(marvin_reply)
        print(marvin_reply)
