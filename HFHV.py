# save this as app .py
form import Flask

app = Flask(__name__)

@app .route("/")
def hello():
    return "hello , world!"