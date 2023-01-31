class Persona:
    #Constructor
    def __init__(self,nombre,dire,tele,tp):
        self.__nombre = nombre
        self.__dire = dire
        self.__tele = tele
        self.__tp = tp
    #Getter
    def get_Nombre(self):
        return self.__nombre    

    def get_Dire(self):
        return self.__dire
    
    def get_Tele(self):
        return self.__tele

    def get_Tp(self):
        return self.__tp

    #Setters

    def set_Nombre(self, nombre):
        self.__nombre = nombre

    def set_Dire(self, dire):
        self.__dire = dire

    def set_Tele(self, tele):
        self.__tele = tele

    def set_Tp(self, tp):
        self.__tp = tp           
