from flask import Flask, request, redirect, render_template_string, url_for
import requests
from io import BytesIO
import os
import random
import string


app = Flask(__name__)

"""DEFAULT ROUTE OF WEBAPP"""
@app.route("/", methods=['GET', 'POST'])
def main():
    """ DO SOMETHING HERE"""
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
