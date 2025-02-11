# 4 varillas, con anillos, un anillo cada 10cm, altura del muro: 2.1m
# 16 varillas en total para hacer un cuarto de 4 paredes: 33.6m de varilla (total)
# anillos requeridos: 84
# entradas: { numero de castillos (columnas), altura  del castillo }

RING_DISTANCE = 0.1
RODS_PER_COLUMN = 4

column_count = float(input('ingrese la cantidad de castillos: '))
column_height = float(input('ingrese la altura de los castillos: '))

required_rod = column_count * column_height * RODS_PER_COLUMN
required_rings = column_count * column_height / RING_DISTANCE

print(f'metros de varilla: { required_rod }')
print(f'anillos requeridos: { required_rings }')
