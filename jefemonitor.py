import random
import praw
import time
from time import strftime, localtime
from praw import errors


def log(msg):
    print('[{}] JefeEstatalBot: {}'.format(strftime("%H:%M:%S", localtime()), msg))


log('Starting bot.')
with open('jefebot.cfg', 'r') as f:
    log_info = f.read().splitlines()
    user, password = log_info

agent = 'JefeEstatal 0.1'

r = praw.Reddit(user_agent=agent)
r.login(user, password, disable_warning=True)

sub = r.get_subreddit('Argentina')

already_done = set()
runs = 0

log('Ready to run. Starting.')

felicitaciones = ['Buen trabajo compa!', 'Siga asi.', 'Excelente como siempre.',
                  'Nestor estaria orgulloso de su trabajo.',
                  'Muy buen trabajo honesto, como buen peronista.', 'Gracias por el trabajo duro cumpa!',
                  'Muy bien, no deje que los medios online se lleven nuestra plata.',
                  'Si sigue asi la proxima el bombo lo toca usted.',
                  'El general una vez dijo:\n\n >"Una de las cosas mas dificiles de la tarea de gobernar es '
                  'encontrar a los hombres con capacidad para realizarla."\n\n Usted lo pondria orgulloso']

while True:
    comms = praw.helpers.flatten_tree(sub.get_comments(limit=100))

    for comment in comms:
        if '{}'.format(comment.author).upper() == 'EMPLEADOESTATALBOT' and comment.id not in already_done and '(Hecho en China.)' in comment.body:
            try:
                comment.reply('{}'.format(random.choice(felicitaciones)))
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
    time.sleep(10)
