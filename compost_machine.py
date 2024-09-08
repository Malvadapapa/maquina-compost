class CompostMachine:
    def __init__(self,__max_capacity, __composting_time ):
        self.max_capacity = __max_capacity
        self.composting_time = __composting_time
        self.__status = False
        self.__material_amount = 0


    def __str__(self):
        current_status = 'apagada' if self.__status == False else 'encendida'

        return f'La maquina actualmente se encuentra {current_status}\nSu capacidad maxima es de {self.max_capacity} kg\nEl tiempo de procesado para su capacidad maxima es de {self.composting_time} minutos.'
        
    def status(self):
        if self.__status == False:
            return f'El estado actual de la maquina es apagado'
        else:
            return f'El estado actual de la maquina es encendido'

    def turn_on(self):
        if self.__status == True:
            raise ValueError('La maquina ya esta encendida!')
        self.__status = True

    def turn_off(self):
        if self.__status == False:
            raise ValueError('La maquina ya esta apagada!')
        self.__status = False

    @property
    def material_amount(self):
        return f'La cantidad de material que tiene la maquina es: {self.__material_amount} kg. '   

    def add_compost(self, quantity):
        if self.__status:
            raise ValueError('La maquina debe estar apagada para ingresar material')

        if (quantity) > self.max_capacity:
            raise ValueError('La cantidad a ingresar excede la capacidad maxima!')

        if (self.__material_amount + quantity) > self.max_capacity:
            raise ValueError('La maquina ya no puede ingresar mas material!')

        self.__material_amount +=  quantity

    def time_needed_to_process_compost(self):
        processing_time = (self.__material_amount/self.max_capacity) * self.composting_time

        return  round(processing_time, 1)
