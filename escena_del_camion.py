from cmu_graphics import *

escena1=Grupo(
        Rect(0, 0, 400, 250, relleno=gradiente('azulCieloProfundo', 'azulCieloClaro', inicio='superior')),


        
        Circulo(35,202,10),
        
        Linea(35,200,35,230),
        
        Linea(35,230,30,250),
        
        Linea(35,230,42,250),
        
        Linea(35,217,30,232),
        
        Linea(35,217,41,232),


        Rect(0, 250, 400, 150, relleno=gradiente('cespedVerde', 'verde', 'cespedVerde',
                                     'cespedVerde', 'verde', inicio='superior')),

        Linea(360,260,360,240,anchuraDeLinea=5,relleno='marron'),
        Rect(335,220,48,20,relleno='marron'),
        Rotulo('Fabrica',360,230,italica=True,negrito=True),

        Rect(0, 275, 400, 100, relleno=gradiente('grisOscuro', 'grisTurbio', inicio='superior')),

        Linea(0,325,400,325,anchuraDeLinea=3,guion=True, relleno='blanco'),

        
        
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
        
        Rotulo('Basura',165,277,relleno='blanco',italica=True,negrito=True,tamaño=17),
        
        Rect(245,297,9,5,relleno='amarillo')
 )
def enTeclaPresionada(tecla):

    if (tecla == 'd'):
        Camion.centroX+=20
    elif (Camion.centroX==400):
        Camion.centroX=-200
    elif (tecla == 'a'):
        Camion.centroX-=20
    if (Camion.centroX>=450):
        Camion.visible=Falso
        escena1.visible=Falso
cmu_graphics.run()      
                
