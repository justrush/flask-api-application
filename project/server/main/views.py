# project/server/main/views.py

import requests
from project.server.main.bitstamp_requests import get_bitstamp_ticker
from flask import render_template, Blueprint

main_blueprint = Blueprint('main', __name__,)


@main_blueprint.route('/')
def home():
    bitstamp_ticker_shit = get_bitstamp_ticker()
    return render_template('main/home.html', bitstamp_last_price=bitstamp_ticker_shit)

@main_blueprint.route('/')
def home():
    bitstamp_ticker_shit = get_bitstamp_ticker()
    return render_template('main/home.html', bitstamp_last_price=bitstamp_ticker_shit)

@main_blueprint.route("/about/")
def about():
    return render_template("main/about.html")
