from flask import Flask

app= Flask(__name__)
@app.route("/")
def home():
    return" hello! Welcome to the first Page of Saas App"

if __name__ == "__main__":
    app.run()