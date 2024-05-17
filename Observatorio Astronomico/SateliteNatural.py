class sateliteNatural:

    def __init__(self, nombre, excenticidad, inclinacionOrbital):
        self.__nombre = nombre
        self.__excentricidad = excenticidad
        self.__inclinacionOrbital = inclinacionOrbital

    def getNombre(self):
        return self.__nombre
    
    def getExcentridad(self):
        return self.__excentricidad

    def setExcentricidad(self, excentricidad):
        self.__excentricidad = excentricidad
    
    def getInclinacion(self):
        return self.__inclinacionOrbital
    
    def setInclinacion(self, inclinacion):
        self.__inclinacionOrbital = inclinacion

