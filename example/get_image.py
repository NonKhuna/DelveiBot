from flask import Flask, request, abort,render_template,request,redirect,url_for,send_from_directory
from config import *

app = Flask(__name__)

app.config["CLIENT_IMAGES"] = imagepart

# localhost/get-image/<image_name>
@app.route("/get-image/<image_name>")
def get_image(image_name):
    try:
        return send_from_directory(app.config["CLIENT_IMAGES"], filename=image_name, as_attachment=True)
    except FileNotFoundError:
        abort(404)

if __name__ == "__main__":
    app.run(port=200)