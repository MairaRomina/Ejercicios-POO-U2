class Viajero:
    __numViajero: int
    __dni: str
    __nombre: str
    __apellido: str
    __millasAcum: int
    
    def __init__(self, numViajero, dni, nombre, apellido, millasAcum):
        self.__numViajero = numViajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasAcum = millasAcum
        
    def __str__(self):
        return ('Numero viajero: {} - Dni: {} - Nombre y Apellido: {} {} - Millas: {}'.format(self.__numViajero,self.__dni,self.__nombre,self.__apellido,self.__millasAcum))
        
    def getIdentificador (self):
        return self.__numViajero
    
    def cantidadTotalMillas (self):
        return self.__millasAcum
    
    def acumMillas (self):
        acum = int(input('Ingrese cantidad de millas recorridas que desea acumular: '))
        if type( acum ) == int: 
            self.__millasAcum += acum
            print('Valor actualizado, cantidad de millas actuales: ', self.__millasAcum)
            return self.__millasAcum
        else:
            print('Error de tipo en acumular millas')
        
    def canjearMillas (self):
        cant = int(input('Ingrese la cantidad de millas que desea canjear: '))
        if type( cant ) == int:
            if self.__millasAcum >= cant:
                self.__millasAcum -= cant
                print('Valor actualizado, cantidad de millas actuales: ', self.__millasAcum)
                return self.__millasAcum
            else:
                print('Error en la operacion')
        else:
            print('Error de tipo en canjear millas')