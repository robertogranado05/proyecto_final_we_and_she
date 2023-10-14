from cmu_graphics import *
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



humano= Grupo(
        Rect(0, 0, 400, 250, relleno=gradiente('azulCieloProfundo', 'azulCieloClaro', inicio='superior')),
        Circulo(35,202,10),
        
        Linea(35,200,35,230),
        
        Linea(35,230,30,250),
        
        Linea(35,230,42,250),
        
        Linea(35,217,30,232),
        
        Linea(35,217,41,232),
        
        Rect(0, 250, 400, 150, relleno=gradiente('cespedVerde', 'verde', 'cespedVerde'))

)
Letrero=Grupo(
        Linea(360,260,360,240,anchuraDeLinea=5,relleno='verde'),
        Rect(335,220,48,20,relleno='Verde'),
        Rotulo('fabrica',360,230),
        Rect(0, 275, 400, 100, relleno=gradiente('grisOscuro', 'grisTurbio', inicio='superior')),
          Linea(0,325,400,325,anchuraDeLinea=3,guion=True, relleno='blanco')
)


Camion=Grupo(
        
        Rect(120,250,100,60,relleno='gainsboro',borde='negro'),
        
        Poligono(128,260,210,260,210,295,128,295,relleno='oro',borde='negro'),
        
        Círculo(140, 310, 11),
        
        Círculo(140, 310, 5,relleno='blanco'),
        
        Linea(135,307,145,313,anchuraDeLinea=1),

        Círculo(202, 310, 11),

        Círculo(202, 310, 5,relleno='blanco'),

        Poligono(120,250,95,275,95,315,110,315,120,310,relleno='blanco',borde='negro'),

        Rect(220,270,35,40,relleno='gainsboro',borde='negro'),

        Rect(235,277,15,15),

        Rotulo('-',230,297),

        Rect(245,297,9,5,relleno='amarillo')

)
MESAJE=Group(
        Rotulo('Para Saltar Escena Presione Espacio ',200,120,tamaño=20,relleno='blanco',italica=True,negrito=True)
)     
def enTeclaPresionada(tecla):

     if (tecla == 'd'):
        Camion.centroX+=20
     elif (Camion.centroX==400):
        Camion.centroX=-200
     elif (tecla == 'a'):
        Camion.centroX-=20
    



fondo1=Group(
          Círculo(0, 0, 70, relleno=gradiente('naranja', 'amarillo')),

          Línea(10, 75, 10, 155, relleno=gradiente('amarillo',  'azulCielo', inicio='superior'),anchuraDeLínea=5,guion=True),


          Línea(35, 70, 75, 140, relleno=gradiente('amarillo',  'azulCielo', inicio='superior'),
          anchuraDeLínea=5,guion=True),

          Línea(55, 55, 125, 100, relleno=gradiente('amarillo',  'azulCielo', inicio='superior'),
          anchuraDeLínea=5,guion=True),

          Línea(70, 30, 145, 50, relleno=gradiente('amarillo',  'azulCielo', inicio='superior'),
          anchuraDeLínea=5,guion=True),

          Línea(75, 5, 155, 5, relleno=gradiente('amarillo',  'azulCielo', inicio='superior'),
          anchuraDeLínea=5,guion=True),
)
playa=Group(
          Poligono(0,230,400,0,400,200,240,240,0,280,fill=gradiente('madera','trigo'),borde='negro'),
          Línea(0,230,400,80,fill='tierra',anchuraDeLínea=8),
          Poligono(0,0,400,0,400,80,0,230,fill=gradiente('azur','lavanda','azulCieloProfundo',inicio='superior')),
          Poligono(0,280,240,240,400,200,400,400,0,400,fill=gradiente('azulAlica','azul','azulMarino',inicio='superior'))
)
#sol
sol=Group(
          Línea(400,0,290,20,fill=gradiente('amarillo','oro'),guión=True),
          Línea(400,0,320,50,fill=gradiente('amarillo','oro'),guión=True),
          Línea(400,0,300,40,fill=gradiente('amarillo','oro'),guión=True),
          Línea(400,0,330,70,fill=gradiente('amarillo','oro'),guión=True),
          Línea(400,0,290,5,fill=gradiente('amarillo','oro'),guión=True),
          Línea(400,0,360,80,fill=gradiente('amarillo','oro'),guión=True),
          Línea(400,0,390,80,fill=gradiente('amarillo','oro'),guión=True),
          Circulo(400,0,50,fill=gradiente('amarillo','oro'))
)
nube=Group(
          Circulo(120,40,20,fill=gradiente('azur','blanco')),
          Circulo(160,20,30,fill=gradiente('azur','blanco')),
          Circulo(200,40,20,fill=gradiente('azur','blanco')),
          Circulo(210,50,30,fill=gradiente('azur','blanco')),
          Circulo(160,80,30,fill=gradiente('azur','blanco')),
          Circulo(120,80,30,fill=gradiente('azur','blanco')),
          Circulo(160,50,30,fill=gradiente('azur','blanco')),

          Circulo(280,80,30,fill=gradiente('azur','blanco')),
          Circulo(300,60,30,fill=gradiente('azur','blanco')),
          Circulo(330,70,30,fill=gradiente('azur','blanco')),
          Circulo(260,80,30,fill=gradiente('azur','blanco')),
          Circulo(320,80,30,fill=gradiente('azur','blanco'))
)


