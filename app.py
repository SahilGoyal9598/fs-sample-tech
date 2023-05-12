from flask import Flask

app = Flask(__name__)


# decorator in python "@"
@app.route("/")  #home page
def hello_world():
  return "Hello world"


print(__name__)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
