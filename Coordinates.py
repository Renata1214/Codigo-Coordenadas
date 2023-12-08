#Librerias que se ocupan
import math
import matplotlib.pyplot as plt


#Variables y listas
lista_de_coordenadas = []
lista_de_coordenadas_x= []
lista_de_coordenadas_y=[]
 # Radio de la Tierra en kilómetros
R = 6371.0


#Abrir documento
file_1 = open("/workspaces/Codigo-Coordenadas/Coordenadas_Prueba_1.txt","r")

#Leer cada linea del documento y guardar en un array
lineas = file_1.readlines()

#Cerrar documento
file_1.close()

for line in lineas[1:]:
    # Split the line into a list of strings
    split_line = line.split()
    
    # Convert each element of the split_line list to an integer
    for x in split_line:
        lista_de_coordenadas.append(int(x))


for z in range(len(lista_de_coordenadas)):
        if z%2==0:
            lista_de_coordenadas_x.append(lista_de_coordenadas[z])
        else:
            lista_de_coordenadas_y.append(lista_de_coordenadas[z])

print (lista_de_coordenadas_x)
print (lista_de_coordenadas_y)

#Calcular la trayectoria funcion
def distancia_Haversine (x1,y1,x2,y2):
    #Transformar de grados a radianes 
    x1_rad=x1*math.pi / 180.0
    y1_rad=y1*math.pi / 180.0
    x2_rad=x2*math.pi / 180.0
    y2_rad=y2*math.pi / 180.0

    disLon = x2_rad-x1_rad
    disLat = y2_rad-y1_rad

    intermediate1 = (pow(math.sin(disLat / 2), 2) + pow(math.sin(disLon / 2), 2) * math.cos(y1_rad) * math.cos(y2_rad))
    
    intermediate2=2 * math.asin(math.sqrt(intermediate1))
    tDistance = R *intermediate2
    return tDistance


# Create a new plot
plt.plot(lista_de_coordenadas_x, lista_de_coordenadas_y)

# Set the title and labels
plt.title('Line Plot Example')
plt.xlabel('X')
plt.ylabel('Y')

# Show the plot
plt.show() 

print (lista_de_coordenadas_x[1])
print(lista_de_coordenadas_y[1])
print(lista_de_coordenadas_x[2])
print(lista_de_coordenadas_y[2])
print(distancia_Haversine(lista_de_coordenadas_x[1],lista_de_coordenadas_y[1],lista_de_coordenadas_x[2],lista_de_coordenadas_y[2]))

#for i in range (len(lista_de_coordenadas_x)):







