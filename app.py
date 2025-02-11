from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/bricks', methods=['GET', 'POST'])
def bricks():
   return f'<p>xd</p>'

if __name__ == "__main__":
    app.run(debug=True)
