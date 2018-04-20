from flask import *
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

if __name__ == '__main__':
  app.run(debug=True)
