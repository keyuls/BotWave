import cloudinary
import cloudinary.uploader
import cloudinary.api

import os
from flask import Flask , request , json , render_template , url_for
from flask_sqlalchemy import  SQLAlchemy

#Configuring cloudinary
cloudinary.config(
        cloud_name="botsfloor",
        api_key="521852823538172",
        api_secret="Exvv_UaBxdvPIT7XmjOTFFAmyXM"
    )

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

toolsList =""

class bot(db.Model):
#    __tableName__ = "botinfo"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    verified = db.Column(db.Boolean)
    imagelink = db.Column(db.String)
    link = db.Column(db.String)

    def __init__(self,name,description,link,imageLink):
        self.name = name
        self.description= description
        self.link = link
        self.imagelink = imageLink

class bottool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self,name):
        self.name= name


@app.route('/signUp', methods=['POST'])
def signUp():
    botName = request.form['inputName']
    botDescription = request.form['inputDescription']
    botLink = request.form['botLink']
   # for tool in request.form.getlist('toolNames'):
    #    toolObj = tools(tool)
     #   db.session.add(toolObj)
    botImage = request.files['botImage']
    response = cloudinary.uploader.upload(botImage)
    botImageURL = response['url']
    botObj = bot(botName,botDescription,botLink,botImageURL)
    db.session.add(botObj)
    db.session.commit()
    global  toolsList
    return render_template('signup.html', toolsList=toolsList)

@app.route('/')
def beta():
    return render_template('beta.html')
    ''' cloudinary.config(
        cloud_name="botsfloor",
        api_key="521852823538172",
        api_secret="Exvv_UaBxdvPIT7XmjOTFFAmyXM"
    )
    cloudinary.uploader.upload("chatbotjobs.png")
    return ('', 204)'''

@app.route('/homepage')
def hello_world():
    return render_template('index.html',data=12)

@app.route('/submitstack')
def main():
    global toolsList
    toolsList = db.session.query(bottool).all()
    return render_template('signup.html',toolsList=toolsList)

@app.route('/bots')
def botDetails():
    return render_template('botdetails.html')

@app.route('/products')
def productDetails():
    return render_template('productdetails.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')
    #app.run(debug=False, port=port, host='127.0.0.1')
