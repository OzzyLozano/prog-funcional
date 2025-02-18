from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# bricks stuff
BRICK_WIDTH = 0.23
BRICK_HEIGHT = 0.05
VERTICAL_JOINT_THICKNESS = 0.01
HORIZONTAL_JOINT_THICKNESS = 0.015

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/bricks', methods=['GET', 'POST'])
def bricks():
  return render_template('bricks.html')

@app.route('/windows', methods=['GET', 'POST'])
def windows():
  return f'<p>xd</p>'

@app.route('/columns', methods=['GET', 'POST'])
def columns():
  return f'<p>xd</p>'

@app.route('/floor', methods=['GET', 'POST'])
def floor():
  return f'<p>xd</p>'

@app.route('/ceiling', methods=['GET', 'POST'])
def ceiling():
  return f'<p>xd</p>'

@app.route('/room', methods=['GET', 'POST'])
def room():
  return f'<p>xd</p>'

@app.route('/exam', methods=['GET', 'POST'])
def exam():
  return f'<p>xd</p>'

@app.route('/calculate-bricks', methods=['GET', 'POST'])
def calc_bricks():
  longitud = request.form.get('longitud', type=float)
  altura = request.form.get('altura', type=float)

  if longitud and altura:
    area = longitud * altura
    bricks = area / ((BRICK_WIDTH + VERTICAL_JOINT_THICKNESS) * (BRICK_HEIGHT + HORIZONTAL_JOINT_THICKNESS))
    return render_template('bricks.html', bricks=bricks)

  return redirect(url_for('bricks'))

if __name__ == "__main__":
  app.run(debug=True)
