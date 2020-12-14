
from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

backup = 'backup' # file where topics and ideas are stored

def get_content() -> dict:
    """
        This function goes through content files (in backup folder)
        backup files have their TOPIC as title and their IDEAS as content, ideas are separated by 2 NEWLINES.
        the return value is a dictionary that has every topic as key, and the topic's respective ideas in an array as value.

        example:
        content = {
            'topic1': [idea1, idea2],
            'topic2': [idea1, idea2],
        }
    """
    content = {}
    topics = os.listdir(os.path.join(os.getcwd(), f'{backup}'))
    for topic in topics:
        topic = topic.replace('.txt', '') # otherwise the extension would be showing in the user interface
        with open(f'{backup}\\{topic}.txt', 'r') as file:
            ideas = file.read().split('\n\n')
        content[topic] = ideas
    return content



@app.route('/', methods=['POST', 'GET'])
def index():
    """
        It's the first page that the user will land on, it allows to browse ideas and add new ones.
        A menu on the left allows the user to navigate the app.
    """
    if request.method == 'POST':
        idea = request.form['idea']
        topic = request.form['topic']

        with open( os.path.join(f'{backup}', f'{topic}.txt'), 'a') as file: # It's better to use os.path.join for better portability
            file.write(idea + '\n\n')

    with open('settings.json', 'r') as file:
        settings = json.loads(file.read())

    content = get_content()
    return render_template('index.html', settings=settings, content=content)

@app.route('/settings', methods=['GET', 'POST'])
def settings():

    with open('settings.json', 'r') as file:
            settings = json.loads(file.read())

    if request.method == 'POST':

        settings["secondary-color"] = request.form.get('color') or settings["secondary-color"]
        settings["dark-mode"] = bool(request.form.get('dark-mode'))

        with open('settings.json', 'w') as file:
            file.write( json.dumps(settings) )

    return render_template('settings.html', settings=settings)


app.run('0.0.0.0', 80, True)



# rgb(87, 121, 184)

