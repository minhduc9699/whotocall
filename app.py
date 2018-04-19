from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tuan')
def tuan():
    return render_template('tuan.html')

if __name__ == '__main__':
  app.run(debug=True)
