from cmu_graphics import*


Rect(0,0,400,200,relleno=gradiente('azulCielo','amarillo',inicio='superior'),opacidad=50)
Círculo(200,200,50,relleno=gradiente('amarillo','naranja',inicio='superior'))
Rect(0,300,400,100,relleno='blancoNaranja')
Polígono(0,200,400,200,400,300,353,324,313,305,243,299,0,300,relleno='azulCieloProfundo')

palaIzquierda = Polígono(190, 165, 130, 155, 130, 165, relleno='grisClaro')
palaDerecha = Polígono(205, 165, 265, 155, 265, 165, relleno='gris')

helicóptero = Grupo(
    Óvalo(200, 200, 100, 50, rotarÁngulo=-5),
    Círculo(200, 165, 8),
    Polígono(190, 180, 192, 165, 208, 165, 210, 175),
    Polígono(235, 185, 245, 205, 320, 190, 320, 180),
    Polígono(325, 205, 330, 195, 325, 180, 330, 160, 325, 155, 320, 170, 315, 185)
    )
helicóptero.relleno ='azul'

helicóptero.agregar(
    Polígono(185, 180, 165, 190, 155, 205, 180, 200, relleno='agua'),
    Polígono(190, 180, 210, 180, 215, 200, 185, 200, relleno='agua'),
    Óvalo(168, 193, 36, 12, relleno=gradiente('azur', 'agua', 'agua'), rotarÁngulo=-35),
    Línea(180, 220, 170, 235, relleno=rgb(70, 75, 75)),
    Línea(210, 220, 220, 235, relleno=rgb(70, 75, 75)),
    Línea(145, 235, 250, 235, relleno=rgb(70, 75, 75), anchuraDeLínea=3),
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
    
    if  helicóptero.centroX<0:    
        huerta.visible=True  
        helicóptero.alFrente()
        helicóptero.centroX=400
    elif helicóptero.centroX>500:
        huerta.visible=False
        helicóptero.visible=True 
        helicóptero.centroX =50
    elif 'izquierda'in keys:    
         helicóptero.centroX-=2             
cmu_graphics.run()