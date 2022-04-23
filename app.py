from flask import Flask, render_template, request, redirect, url_for
import database
import sys


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("hello.html")


# 집 등록하기
@app.route('/apply')
def apply():
    return render_template("apply.html")


@app.route('/applyphoto')
def photo_apply():
    location = request.args.get("location")
    cleaness = request.args.get("clean")
    built_in = request.args.get("built")
    if cleaness == None :
        cleaness = False
    else :
        cleaness = True

    database.save(location,cleaness,built_in)
    return render_template("apply_photo.html")


@app.route('/upload_done', methods=['POST'])
def upload_done():
    uploaded_files = request.files["file"]
    uploaded_files.save("static/img/{}.jpeg".format(database.now_index()))
    return redirect(url_for("hello"))


@app.route("/list")
def list() :
    return render_template("list.html")


if __name__ == '__main__':
    app.run(debug=True, port=8000)
