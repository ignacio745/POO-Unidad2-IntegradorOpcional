from asyncio import FastChildWatcher
from ClaseProyecto import Proyecto
from ClaseManejadorIntegrantesProyecto import ManejadorIntegrantesProyecto
import csv

class ManejadorProyectos:
    __proyectos = []

    def __init__(self):
        self.__proyectos = []
    

    def cargarCSV(self, nombreArchivo):
        archivo = open(nombreArchivo)
        reader = csv.reader(archivo, delimiter=";")
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                unProyecto = Proyecto(fila[0], fila[1], fila[2])
                self.__proyectos.append(unProyecto)
        archivo.close()
    
    
    
    def calcularPuntosProyectos(self, unManejadorIntegrantesProyecto):
        if isinstance(unManejadorIntegrantesProyecto, ManejadorIntegrantesProyecto):
            for unProyecto in self.__proyectos:
                unProyecto.setPuntos(unManejadorIntegrantesProyecto.calcularPuntaje(unProyecto.getIdentificador()))
    
    
    def listarProyectos(self, unManejadorIntegrantesProyecto):
        self.calcularPuntosProyectos(unManejadorIntegrantesProyecto)
        self.__proyectos.sort(reverse=True)
        print("Datos de los proyectos")
        print("{0:<15}{1:<80}{2:<50}{3}".format("Identificador", "Titulo", "Palabras clave", "Puntos"))
        for unProyecto in self.__proyectos:
            if isinstance(unProyecto, Proyecto):
                print("{0:<15}{1:<80}{2:<50}{3}".format(unProyecto.getIdentificador(), unProyecto.getTitulo(), unProyecto.getPalabrasClave(), unProyecto.getPuntos()))
        