from cmu_graphics import*

#playa
Poligono(0,230,400,0,400,200,240,240,0,280,fill=gradiente('madera','trigo'),borde='negro')
Línea(0,230,400,80,fill='tierra',anchuraDeLínea=8)
Poligono(0,0,400,0,400,80,0,230,fill=gradiente('azur','lavanda','azulCieloProfundo',inicio='superior'))
Poligono(0,280,240,240,400,200,400,400,0,400,fill=gradiente('azulAlica','azul','azulMarino',inicio='superior'))

#palmera
Poligono(0,280,20,240,40,160,60,160,60,240,80,267,fill="tierra")
Circulo(40,160,10,fill='naranjaMarrón',borde='negro')
Circulo(60,160,10,fill='naranjaMarrón',borde='negro')
Circulo(50,170,10,fill='naranjaMarrón',borde='negro')


cmu_graphics.run()