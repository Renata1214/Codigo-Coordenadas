# Distance Calculation Program

## Project Description
This Python project reads a text file containing geographic coordinates (latitude and longitude), calculates the total distance traveled between these coordinates using the Haversine formula, and generates a plot of the trajectory.

## Libraries Used
math: For mathematical calculations such as converting degrees to radians and calculating distances using the Haversine formula.
matplotlib.pyplot: For creating and displaying the trajectory plot.

## Files
Coordenadas_Prueba_1.txt: A text file containing geographic coordinates. The coordinates should be in degrees and separated by spaces on each line.
Code Structure
Initialization of Variables and Lists:

lista_de_coordenadas: Stores all the coordinates read from the file.
lista_de_coordenadas_x: Stores longitude coordinates.
lista_de_coordenadas_y: Stores latitude coordinates.
Dist_T: Accumulates the total calculated distance.
R: Radius of the Earth in kilometers (constant).

## File Reading:

The file Coordenadas_Prueba_1.txt is opened and all its lines are read.
Each line (except the first) is split into individual components and converted to integers, which are stored in lista_de_coordenadas.
Coordinate Separation:

The coordinates are separated into lista_de_coordenadas_x (longitudes) and lista_de_coordenadas_y (latitudes).
Distance Calculation Using the Haversine Formula:

The function distancia_Haversine is defined to calculate the distance between two given geographic points.
The total distance between the coordinates in the list is calculated and stored in Dist_T.
Plot Generation:

A plot of the trajectory is created using the longitude and latitude coordinates.
Title and labels are added to the plot.
The plot is displayed.

## Example of Coordinate File Format
The Coordenadas_Prueba_1.txt file should have the following format:

mathematica
Copy code
Latitude Longitude
19.432608 -99.133209
19.432701 -99.133300
...
Each line represents a geographic point with latitude and longitude separated by a space.
