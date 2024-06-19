import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hi sir, Done with my Work, Thank you.!"
if __name__ == "__main__":
    app.run()
