from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    # return {"message": "Hello Boss, your API is running!"}
    return "Hello Boss, your API is running now !"

if __name__ == "__main__":
    app.run(debug=True)
