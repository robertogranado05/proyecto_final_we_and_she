from cmu_graphics import*

playa=Grupo(
            Rect(0,0,400,200,relleno=gradiente('azulCielo','amarillo',inicio='superior'),opacidad=50),
            Círculo(200,200,50,relleno=gradiente('amarillo','naranja',inicio='superior')),
            Rect(0,300,400,100,relleno='blancoNaranja'),
            Polígono(0,200,400,200,400,300,353,324,313,305,243,299,0,300,relleno=gradiente('azulAlica','azul','azulCieloProfundo',inicio='inferior'))
            )

playa.visible=False
#playa
inicio_playa=Grupo(
            Poligono(0,230,400,0,400,200,240,240,0,280,fill=gradiente('madera','trigo'),borde='negro'),
            Línea(0,230,400,80,fill='tierra',anchuraDeLínea=8),
            Poligono(0,0,400,0,400,80,0,230,fill=gradiente('azur','lavanda','azulCieloProfundo',inicio='superior')),
            Poligono(0,280,240,240,400,200,400,400,0,400,fill=gradiente('azulAlica','azul','azulMarino',inicio='superior')),

            #palmera
            Poligono(0,280,20,240,40,160,60,160,60,240,80,267,fill="tierra"),
            Circulo(40,160,10,fill='naranjaMarrón',borde='negro'),
            Circulo(60,160,10,fill='naranjaMarrón',borde='negro'),
            Circulo(50,170,10,fill='naranjaMarrón',borde='negro'),
)

espuma=Group(
          Circulo(80,280,25,fill=gradiente('marVerdeClaro','blanco'),borde='gainsboro'),
          Circulo(120,270,20,fill=gradiente('marVerdeClaro','blanco'),borde='gainsboro'),
          Circulo(160,280,20,fill=gradiente('marVerdeClaro','blanco'),borde='gainsboro'),
          Circulo(150,270,20,fill=gradiente('marVerdeClaro','blanco'),borde='gainsboro'),
          Circulo(180,270,25,fill=gradiente('marVerdeClaro','blanco'),borde='gainsboro'),
          Circulo(200,240,15,fill=gradiente('marVerdeClaro','blanco'),borde='gainsboro'),
          Circulo(220,270,25,fill=gradiente('marVerdeClaro','blanco'),borde='gainsboro'),
          Circulo(240,240,15,fill=gradiente('marVerdeClaro','blanco'),borde='gainsboro'),
          Circulo(400,200,20,fill=gradiente('marVerdeClaro','blanco'),borde='gainsboro'),
          Circulo(360,220,25,fill=gradiente('marVerdeClaro','blanco'),borde='gainsboro'),
          Circulo(320,240,20,fill=gradiente('marVerdeClaro','blanco'),borde='gainsboro'),
          Circulo(280,240,25,fill=gradiente('marVerdeClaro','blanco'),borde='gainsboro'),
          Circulo(320,225,15,fill=gradiente('marVerdeClaro','blanco'),borde='gainsboro')
)
espuma.visible=False
basura=Group(
          Poligono(320,360,290,330,320,320,310,320,330,320),
          Poligono(320,350,290,370,280,400,360,400,330,370,325,360,320,350),
          Rect(360,280,20,40,fill='rojo',borde='negro',opacidad=50),
          Circulo(360,320,10,fill='azul'),
          Circulo(380,280,10,fill='azul'),
          Poligono(400,200,380,220,380,250,400,250,400,200,fill='ladrillo',borde='negro',opacidad=50),
          Circulo(400,200,10,fill='grisTurbio'),
          Circulo(320,240,10,fill='grisTurbio',opacidad=50,borde='negro'),
          Poligono(320,240,300,250,300,270,330,270,330,250,320,240,fill='ladrillo',borde='negro',opacidad=50),
          Rect(10,340,120,20,fill='tierra',borde='marrónCuero'),
          Poligono(120,320,140,320,80,380,50,370,120,320,fill='tierra',borde='marrónCuero'),
          Circulo(240,320,35,fill='grisTurbio',borde='negro'),
          Circulo(240,320,25,fill='azul',borde='negro'),
          Rect(200,330,80,25,fill=gradiente('azul','azulMarino',inicio='superior')),
          Poligono(160,320,240,360,200,400,120,400,160,320,fill='verde',borde='verdeOscuro',anchuraDeBorde=5,opacidad=70),
          Línea(160,320,240,360,fill=gradiente('amarillo','oro'),anchuraDeLínea=5),
          Poligono(180,360,140,380,180,400,180,360,fill='amarillo',borde='negro'),
          Circulo(168,378,6,fill=None,borde='negro'),
          Circulo(163,380,6,fill=None,borde='negro'),
          Circulo(170,383,6,fill=None,borde='negro')
)
basura.visible=False
palaIzquierda = Polígono(190, 165, 130, 155, 130, 165, relleno='grisClaro')
palaDerecha = Polígono(205, 165, 265, 155, 265, 165, relleno='gris')

