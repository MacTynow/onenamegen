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
  "kingdom",
  "tribe",
  "heroes",
  "union",
  "dynasty",
  "state",
  "quest",
  "battle"
  "reign",
  "pinnacle",
  "legends",
  "spirit"
]

secondword_list = [
  "greatness",
  "the lion",
  "dream",
  "heroes",
  "champions",
  "warriors",
  "power",
  "nations",
  "destiny",
  "superheroes",
  "heavens",
  "kings",
  "horizon",
  "domination"
]

@app.route("/newevent")
def newevent():
  firstword = random.choice(firstword_list)
  secondword = firstword
  while secondword == firstword:
    secondword = random.choice(secondword_list)

  s = "ONE : " + firstword.capitalize() + " of "  + secondword.capitalize()

  return s
