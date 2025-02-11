# variables (metros)
longitud_ladrillo = 0.23
altura_ladrillo = 0.05

espesor_junta_horizontal = 0.010
espesor_junta_vertical = 0.015

longitud_pared = float(input('ingrese la longitud de la pared: '))
altura_pared = float(input('ingrese la altura de la pared: '))

area_pared = altura_pared * longitud_pared

cantidad_ladrillo = (area_pared / ((longitud_ladrillo + espesor_junta_horizontal) * (altura_ladrillo + espesor_junta_vertical)))
print(f'vas a requerir {'{:.2f}'.format(cantidad_ladrillo)} ladrillos')

# longitud_block = 0.39
# altura_block = 0.20
# cantidad_block = (area_pared / ((longitud_block + espesor_punta_horizontal) * (altura_block + espesor_punta_vertical)))
# print(f'vas a requerir {cantidad_block} blocks')
