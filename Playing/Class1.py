#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 18:44:11 2021

@author: diegobarbosa
"""
class edificacion:
    altura=0
    dueno=""
    precio=0
    ubicacion=""
    
    def __init__(self, altura, dueno, precio, ubicacion):
        self.altura=altura
        self.dueno=dueno
        self.precio=precio
        self.ubicacion=ubicacion
    def defAltura(self, altura):
        self.altura=altura

    def defDueno(self, altura):
        self.dueno=dueno

    def defPrecio(self, altura):
        self.precio=precio
        
    def defUbicacion(self, altura):
        self.ubicacion=ubicacion
        
    def gimmeAltura(self):
        return self.altura
      
    def gimmeDueno(self):
        return self.dueno
    
    def gimmePrecio(self):
        return self.precio
    
    def gimmeUbicacion(self):
        return self.ubicacion
    
edificio=edificacion(100, "Diego" ,1200, "Bogota")
print("Altura: ", edificio.gimmeAltura()," Dueño: ",edificio.gimmeDueno(), " Precio: ", 
      edificio.gimmePrecio(), " Ubicación: ", edificio.gimmeUbicacion() )

class casa(edificacion):
    habitantes=0
    def __init__(self, altura, dueno, precio, ubicacion, habitantes):
        super().defAltura(altura)
        super().defDueno(dueno)
        super().defPrecio(precio)
        super().defUbicacion(ubicacion)
        
    def gimmeHabitantes(self):
        return self.habitantes
    
casa1=casa(10, "Lala", 500, "Fusa", 3)   
print("Habitantes: ",casa1.gimmeHabitantes(), " Altura: " ,casa1.gimmeAltura())   
    