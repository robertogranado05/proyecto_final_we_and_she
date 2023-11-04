from cmu_graphics import *

    





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


