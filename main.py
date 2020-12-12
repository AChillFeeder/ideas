
from flask import Flask, render_template

app = Flask(__name__)

app.route('/')
def index():
    return render_template('index.html')

# how to deny access to subdirectories in flask?

class User:
    def __init__(self, name, topics) -> object:
        self.name = name
        self.topics = topics # array
        self.username = 'nagakabourous'
        self.password = '1UPPER1lower1digit.'

    def login(self, username, password): # might cause an error, test both cases
        return (username == self.username and password == self.password)

    def settings(settings = {}):
        """
            This function is our middle-man to the JSON file
            if an argument or a non-empty dictionary is supplied then the function changes current settings
            else it returns the current settings

            settings = {
                'username': string,
                'password': string, # hashed possibly
                'name': string,
            }
        """
        import json # we'll use JSON in this function exclusively, so there's no need to import it at the start
        if settings:
            # change settings
            with open('settings.json', 'w') as file:
                file.write( json.dumps(settings) )
        else:
            with open('settings.json', 'r') as file:
                return json.loads( file.read() )


class Topic:
    def __init__(self, title, tags, ideas=[]) -> object:
        self.title = title # str
        self.tags = tags # array
        self.ideas = ideas # array

    def add_idea(self, idea):
        self.ideas.append(idea)




