from flask import Flask, render_template, redirect, url_for, request, session, flash, g, make_response, send_file
# import requests
# from bs4 import BeautifulSoup
from os import urandom
from formSideBar import subjects_maker


app = Flask(__name__)


@app.route('/')
def index():
	subjpic = subjects_maker(tabu=0)
	subjects = list(subjpic.keys())
	return render_template("index.html", subjects=subjects, subjpic=subjpic)


if __name__ == "__main__":
    secret_key = urandom(134)
    print("\n Secret_key = ", secret_key, " \n")
    app.secret_key = secret_key
    app.run(debug=True)