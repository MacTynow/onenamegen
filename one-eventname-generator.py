import random
from flask import Flask
app = Flask(__name__)

firstword_list = [
  "pursuit",
  "heart",
  "warrior",
  "conquest",
  "destiny",
  "realm",
  "kingdom"
]

secondword_list = [
  "greatness",
  "the lion",
  "dream",
  "heroes",
  "champions"
]

@app.route("/newevent")
def newevent():
  firstword = random.choice(firstword_list)
  secondword = random.choice(secondword_list)
  s = "ONE : " + firstword.capitalize() + " of "  + secondword.capitalize()

  return s
