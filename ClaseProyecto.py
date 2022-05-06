class Proyecto:
    __idProyecto = ""
    __titulo = ""
    __palabrasClave = ""
    __puntos = 0

    def __init__(self, idProyecto = "", titulo = "", palabrasClave = ""):
        self.__idProyecto = idProyecto
        self.__titulo = titulo
        self.__palabrasClave = palabrasClave
        self.__puntos = 0

    
    def getIdentificador(self):
        return self.__idProyecto

    def getTitulo(self):
        return self.__titulo
    
    def getPalabrasClave(self):
        return self.__palabrasClave
    
    def setPuntos(self, puntos):
        if isinstance(puntos, int):
            self.__puntos = puntos
    
    def getPuntos(self):
        return self.__puntos


    def __gt__(self, otro):
        print("Mayor que")
        retorno = False
        if isinstance(otro, Proyecto):
            retorno = self.getPuntos() > otro.getPuntos()
        return retorno
    
    def __eq__(self, otro):
        print("Igual que")
        retorno = False
        if isinstance(otro, Proyecto):
            retorno = self.getPuntos() == otro.getPuntos()
        return retorno
    
    def __lt__(self, otro):
        print("Menor que")
        retorno = False
        if isinstance(otro, Proyecto):
            retorno = self.getPuntos() < otro.getPuntos()
        return retorno
    
    def __le__(self, otro):
        print("menor o igual que")
        return self < otro or self == otro