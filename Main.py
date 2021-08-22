from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename
from flask import jsonify
import os

import OCR

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template("./index.html")

@app.route('/doocr', methods=['GET', 'POST'])
def doocr():
    if request.method == 'POST':
        try:
            f = request.files['file']
            filename = secure_filename(f.filename)
            path = os.path.join(os.getcwd(), "static", "upload", filename)
            f.save(path)
            res = OCR.doOCR(path)
            return jsonify(res)
        except print(0):
            return jsonify({
                'status' : 500,
                'msg': "failed"
            })
    else:
        return jsonify({
                'status' : 401,
                'msg': "method get not allowed"
            })


if __name__ == '__main__':
    app.run(debug=True)
    