from flask import *
from gtts import gTTS
from random import randint
from models.name import *
import mlab

app = Flask(__name__)
app.secret_key = "sudo"
mlab.connect()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tuan')
def tuan():
    return render_template('tuan.html')

@app.route('/admin', methods=["GET", "POST"])
def add_name():
    if request.method == "GET":
        return render_template('new-name.html')
    elif request.method == "POST":
        form = request.form
        new_name = form['name']
        new_audio = gTTS(text=new_name, lang='vi')
        audio_location = 'static/audio/{0}.mp3'.format(new_name)
        new_audio.save(audio_location)
        new_victim = Name(name=new_name, audio=audio_location)
        new_victim.save()
        return redirect(url_for('add_name'))

if __name__ == '__main__':
  app.run(debug=True)
