# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

"""
En este script van a haber un predador y una presa, la dinamica de la poblacion 
dependera del indice de mortalidad de ambos y de la relacion predador presa
"""

"""
En primera instancia voy a definir mis clases. Predador y Presa.
Ambas tienen definidos tamaños poblacionales iniciales.
Existe un territorio en el cual interaccionan, ese territorio esta construido por una matriz de ceros.
En cuyo caso no hay animales de ningun tipo presente.
Los animales pueden moverse a traves de la matriz. En el caso de que coincidan las posiciones de ambos animales en la matriz, 
el predador tiene la posibilidad de eliminar a la presa.
Al incio de la simulacion los animales empiezan en una posicion random de lo matriz.
Aca se abren dos posibilades.
1. Que la simulacion funcione como una imagen instante a instante, generando diferentes posiciones
random en la matriz y que calcule el numero de coincidencias entre animales. 
Yo en esta caso seteo el numero de matrices generadas y a cada momento calculo los indicies poblacionales.
2. Que la simulacion incluya un parametro temporal y cada x tiempo los animales se mueven de
a una celda a la vez, y calcula al final del tiempo de la simulacion como se modificaron 
los parametros poblacionales

"""
import numpy as np
import random

class Predador():
    def __init__(self, N, X, genero): #N es la poblacion inicial, X es el numero de presas que debe comer por dia para sobrevivir.
        self.N=0
        self.X=0
        self.genero=None
    def agregar(N):
        self.N=#Ecuacion que define en un instante de tiempo el numero de predadores que hay.
        
        
class Presa():
    def __init__(self, N, genero):
        self.N=0
        self.genero=None
        
    def agregar(N):
        N
        self.N=#Ecuacion que define en un instante de tiempo el numero de presas que hay.

class Territorio():
    def __init__(self, filas, columnas, territorio):
#Es una matriz con i filas y j columnas
        self.territorio=np.zeros(filas,columnas, dtype=int)
        """
Defino la distribucion inicial de los animales. Tengo tres opciones, que haya una presa,
que haya un predador, o que el espacio este vacio.
No voy a definir cantidades iguales de espacio vacio, presas y predadores.
El 50% del espacio va a estar vacio. El 30% van a ser presas, y el 20%Predadores.
    """
        for i in range (len(territorio)):
            for j in range(len(territorio[,:])):
                categ=random.range(1,10)
                if categ<=3:
                    self.territorio[i,j]="Presa"
                elif categ>5:
                    self.territorio[i,j]=0
                else:
                    self.territorio[i,j]="Predador"
        
        
        