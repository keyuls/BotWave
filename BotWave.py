import cloudinary
import cloudinary.uploader
import cloudinary.api

from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    cloudinary.config(
        cloud_name="botsfloor",
        api_key="521852823538172",
        api_secret="Exvv_UaBxdvPIT7XmjOTFFAmyXM"
    )
    cloudinary.uploader.upload("images.jpeg")

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    #app.run(debug=False, port=port, host='0.0.0.0')
    app.run(debug=False, port=port, host='127.0.0.1')