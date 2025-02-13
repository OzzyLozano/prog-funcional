# cuarto, valores fijos:
DOOR_LENGTH = 1
DOOR_HEIGHT = 1.9
DOOR_AREA = DOOR_LENGTH * DOOR_HEIGHT
WINDOW_WIDTH = 1.2
WINDOW_HEIGHT = 1.5
WINDOW_AREA = WINDOW_WIDTH * WINDOW_HEIGHT

# bricks stuff
BRICK_WIDTH = 0.23
BRICK_HEIGHT = 0.05
VERTICAL_JOINT_THICKNESS = 0.01
HORIZONTAL_JOINT_THICKNESS = 0.015

# inputs
front_wall_length = float(input('largo de la pared frontal: '))
lateral_wall_length = float(input('largo de la pared lateral: '))
wall_height = float(input('altura de la pared: '))

front_wall_area = (front_wall_length * wall_height) - DOOR_AREA
lateral_wall_area = (lateral_wall_length * wall_height) - WINDOW_AREA
back_wall_area = (front_wall_length * wall_height)

total_area = front_wall_area + (lateral_wall_area * 2) + back_wall_area

bricks = ((total_area) / ((BRICK_WIDTH + VERTICAL_JOINT_THICKNESS) * (BRICK_HEIGHT + HORIZONTAL_JOINT_THICKNESS)))

print(f'ladrillos: {"{:.2f}".format(bricks)}')
