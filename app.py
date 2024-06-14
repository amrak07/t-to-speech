from flask import Flask, render_template
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)
app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/play")
def play_audio():
  message = "I love you Nakshathra"  # Replace with your desired message
  engine.say(message)
  engine.runAndWait()
  return "Audio Played"  # Optional confirmation message

if __name__ == "__main__":
  app.run(debug=True)
