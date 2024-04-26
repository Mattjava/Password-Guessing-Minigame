from generator import generateString
from flask import Flask, render_template, url_for, request

username = generateString(8)
password = generateString(10)

count = 3

print(username)
print(password)

def checkPassword(input):
    if input == password:
        return True
    else:
        return False


app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def main():
    global count
    if request.method == "GET":
        return render_template("index.html", username=username, correct=True, count=count, password=password)
    elif request.method == "POST":
        if request.form["username"] != username or not checkPassword(request.form["password"]):
            count += -1
            return render_template("index.html", username=username, correct=False, count=count, password=password)
        else:
            return render_template("correct.html")

if __name__ == "__main__":
    app.run()