helicóptero = Grupo(
    Óvalo(200, 200, 100, 50, rotarÁngulo=-5),
    Círculo(200, 165, 8),
    Polígono(190, 180, 192, 165, 208, 165, 210, 175),
    Polígono(235, 185, 245, 205, 320, 190, 320, 180),
    Polígono(325, 205, 330, 195, 325, 180, 330, 160, 325, 155, 320, 170, 315, 185)
    )
helicóptero.relleno ='amarillo'

helicóptero.agregar(
    Polígono(185, 180, 165, 190, 155, 205, 180, 200, relleno='agua'),
    Polígono(190, 180, 210, 180, 215, 200, 185, 200, relleno='agua'),
    Óvalo(168, 193, 36, 12, relleno=gradiente('azur', 'agua', 'agua'), rotarÁngulo=-35),
    Línea(180, 220, 170, 235, relleno='rojo'),
    Línea(210, 220, 220, 235, relleno='rojo'),
    Línea(145, 235, 250, 235, relleno='rojo', anchuraDeLínea=3),
    palaIzquierda, palaDerecha
    )

huerta=Grupo( Rect(0,0,400,200,relleno=gradiente('azulCielo','amarillo',inicio='superior')),
            ##
            Rect(0,200,400,100,relleno='limaVerde'),
            ##
            Rect(0,300,400,100,relleno='gris'),
            Línea(0,376,400,376,relleno='blanco',anchuraDeLínea=8,guión=True),
            Línea(0,300,400,300,relleno='amarillo',anchuraDeLínea=5),
            ##
            Rect(27,180,170,100,relleno='naranjaMarrón',borde='NEGRO'),
            Rect(100,230,20,50,relleno='marrón',borde='negro'),
            Polígono(10,197,214,197,170,148,52,148,relleno='plateado',borde='negro') 
)
huerta.visible=False


      
def enTeclaRetenida(keys):
   
    if 'izquierda'in keys:
        helicóptero.centroX-=2 
       
    if 'derecha'in keys:
        helicóptero.centroX+=2
        
    if 'arriba'in keys:
        helicóptero.centroY-=2 
        
    if 'abajo'in keys:
        helicóptero.centroY+=2 
        
    
    if palaIzquierda.relleno=='grisClaro':
       palaIzquierda.relleno='gris'
       palaDerecha.relleno='grisClaro'
        
    else: 
         palaDerecha.relleno=='gris'
         palaIzquierda.relleno='grisClaro'
         palaDerecha.relleno='gris'
    
    if  helicóptero.centroX<=0:    
        inicio_playa.visible=False
        playa.visible=True 
        helicóptero.centroX=400
        helicóptero.alFrente()
        #helicóptero.centroX=400
    if helicóptero.centroX>400:
        playa.visible=False
        helicóptero.visible=True 
        helicóptero.centroX =50
        inicio_playa.visible=True
    elif 'izquierda'in keys:    
         helicóptero.centroX-=2  
    elif playa.visible==True:
        basura.visible=True
        espuma.visible=True           
    else:
        playa.visible==False
        basura.visible=False
        espuma.visible=False

cmu_graphics.run()
