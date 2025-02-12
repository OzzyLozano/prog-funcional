# input: { largo, ancho, espesor del piso }, volumen concreto requerido para el piso
# 1m^3 de concreto requiere: { 350kg cemento, 0.56m^3 arena, 0.56m^3 grava, 180l agua }
# la cantidad de concreto requerido para el piso requieren: { ?? }
ROOF_THICKNESS = 0.1

class ConcreteRequirements:
  def __init__(self):
    self.cement_bag = {'amount': 7, 'unit': 'sacos'}
    self.sand = {'amount': 0.56, 'unit': 'm^3'}
    self.gravel = {'amount': 0.84, 'unit': 'm^3'}
    self.water = {'amount': 180, 'unit': 'l'}
  
  def get_requirements(self, concrete_amount):
    return [
      f'cemento requerido: { '{:.2f}'.format(concrete_amount * self.cement_bag['amount']) } { self.cement_bag['unit'] }\n'
      f'arena requerida: { '{:.2f}'.format(concrete_amount * self.sand['amount']) } { self.sand['unit'] }\n'
      f'grava requerida: { '{:.2f}'.format(concrete_amount * self.gravel['amount']) } { self.gravel['unit'] }\n'
      f'agua requerida: { '{:.2f}'.format(concrete_amount * self.water['amount']) } { self.water['unit'] }\n'
    ]

room_length = float(input('longitud frontal (m): '))
room_width = float(input('longitud lateral (m): '))

concrete_volume = room_length * room_width * ROOF_THICKNESS

requirements = ConcreteRequirements().get_requirements(concrete_volume)

for requirement in requirements:
  print(requirement)
