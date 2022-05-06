from ClaseIntegrante import Integrante
import csv
import numpy as np

class ManejadorIntegrantesProyecto:
    __cantidad = 0
    __dimension = 20
    __incremento = 5
    __integrantes = None


    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 20
        self.__incremento = 5
        self.__integrantes = np.empty(20, dtype=Integrante)
    
    def agregarIntegrante(self, unIntegrante):
        if isinstance(unIntegrante, Integrante):
            if self.__cantidad == self.__dimension:
                self.__dimension += self.__incremento
                self.__integrantes.resize(self.__dimension)
            self.__integrantes[self.__cantidad] = unIntegrante
            self.__cantidad += 1
        else:
            print("[ERROR] Solo se pueden agregar integrantes del proyecto")



    
    def cargarCSV(self, nombreArchivo):
        archivo = open(nombreArchivo)
        reader = csv.reader(archivo, delimiter=";")
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                unIntegrante = Integrante(fila[0], fila[1], fila[2], fila[3], fila[4])
                self.agregarIntegrante(unIntegrante)
        archivo.close()
    
    def getNumeroIntegrantes(self, idProyecto):
        i = 0
        total = 0
        while i < self.__cantidad:
            if self.__integrantes[i].getIdProyecto() == idProyecto:
                total += 1
            i += 1
        return total
    

    def checkMiembro(self, idProyecto, rol, categorias = ["I", "II", "III", "IV", "V"]):
        i = 0
        while i < self.__cantidad and (self.__integrantes[i].getIdProyecto() != idProyecto or self.__integrantes[i].getRol() != rol or (self.__integrantes[i].getCategoriaInvestigacion() not in categorias)):
            i += 1
        return i < self.__cantidad
    
    
    def calcularPuntaje(self, idProyecto):
        print("Calculando puntaje del proyecto {0}".format(idProyecto))
        puntaje = 0
        if self.getNumeroIntegrantes(idProyecto) >= 3:
            puntaje += 10
        else:
            puntaje -= 20
            print("El proyecto debe tener como minimo 3 integrantes")
        
        if self.checkMiembro(idProyecto, "director", ["I", "II"]):
            puntaje += 10
        else:
            puntaje -= 5
            print("El director del proyecto debe tener categoria I o II")
        
        if self.checkMiembro(idProyecto, "codirector", ["I", "II", "III"]):
            puntaje += 10
        else:
            puntaje -= 5
            print("El codirector del proyecto debe tener como minimo categoria III")
        
        if not self.checkMiembro(idProyecto, "director"):
            puntaje -= 10
            print("El proyecto debe tener un director")
        
        if not self.checkMiembro(idProyecto, "codirector"):
            puntaje -= 10
            print("El proyecto debe tener un codirector")
        
        return puntaje