helicóptero= Grupo(
                  Polígono(185, 180, 165, 190, 155, 205, 180, 200, relleno='azul'),
                  Polígono(190, 180, 210, 180, 215, 200, 185, 200, relleno='azul'),
                  Óvalo(168, 193, 36, 12, relleno=gradiente('azur', 'agua', 'agua'), rotarÁngulo=-35),
                  Línea(180, 220, 170, 235, relleno=rgb(70, 75, 75)),
                  Línea(210, 220, 220, 235, relleno=rgb(70, 75, 75)),
                  Línea(145, 235, 250, 235, relleno=rgb(70, 75, 75), anchuraDeLínea=3),
                  #palaIzquierda, palaDerecha
                  Rect(120,284,150,70,relleno=None,borde='negro'),
                  Linea(145,235,120,284),
                  Linea(250,235,270,284),
                  Circulo(138,338,5),
                  Rect(156,336,10,10),
                  Circulo(188,346,5),
                  Rect(212,326,10,20,relleno='verde',borde='negro'),
                  Rect(182,317,10,20,relleno='rojo', borde='negro'),
                  Rect(235,329,30,20,relleno='blanco',borde='negro'),
                  Circulo(249,338,5,relleno=None,borde='negro'),
                  Rect(138,305,30,20,relleno='verde',borde='negro'),
                  Óvalo(200, 200, 100, 50, rotarÁngulo=-5),
                  Círculo(200, 165, 8),
                  Polígono(190, 180, 192, 165, 208, 165, 210, 175),
                  Polígono(235, 185, 245, 205, 320, 190, 320, 180),
                  Polígono(325, 205, 330, 195, 325, 180, 330, 160, 325, 155, 320, 170, 315, 185)
                  
                  
                  
  )

helicóptero.centroY=100  
def enTeclaPrecionada(keys): 
    
    if 'izquierda'in keys:
        helicóptero.centroX-=2
    
    
    
    if palaDerecha.relleno=='gris':
       palaIzquierda.relleno=='pink'
       palaDerecha.relleno='gris'
    else:
        palaDerecha.relleno=='pink'
        palaIzquierda.relleno='gris'
        palaDerecha.relleno='pink'    
       
def enTeclaRetenida(tecla):
    if 'izquierda' in tecla:
       helicóptero.centroX-=2
       helicóptero.rotarÁngunlo=-15
    if 'derecha' in tecla :
       helicóptero.centroX+=2
       helicóptero.rotarÁngulo=-15
    if 'abajo' in tecla:
        helicóptero.centroY+=2
        helicóptero.rotarÁngulo=15
    if 'arriba'in tecla:
        helicóptero.rotarÁngulo=-15
    if  'arriba'in tecla and 'Derecha':
         helicóptero.rotarÁngulo=15
    if  'arriba'in tecla and 'izquierda' in tecla:
         helicóptero.rotarÁngulo=15
    if   'abajo' in tecla and 'izquierda'in tecla:
         helicóptero.rotarÁngulo=-15


