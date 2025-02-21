from flask import Flask, render_template, request#, redirect, url_for

app = Flask(__name__)

FUEL_COST = 26
FUEL_TANK_CAPACITY = 500

DISTANCESnREQUIRED_FUEL = {
  "tijuana": {
    "distance": 2500,
    "fuel": 714
  },
  "juarez": {
    "distance": 1380,
    "fuel": 394
  },
  "laredo": {
    "distance": 720,
    "fuel": 206
  },
  "vallarta": {
    "distance": 624,
    "fuel": 178
  },
  "merida": {
    "distance": 1700,
    "fuel": 486
  },
  "nogales": {
    "distance": 1720,
    "fuel": 491
  },
  "tuxtla": {
    "distance": 1230,
    "fuel": 351
  },
  "puerto_escondido": {
    "distance": 1050,
    "fuel": 300
  },
  "manzanillo": {
    "distance": 615,
    "fuel": 176
  }
}

@app.route('/')
def home():
  return render_template('mapa-mexico.html')

@app.route('/mapa1', methods=['GET', 'POST'])
def mapa1():
  tijuana = request.form.get('tijuana', type=int) or 0
  juarez = request.form.get('juarez', type=int) or 0
  laredo = request.form.get('laredo', type=int) or 0
  vallarta = request.form.get('vallarta', type=int) or 0
  merida = request.form.get('merida', type=int) or 0
  info = {
    "tijuana": {
      "trips": tijuana,
      "distance": tijuana * DISTANCESnREQUIRED_FUEL["tijuana"]["distance"],
      "fuel": tijuana * DISTANCESnREQUIRED_FUEL["tijuana"]["fuel"]
    },
    "juarez": {
      "trips": juarez,
      "distance": juarez * DISTANCESnREQUIRED_FUEL["juarez"]["distance"],
      "fuel": juarez * DISTANCESnREQUIRED_FUEL["juarez"]["fuel"]
    },
    "laredo": {
      "trips": laredo,
      "distance": laredo * DISTANCESnREQUIRED_FUEL["laredo"]["distance"],
      "fuel": laredo * DISTANCESnREQUIRED_FUEL["laredo"]["fuel"]
    },
    "vallarta": {
      "trips": vallarta,
      "distance": vallarta * DISTANCESnREQUIRED_FUEL["vallarta"]["distance"],
      "fuel": vallarta * DISTANCESnREQUIRED_FUEL["vallarta"]["fuel"]
    },
    "merida": {
      "trips": merida,
      "distance": merida * DISTANCESnREQUIRED_FUEL["merida"]["distance"],
      "fuel": merida * DISTANCESnREQUIRED_FUEL["merida"]["fuel"]
    }
  }
  return render_template('mapa-mexico.html', info=info)

