from Planeta import planeta

class observatorio:

    CANTIDAD_PLAN = 8
    NOMBRES_PLANETAS ={
        "MERCURIO": "Mercurio",
        "VENUS": "Venus",
        "TIERRA": "Tierra",
        "MARTE": "Marte",
        "JUPITER": "Jupiter",
        "SATURNO": "Saturno",
        "URANO": "Urano",
        "NEPTUNO": "Neptuno"
    }

    def __init__(self):
        self.__planetas= []

    def getNombrePlanetas(self):
        nombrePlanetas = []
        for nombre in self.NOMBRES_PLAN.items():
            keys = nombre(0)
            nombrePlanetas.append(keys)
        return nombrePlanetas
    
    def getSateliteNaturalNombre(self, nombre):
        planeta.getSatelite(nombre)
    
    def getPlanetaPorDistancia(self, distancia):
        planeta.getSatelite(distancia)

    def getPlanetaPorInclinacion(self, inclinacion):
        planeta.getSatelite(inclinacion)

    def agregarSateliteNatural(self, nombre, excentricidad, inclinacion):
        planeta.agregarSateliteNatural(nombre, excentricidad, inclinacion)
        return planeta.agregarSateliteNatural(nombre, excentricidad, inclinacion)
        
    def eliminarSatelite(self, nombre):
        planeta.eliminarSatelites(nombre)

    def editarSatelite(self, nombre, excentricidad, inclinacion):
        planeta.editarSateliteNatural(nombre, excentricidad, inclinacion)
        