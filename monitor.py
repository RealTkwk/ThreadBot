import praw
import time
from time import strftime, localtime
from praw import errors


def log(msg):
    print('[{}] ThreadBot: {}'.format(strftime("%H:%M:%S", localtime()), msg))


log('Starting bot.')
with open('bot.cfg', 'r') as f:
    log_info = f.read().splitlines()
    user, password = log_info

agent = 'ClosingThreads247 0.1'

r = praw.Reddit(user_agent=agent)
r.login(user, password, disable_warning=True)

sub = r.get_subreddit('all')

already_done = set()
runs = 0

log('Ready to run. Starting.')

while True:
    comms = praw.helpers.flatten_tree(sub.get_comments(limit=1500))

    for comment in comms:
        if '/THREAD' in comment.body.upper() and comment.id not in already_done:
            try:
                comment.reply(
                    '##**CONGRATULATIONS /u/{}, YOU HAVE KILLED THE THREAD. EVERYONE GET OUT.**\n\n Closing requested'
                    ' by /u/{} \n --- \n ^^^This ^^^is ^^^a ^^^bot. ^^^If ^^^there ^^^are ^^^any ^^^issues, ^^^please'
                    ' ^^^send ^^^a ^^^PM ^^^as ^^^they\'re ^^^checked ^^^regularly.'.format(
                        r.get_info(thing_id=comment.parent_id).author,comment.author))
                already_done.add(comment.id)
                log('Responded to {}'.format(comment.author))
            except errors.RateLimitExceeded as e:
                log(e)
                log('Sleping for 10 minutes.')
                time.sleep(600)

    if runs % 200 == 0:
        log('Still running.')
        already_done.clear()

    runs += 1
    time.sleep(2)