@app.route('/mapa2', methods=['GET', 'POST'])
def mapa2():
  tijuana = request.form.get('tijuana', type=int) or 0
  juarez = request.form.get('juarez', type=int) or 0
  laredo = request.form.get('laredo', type=int) or 0
  vallarta = request.form.get('vallarta', type=int) or 0
  merida = request.form.get('merida', type=int) or 0
  info = {
    "tijuana": {
      "trips": tijuana,
      "distance": tijuana * DISTANCESnREQUIRED_FUEL["tijuana"]["distance"],
      "fuel": tijuana * DISTANCESnREQUIRED_FUEL["tijuana"]["fuel"],
      "total_tanks": tijuana * DISTANCESnREQUIRED_FUEL["tijuana"]["fuel"] / FUEL_TANK_CAPACITY,
      "fuel_cost": tijuana * DISTANCESnREQUIRED_FUEL["tijuana"]["fuel"] * FUEL_COST
    },
    "juarez": {
      "trips": juarez,
      "distance": juarez * DISTANCESnREQUIRED_FUEL["juarez"]["distance"],
      "fuel": juarez * DISTANCESnREQUIRED_FUEL["juarez"]["fuel"],
      "total_tanks": juarez * DISTANCESnREQUIRED_FUEL["juarez"]["fuel"] / FUEL_TANK_CAPACITY,
      "fuel_cost": juarez * DISTANCESnREQUIRED_FUEL["juarez"]["fuel"] * FUEL_COST
    },
    "laredo": {
      "trips": laredo,
      "distance": laredo * DISTANCESnREQUIRED_FUEL["laredo"]["distance"],
      "fuel": laredo * DISTANCESnREQUIRED_FUEL["laredo"]["fuel"],
      "total_tanks": laredo * DISTANCESnREQUIRED_FUEL["laredo"]["fuel"] / FUEL_TANK_CAPACITY,
      "fuel_cost": laredo * DISTANCESnREQUIRED_FUEL["laredo"]["fuel"] * FUEL_COST
    },
    "vallarta": {
      "trips": vallarta,
      "distance": vallarta * DISTANCESnREQUIRED_FUEL["vallarta"]["distance"],
      "fuel": vallarta * DISTANCESnREQUIRED_FUEL["vallarta"]["fuel"],
      "total_tanks": vallarta * DISTANCESnREQUIRED_FUEL["vallarta"]["fuel"] / FUEL_TANK_CAPACITY,
      "fuel_cost": vallarta * DISTANCESnREQUIRED_FUEL["vallarta"]["fuel"] * FUEL_COST
    },
    "merida": {
      "trips": merida,
      "distance": merida * DISTANCESnREQUIRED_FUEL["merida"]["distance"],
      "fuel": merida * DISTANCESnREQUIRED_FUEL["merida"]["fuel"],
      "total_tanks": merida * DISTANCESnREQUIRED_FUEL["merida"]["fuel"] / FUEL_TANK_CAPACITY,
      "fuel_cost": merida * DISTANCESnREQUIRED_FUEL["merida"]["fuel"] * FUEL_COST
    }
  }
  return render_template('mapa2.html', info=info)

