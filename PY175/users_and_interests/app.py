import yaml
from flask import Flask, render_template, g

app = Flask(__name__)

with open('data/users.yaml', 'r') as file:
    data = yaml.safe_load(file)
    user_names = [key for key in data]

def total_interests(user_data):
    return sum(len(value['interests']) for value in user_data.values())

app.jinja_env.filters['total_interests'] = total_interests

@app.route('/')
def index():
    return render_template('index.html',
                           data=data,
                           user_names=user_names)

@app.route('/users/<user>')
def users(user):
    user_data = data[user]
    email = user_data['email']
    interests = user_data['interests']

    return render_template('user.html',
                           user=user,
                           email=email,
                           interests=interests,
                           data=data,
                           user_names=user_names)

if __name__ == '__main__':
    app.run(debug=True, port=5003)
