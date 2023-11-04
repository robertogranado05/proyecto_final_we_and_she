from cmu_graphics import*

#playa
fabrica=Grupo(
        Rect(0,0,400,120,fill='cianClaro'),
        Rect(0,120,400,280,fill='verdeBosque',borde='verde'),
        Poligono(0,120,40,80,200,80,240,120,0,120,fill='grisOscuro',borde='gris'),
        Poligono(0,120,240,120,240,320,0,320,0,120,fill='grisOscuro',borde='gris'),
        Rect(40,200,160,120,fill='chocolate',borde='marrónCuero'),    
        Poligono(0,160,80,160,80,240,0,240,0,160,opacidad=50,borde='negro'),    
        Poligono(160,160,240,160,240,240,160,240,160,160,opacidad=50,borde='negro'), 
        Línea(120,200,120,320,anchuraDeLínea=5),

#huerta
       Poligono(240,120,400,120,280,280,240,240,240,120,fill='tierra',borde='negro'),
       Línea(240,240,280,120,anchuraDeLínea=6),
       Línea(280,280,330,120,anchuraDeLínea=6),
          
#plantas´
       Poligono(280,120,300,120,290,140,fill='verde'),
       Línea(290,138,290,160,fill='granate',anchuraDeLínea=5),

       Poligono(360,120,330,130,365,130,360,120,fill='verde'),
       Línea(365,130,360,160,fill='granate',anchuraDeLínea=5)
)

cmu_graphics.run()