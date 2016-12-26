import cloudinary
import cloudinary.uploader
import cloudinary.api

import os
from flask import Flask , request  , render_template
from flask_sqlalchemy import  SQLAlchemy

#Configuring cloudinary
cloudinary.config(
        cloud_name="botsfloor",
        api_key="521852823538172",
        api_secret="Exvv_UaBxdvPIT7XmjOTFFAmyXM"
    )

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/postgres'
db = SQLAlchemy(app)

toolsList =""

class botinfo(db.Model):
#    __tableName__ = "botinfo"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    link = db.Column(db.String)
    imagelink = db.Column(db.String)

    def __init__(self,name,email,link,imageLink):
        self.name = name
        self.email= email
        self.link = link
        self.imagelink = imageLink

class tools(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self,name):
        self.name= name


@app.route('/signUp', methods=['POST'])
def signUp():
    botName = request.form['inputName']
    botEmail = request.form['inputEmail']
    otherTools = request.form['otherTools']
    botLink = request.form['botLink']
    for tool in request.form.getlist('toolNames'):
        toolObj = tools(tool)
        db.session.add(toolObj)
    botImage = request.files['botImage']
    response = cloudinary.uploader.upload(botImage)
    botImageURL = response['url']
    bot = botinfo(botName,botEmail,botLink,botImageURL)
    db.session.add(bot)
    db.session.commit()
    global  toolsList
    return render_template('signup.html', toolsList=toolsList)

@app.route('/')
def hello_world():
    return render_template('index.html',data=12)
    '''
    return ('', 204)'''

@app.route('/submitstack')
def main():
    global toolsList
    toolsList = db.session.query(tools).all()
    return render_template('signup.html',toolsList=toolsList)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    #app.run(debug=False, port=port, host='0.0.0.0')
    app.run(debug=False, port=port, host='127.0.0.1')