Palmera=Group(
    
          Poligono(0,280,20,240,40,160,60,160,60,240,80,267,fill="tierra",borde='marrónCuero',anchuraDeBorde=4),
          Poligono(50,160,55,120,50,70,60,60,80,40,100,80,90,90,80,120,50,160,fill='limaVerde',borde='verdeOscuro'),
          Poligono(50,160,50,120,40,100,50,80,40,60,40,40,0,40,0,120,10,160,10,200,50,160,fill='limaVerde',borde='verdeOscuro'),
          Poligono(50,160,80,130,90,90,130,90,120,150,90,155,50,160,fill='limaVerde',borde='verdeOscuro'),
          Poligono(50,160,100,165,120,175,130,220,80,200,50,160,fill='limaVerde',borde='verdeOscuro'),
          Línea(50,160,80,40,fill='verdeOscuro'),
          Línea(50,160,0,40,fill='verdeOscuro'),
          Línea(50,160,130,220,fill='verdeOscuro'),
          Línea(50,160,130,90,fill='verdeOscuro'),
          Circulo(40,160,10,fill='naranjaMarrón',borde='negro'),
          Circulo(60,160,10,fill='naranjaMarrón',borde='negro'),
          Circulo(50,170,10,fill='naranjaMarrón',borde='negro')
)
#espumaDelMar
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
def enRatónMovido(x,y):
     if   nube.centroX<=400:
          nube.centroX+=5
     else:
        nube.centroX=5
        
#basura
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
#tarroDeBasura}
Tarro=Group(
          Poligono(400,200,370,200,360,165,400,165,400,200,fill='verde',borde='verdeOscuro'),
          Línea(360,165,400,165,fill='verdeOscuro',anchuraDeLínea=3),
          Poligono(360,165,360,155,400,130,400,165,fill='verdeOscuro',borde='negro'),
          Circulo(385,155,12),
          Línea(385,155,375,140,fill='blanco',anchuraDeLínea=5),
          Línea(385,155,375,150,fill='blanco',anchuraDeLínea=5),
          Poligono(360,200,350,215,360,240,365,215,360,200,fill='grisPizarra'),
          Circulo(360,200,5),
          Poligono(330,170,360,170,340,180),
          Poligono(340,180,320,180,320,200,330,215,360,200,340,180),
          Circulo(340,180,5),
          Ovalo(120,240,20,15,fill='tierra',borde='marrón'),
          Ovalo(360,120,20,15,fill='tierra',borde='marrón'),
          Ovalo(280,200,20,15,fill='tierra',borde='marrón'),
          Ovalo(240,220,20,15,fill='tierra',borde='marrón'),
          Ovalo(160,200,20,15,fill='tierra',borde='marrón'),
)
humano1= Grupo(
        
        Circulo(35,202,10),
        
        Linea(35,200,35,230),
        
        Linea(35,230,30,250),
        
        Linea(35,230,42,250),
        
        Linea(35,217,30,232),
        
        Linea(35,217,41,232),
)
humano1.centroY=180
humano1.centroX=200
basura3=Circle(210,190,9)

#ol.visible=False
#nube.visible=False
#Palmera.visible=False
#espuma.visible=False
#basura.visible=False
#Tarro.visible=False
#playa.visible=False
humano.visible=True

def enTeclaPresionada(tecla):

     if (tecla == 'e'):
        humano1.centroX+=20
        basura3.visible=False
        #basura3.centro+=20
     elif (humano1.centroX==100):
        humano1.visible=False
        basura3.visible=False
        sol.visible=False
        nube.visible=False
        Palmera.visible=False
        espuma.visible=False
        basura.visible=False
        Tarro.visible=False
        playa.visible=False
     elif (tecla == 'q'):
        humano1.centroX-=20
        basura3.centroX-=20
     if (tecla == 'd'):
        Camion.centroX+=20
     elif (Camion.centroX==400):
        Camion.centroX=-200
     elif (tecla == 'a'):
        Camion.centroX-=20
     elif (Camion.centroX==100):
         humano.visible=False
         Letrero.visible=False
         Camion.visible=False
     if (tecla=='espacio'):
         humano.visible=False
         Letrero.visible=False
         Camion.visible=False
         MESAJE.visible=False
         fabrica.visible=True




cmu_graphics.run()


