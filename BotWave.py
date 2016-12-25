import cloudinary
import cloudinary.uploader
import cloudinary.api

import os
from flask import Flask , request , json , render_template , url_for


app = Flask(__name__)

@app.route('/signUp', methods=['POST'])
def signUp():
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _otherTools = request.form['otherTools']
    _botLink = request.form['botLink']
    return render_template('empty.html')
    '''if _name and _email and _otherTools and _botLink:
        return json.dumps({'html': '<span>All fields good !!</span>'})
    else:
     return json.dumps({'html': '<span>Enter the required fields</span>'})'''

@app.route('/')
def hello_world():
    return render_template('index.html',data=12)
    ''' cloudinary.config(
        cloud_name="botsfloor",
        api_key="521852823538172",
        api_secret="Exvv_UaBxdvPIT7XmjOTFFAmyXM"
    )
    cloudinary.uploader.upload("chatbotjobs.png")
    return ('', 204)'''

@app.route('/submitstack')
def main():
    return render_template('signup.html')

@app.route('/bots')
def botDetails():
    return render_template('botdetails.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    #app.run(debug=False, port=port, host='0.0.0.0')
    app.run(debug=False, port=port, host='127.0.0.1')
