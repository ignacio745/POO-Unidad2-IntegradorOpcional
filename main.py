from ClaseManejadorProyectos import ManejadorProyectos
from ClaseManejadorIntegrantesProyecto import ManejadorIntegrantesProyecto


if __name__ == "__main__":
    unManejadorProyectos = ManejadorProyectos()
    unManejadorIntegrantesProyecto = ManejadorIntegrantesProyecto()
    
    unManejadorProyectos.cargarCSV("proyectos.csv")
    unManejadorIntegrantesProyecto.cargarCSV("integrantesProyecto.csv")

    unManejadorProyectos.listarProyectos(unManejadorIntegrantesProyecto)