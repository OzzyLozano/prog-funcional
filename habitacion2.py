# bricks stuff
BRICK_WIDTH = 0.23
BRICK_HEIGHT = 0.05
VERTICAL_JOINT_THICKNESS = 0.01
HORIZONTAL_JOINT_THICKNESS = 0.015

# inputs
door_length = float(input('ancho de la puerta: '))
door_height = float(input('altura de la puerta: '))
right_window_width = float(input('ancho de la ventana (der): '))
right_window_height = float(input('altura de la ventana (der): '))
left_window_width = float(input('ancho de la ventana (izq): '))
left_window_height = float(input('altura de la ventana (izq): '))
back_window_width = float(input('ancho de la ventana (atras): '))
back_window_height = float(input('altura de la ventana (atras): '))
front_wall_length = float(input('largo de la pared frontal: '))
lateral_wall_length = float(input('largo de la pared lateral: '))
wall_height = float(input('altura de la pared: '))

# formulas
door_area = door_length * door_height
right_window_area = right_window_width * right_window_height
left_window_area = left_window_width * left_window_height
back_window_area = back_window_width * back_window_height
front_wall_area = (front_wall_length * wall_height) - door_area
right_wall_area = (lateral_wall_length * wall_height) - right_window_area
left_wall_area = (lateral_wall_length * wall_height) - left_window_area
back_wall_area = (front_wall_length * wall_height) - back_window_area

total_area = front_wall_area + right_wall_area + left_wall_area + back_wall_area

bricks = ((total_area) / ((BRICK_WIDTH + VERTICAL_JOINT_THICKNESS) * (BRICK_HEIGHT + HORIZONTAL_JOINT_THICKNESS)))

print(f'area total: {total_area:.2f}')
print(f'ladrillos: {bricks:.2f}')
