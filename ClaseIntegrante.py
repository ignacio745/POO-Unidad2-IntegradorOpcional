class Integrante:
    __idProyecto = ""
    __apellidoNombre = ""
    __dni = ""
    __categoriaInvestigacion = ""
    __rol = ""

    def __init__(self, idProyecto, apellidoNombre, dni, categoriaInvestigacion, rol):
        self.__idProyecto = idProyecto
        self.__apellidoNombre = apellidoNombre
        self.__dni = dni
        self.__categoriaInvestigacion = categoriaInvestigacion
        self.__rol = rol
    

    def getIdProyecto(self):
        return self.__idProyecto
    
    def getApellidoNombre(self):
        return self.__apellidoNombre
    
    def getDNI(self):
        return self.__dni
    
    def getCategoriaInvestigacion(self):
        return self.__categoriaInvestigacion
    
    def getRol(self):
        return self.__rol
    
    