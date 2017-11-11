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
    return "hello cloud!!!"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