@app.route('/mapa3', methods=['GET', 'POST'])
def mapa3():
  tijuana = request.form.get('tijuana', type=int) or 0
  juarez = request.form.get('juarez', type=int) or 0
  laredo = request.form.get('laredo', type=int) or 0
  vallarta = request.form.get('vallarta', type=int) or 0
  merida = request.form.get('merida', type=int) or 0
  nogales = request.form.get('nogales', type=int) or 0
  tuxtla = request.form.get('tuxtla', type=int) or 0
  puerto_escondido = request.form.get('puerto_escondido', type=int) or 0
  manzanillo = request.form.get('manzanillo', type=int) or 0
  info = {
    "tijuana": {
      "trips": tijuana,
      "distance": tijuana * DISTANCESnREQUIRED_FUEL["tijuana"]["distance"],
      "fuel": tijuana * DISTANCESnREQUIRED_FUEL["tijuana"]["fuel"],
      "total_tanks": tijuana * DISTANCESnREQUIRED_FUEL["tijuana"]["fuel"] / FUEL_TANK_CAPACITY,
      "fuel_cost": tijuana * DISTANCESnREQUIRED_FUEL["tijuana"]["fuel"] * FUEL_COST
    },
    "juarez": {
      "trips": juarez,
      "distance": juarez * DISTANCESnREQUIRED_FUEL["juarez"]["distance"],
      "fuel": juarez * DISTANCESnREQUIRED_FUEL["juarez"]["fuel"],
      "total_tanks": juarez * DISTANCESnREQUIRED_FUEL["juarez"]["fuel"] / FUEL_TANK_CAPACITY,
      "fuel_cost": juarez * DISTANCESnREQUIRED_FUEL["juarez"]["fuel"] * FUEL_COST
    },
    "laredo": {
      "trips": laredo,
      "distance": laredo * DISTANCESnREQUIRED_FUEL["laredo"]["distance"],
      "fuel": laredo * DISTANCESnREQUIRED_FUEL["laredo"]["fuel"],
      "total_tanks": laredo * DISTANCESnREQUIRED_FUEL["laredo"]["fuel"] / FUEL_TANK_CAPACITY,
      "fuel_cost": laredo * DISTANCESnREQUIRED_FUEL["laredo"]["fuel"] * FUEL_COST
    },
    "vallarta": {
      "trips": vallarta,
      "distance": vallarta * DISTANCESnREQUIRED_FUEL["vallarta"]["distance"],
      "fuel": vallarta * DISTANCESnREQUIRED_FUEL["vallarta"]["fuel"],
      "total_tanks": vallarta * DISTANCESnREQUIRED_FUEL["vallarta"]["fuel"] / FUEL_TANK_CAPACITY,
      "fuel_cost": vallarta * DISTANCESnREQUIRED_FUEL["vallarta"]["fuel"] * FUEL_COST
    },
    "merida": {
      "trips": merida,
      "distance": merida * DISTANCESnREQUIRED_FUEL["merida"]["distance"],
      "fuel": merida * DISTANCESnREQUIRED_FUEL["merida"]["fuel"],
      "total_tanks": merida * DISTANCESnREQUIRED_FUEL["merida"]["fuel"] / FUEL_TANK_CAPACITY,
      "fuel_cost": merida * DISTANCESnREQUIRED_FUEL["merida"]["fuel"] * FUEL_COST
    },
    "nogales": {
      "trips": nogales,
      "distance": nogales * DISTANCESnREQUIRED_FUEL["nogales"]["distance"],
      "fuel": nogales * DISTANCESnREQUIRED_FUEL["nogales"]["fuel"],
      "total_tanks": nogales * DISTANCESnREQUIRED_FUEL["nogales"]["fuel"] / FUEL_TANK_CAPACITY,
      "fuel_cost": nogales * DISTANCESnREQUIRED_FUEL["nogales"]["fuel"] * FUEL_COST
    },
    "tuxtla": {
      "trips": tuxtla,
      "distance": tuxtla * DISTANCESnREQUIRED_FUEL["tuxtla"]["distance"],
      "fuel": tuxtla * DISTANCESnREQUIRED_FUEL["tuxtla"]["fuel"],
      "total_tanks": tuxtla * DISTANCESnREQUIRED_FUEL["tuxtla"]["fuel"] / FUEL_TANK_CAPACITY,
      "fuel_cost": tuxtla * DISTANCESnREQUIRED_FUEL["tuxtla"]["fuel"] * FUEL_COST
    },
    "puerto_escondido": {
      "trips": puerto_escondido,
      "distance": puerto_escondido * DISTANCESnREQUIRED_FUEL["puerto_escondido"]["distance"],
      "fuel": puerto_escondido * DISTANCESnREQUIRED_FUEL["puerto_escondido"]["fuel"],
      "total_tanks": puerto_escondido * DISTANCESnREQUIRED_FUEL["puerto_escondido"]["fuel"] / FUEL_TANK_CAPACITY,
      "fuel_cost": puerto_escondido * DISTANCESnREQUIRED_FUEL["puerto_escondido"]["fuel"] * FUEL_COST
    },
    "manzanillo": {
      "trips": manzanillo,
      "distance": manzanillo * DISTANCESnREQUIRED_FUEL["manzanillo"]["distance"],
      "fuel": manzanillo * DISTANCESnREQUIRED_FUEL["manzanillo"]["fuel"],
      "total_tanks": manzanillo * DISTANCESnREQUIRED_FUEL["manzanillo"]["fuel"] / FUEL_TANK_CAPACITY,
      "fuel_cost": manzanillo * DISTANCESnREQUIRED_FUEL["manzanillo"]["fuel"] * FUEL_COST
    }
  }
  return render_template('mapa3.html', info=info)

if __name__ == "__main__":
  app.run(debug=True)
