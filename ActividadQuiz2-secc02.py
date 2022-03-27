"""
Actividad: evaluacion complementaria 2
resolucion ejercicio del VIDEO

Autor: Ronaldo Oviedo 29.635.289
seccion 02 / computacion I

"""
'''
UNA EMPRESA DE ENVIOS NECESITA MANEJAR CIERTA ESTADISTICA DE LOS PAQUETES QUE PROCESA CADA DIA,
PARA ELLO REGISTRA EN EL ARCHIVO envios.txt LA SIG. INFORMACION:
Ciudad de origen, ciudad de destino, Peso del paquete en kg, tipo de envío (1=nacional, 2=internacional)

Desarrolle un programa que cree dos archivos de nombre nacionales.txt e internacionales.txt
con la ciudad de destino

adicional:
1)Ciudad a donde llegó el paquete mas pesado
2)Porcentaje de paquetes enviados que superan los 150kg
3)Cuantos envíos se hicieron a la primera ciudad de destino registrada en el archivo 
'''
#Apertura de Archivos

arch = open('envios.txt','r')

arch1 = open('nacionales.txt', 'w')
arch2 = open('internacionales.txt','w')

#Inicializacion de variables
cont_paquetes = 0
cont_may_150 = 0
B1 = B2 = 0
cont_pd = 0

#Recorrido y Proceso

for registro in arch:
    linea = registro.split(',')
    origen = linea[0]
    destino = linea[1]
    peso = float(linea[2])
    t_envio = int(linea[3])
    
    cont_paquetes += 1
    
    #Impresion en Archivos
    if t_envio == 1:
        arch1.write(destino + '\n')
    
    else:
        arch2.write(destino + '\n')
        
    #Impresion en consola
    #Pregunta 1
    
    if B1 == 0:
        mas_pesado = peso
        destino_mp = destino
        B1 = 1
        
    elif peso > mas_pesado:
        mas_pesado = peso
        destino_mp = destino
    
    #Pregunta 2
        
    if peso > 150:
        cont_may_150 +=1
        
    #Pregunta 3
    
    if B2 == 0:
        primer_destino = destino
        B2 = 1
        cont_pd = 1
        
    elif destino == primer_destino:
        cont_pd += 1
        
#Impresion (Fuera del ciclo)

#Pregunta 1
print('El paquete mas pesado se envió a: ', destino_mp)

#Pregunta 2

if cont_may_150 != 0:
    
    porc = (cont_may_150/cont_paquetes)*100
    print('El ',porc,'% de los paquetes supera los 150kg')

else:
    print('Ningun paquete supera los 150kg')

#Pregunta 3
print('A la primera ciudad de destino se hicieron: ',cont_pd, 'envio(s)')


arch.close()
arch1.close()
arch2.close()

