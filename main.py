
from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

backup = 'backup' # file where topics and ideas are stored

def get_content():
    content = {}
    topics = os.listdir(os.path.join(os.getcwd(), f'{backup}'))
    for topic in topics:
        topic = topic.replace('.txt', '')
        with open(f'{backup}\\{topic}.txt', 'r') as file:
            ideas = file.read().split('\n\n')
        content[topic] = ideas
    return content

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        idea = request.form['idea']
        topic = request.form['topic']

        with open(f'{backup}\\{topic}.txt', 'a') as file:
            file.write(idea + '\n\n')

    with open('settings.json', 'r') as file:
        settings = json.loads(file.read())

    content = get_content()

    return render_template('index.html', settings=settings, content=content)


app.run('0.0.0.0', 80, True)







# POPULATE JSON FILES:
# User.settings({
#     'username': 'nagakabourous',
#     'password': '1UPPER1lower1digit.',
#     'name': 'Reda',
#     'profile-image': 'thee.jpg',
#     'dark-mode': False,
#     'secondary-color': 'rgb(55, 109, 42)'
# })

# with open('topics.json', 'w') as file:
#     file.write( json.dumps(
#     {
#     'topic1': ['idea1','idea2','idea3','idea4'],
#     'topic2': ['idea1','idea2','idea3','idea4'],
#     }
# ))



