import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def int main():
    a=10
    b=20
    return "abc" 
    '''a=10
    b=20
    print ("The sum is:",a+b)
main()'''
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
