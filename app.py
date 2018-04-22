from flask import *
from gtts import gTTS
from random import randint, choice
from models.name import *
import mlab

app = Flask(__name__)
app.secret_key = "sudo"
mlab.connect()



@app.route('/')
def index():
    return render_template('index.html')

<<<<<<< HEAD
@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "GET":
        return render_template('sign_up.html')
    elif request.method == "POST":
        form = request.form
        fullname = form['fullname']
        email = form['email']
        username = form['username']
        password = form['password']
        all_user = User.objects(username=username).first()
        if all_user == None:
            new_user = User(fullname=fullname,
                            email=email,
                            username=username,
                            password=password)
            new_user.save()
            return redirect(url_for('log_in'))
        else:
            return 'Tên đăng nhập đã bị trùng, vui lòng bấm back để nhập lại'


@app.route('/login', methods=["GET", "POST"])
def log_in():
    if request.method == "GET":
        return render_template('log_in.html')
    elif request.method == "POST":
        form = request.form
        username_input = form['username']
        password_input = form['password']
        account = User.objects(username=username_input, password=password_input).first()
        if account == None:
            return redirect(url_for('log_in'))
        else:
            return redirect(url_for('index'))

=======
@app.route("/ajax")
def ajax():
    return render_template("test.html")

@app.route('/tuan')
def tuan():
    return render_template('tuan.html')
>>>>>>> e97e548d9c18be8f032384e47830beedfff8e170

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


@app.route("/add-char", methods=["GET", "POST"])
def add_char():
    if request.method == "GET":
        return render_template('new-char.html')
    elif request.method == "POST":
        form = request.form
        new_char = form['char']
        audio = form['audio']
        new_audio = gTTS(text='xin mời '+ audio + " lên bảng", lang='vi')
        audio_location = 'static/audio/{0}.mp3'.format(new_char)
        new_audio.save(audio_location)
        new_character = Character(char=new_char, audio=audio_location)
        new_character.save()
        return redirect(url_for('add_char'))

@app.route("/add-state", methods=["GET", "POST"])
def add_state():
    if request.method == "GET":
        return render_template('new-state.html')
    elif request.method == "POST":
        form = request.form
        new_state = form['state']
        audio = form['audio']
        new_audio = gTTS(text=audio, lang='vi')
        audio_location = 'static/audio/{0}.mp3'.format(new_state)
        new_audio.save(audio_location)
        new_state = State(state=new_state, audio=audio_location)
        new_state.save()
        return redirect(url_for('add_state'))


if __name__ == '__main__':
  app.run(debug=True)
