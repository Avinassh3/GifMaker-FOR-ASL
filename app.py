from flask import Flask, request, jsonify
import uuid
import os
import sys
from os import path
import numpy as np
from flask import Flask, request, redirect, url_for,send_file
from werkzeug.utils import secure_filename
from flask_cors import CORS,cross_origin
app = Flask(__name__)
CORS(app)
import imageio
def GenerateGIF(filenames,gifname):
    images=[]
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave(gifname, images,duration=1)


def saveGif(nam):
    filename=['Images/start.jpg']
    fil=nam.upper()
    nam=list(nam)
    for i in range(0,len(nam)):
        if nam[i]==" ":
            filename.append("Images/"+"space"+"_test.jpg")
            continue
        filename.append("Images/"+nam[i]+"_test.jpg")
    GenerateGIF(filename,"gifs/"+fil+".gif")




#change request.form to request.get_json()


@app.route('/api/gif', methods=['POST'])
@cross_origin()
def gen_gif():
    if request.method=="POST":
        data = request.get_json()
        if 'word' in data:
            name=data['word']
            name=name.upper()
            if path.exists("gifs/"+name+".gif"):
                return send_file("gifs/"+name+".gif",mimetype="image/gif")
            saveGif(name)
            return send_file("gifs/"+name+".gif",mimetype="image/gif")

if __name__ == '__main__':
    app.run(port=5000,debug=True)
