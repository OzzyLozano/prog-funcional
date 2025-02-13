wall_height = float(input('ingrese la altura de la pared: '))
wall_width = float(input('ingrese la longitud de la pared: '))
wall_area = wall_height * wall_width

window_height = float(input('ingrese la altura del ventana 1: '))
window_width = float(input('ingrese la longitud del ventana 1: '))
window_1 = window_height * window_width

window_height_2 = float(input('ingrese la altura del ventana 2: '))
window_width_2 = float(input('ingrese la longitud del ventana 2: '))
window_2 = window_height_2 * window_width_2

BRICK_WIDTH = 0.23
BRICK_HEIGHT = 0.05
espesor_punta_horizontal = 0.01
espesor_punta_vertical = 0.015
bricks = ((wall_area - window_1 - window_2) / ((BRICK_WIDTH + espesor_punta_horizontal) * (BRICK_HEIGHT + espesor_punta_vertical)))
print(f'cantidad de ladrillos requeridos: { bricks:.2f }')
