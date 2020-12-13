
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pass #

    user = User.login(
        'nagakabourous',
        '1UPPER1lower1digit.'
    )
    return render_template('index.html', user=user)

# how to deny access to subdirectories in flask?

class User:
    def __init__(self, name, topics, username, password, profile_image='thee.jpg') -> object:
        self.name = name
        self.topics = topics
        self.username = username
        self.password = password
        self.profile_image = profile_image

        self.dark_mode = True
        self.secondary_color = 'rgb(55, 109, 42)'

    @classmethod
    def login(cls, username, password): 
        with open('settings.json', 'r') as file:
                settings = json.loads( file.read() )
        with open('topics.json', 'r') as file:
                topics = json.loads( file.read() )

        if settings['username'] == username and settings['password'] == password:
            return cls(
                settings['name'],
                topics,
                settings['username'],
                settings['password'],
                settings['profile-image'],
            )



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



