from flask import Flask, render_template, request
import sys

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("hello.html")


# 집 등록하기
@app.route('/apply')
def apply():
    return render_template("apply.html")


# 집 리스트
@app.route('/list')
def list():
    return render_template("list.html")

@app.route('/applyphoto')
def applyphoto() :
    location = request.args.get("location")
    cleaness = request.args.get("clean")
    built_in = request.args.get("built")
    print(location, cleaness, built_in)
    # return render_template("apply.html")


if __name__ == '__main__':
    app.run(debug=True, port=8000)
