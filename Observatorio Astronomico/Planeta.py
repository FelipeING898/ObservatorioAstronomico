from SateliteNatural import sateliteNatural

class planeta:

    def __init__(self, nombre, distanciaMediaSol, excentricidad, periodoOrbitalSinodico, velocidadOrbitalMedia, inclinacion):
        self.__satelites = []
        self.__nombre = nombre
        self.__distanciaMediaSol = distanciaMediaSol
        self.__excentridicad = excentricidad
        self.__periodoOrbitalSinodico = periodoOrbitalSinodico
        self.__velocidadOrbitalMedia = velocidadOrbitalMedia
        self.__inclinacion = inclinacion

    def getNombre(self):
         return self.__nombre
    
    def getExcentricidad(self):
         return self.__excentridicad
    
    def setExcentricidad(self, excentridicad):
        self.__excentridicad = excentridicad
    
    def getInclinacion(self):
        return self.__inclinacion
    
    def setInclinacion(self, inclinacion):
        self.__inclinacion = inclinacion

    def agregarSateliteNatural(self, nombre, excentricidad, inclinacion):
        confirmacion = False
        nuevo = sateliteNatural(nombre, excentricidad, inclinacion) 
        self.__satelites.append(nuevo)
        if nuevo is not None:
            confirmacion = True
        return confirmacion
    
    def eliminarSatelites(self, nombre):
        self.__satelites.remove(nombre)

    def getSatelites(self, nombre):
        return self.__satelites(self.__satelites.index(nombre))
    
    def editarSateliteNatural(self, nombre, excentricidad, inclinacion):
        for satelite in self.__satelites:
            if satelite.getNombre() == nombre:
                satelite.getExcentricidad() == excentricidad
                satelite.getInclinacion() == inclinacion

        

