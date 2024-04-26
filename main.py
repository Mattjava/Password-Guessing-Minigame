from generator import generateString
from flask import Flask, render_template, url_for, request

# Generates username and password
username = generateString(8)
password = generateString(10)

# This number counts down when a user enters the incorrect details
# When it reaches 0 or less, it will tell the user the password through the website
count = 3

# Checks if the inputted password is the correct password
#Returns true if it is, and false if otherwise
def checkPassword(input):
    if input == password:
        return True
    else:
        return False

# Creates the web app
app = Flask(__name__, template_folder="templates")

# Connects the main method to the web app
@app.route("/", methods=["GET", "POST"])
def main():
    global count
    if request.method == "GET":
        # Returns and generates "index.html" in its initial state
        return render_template("index.html", username=username, correct=True, count=count, password=password)
    elif request.method == "POST":
        if request.form["username"] != username or not checkPassword(request.form["password"]):
            # Returns "index.html", but edited to show a message letting the user know they got something incorrect.
            # It also subtracts 1 from count. Scroll up for more information.
            count += -1
            return render_template("index.html", username=username, correct=False, count=count, password=password)
        else:
            # Returns and generates "correct.html"
            return render_template("correct.html")

if __name__ == "__main__":
    app.run()