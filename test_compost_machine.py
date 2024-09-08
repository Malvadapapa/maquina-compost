from compost_machine import CompostMachine
import pytest

def test_inicializacion_componentes():
    primera_compostadora = CompostMachine(5000, 60)
    assert isinstance(primera_compostadora, CompostMachine)
    assert primera_compostadora.max_capacity == 5000
    assert primera_compostadora.composting_time == 60    

def test_representacion_en_str():
    primera_compostadora = CompostMachine(4000, 60)
    str_esperado = 'La maquina actualmente se encuentra apagada\nSu capacidad maxima es de 4000 kg\nEl tiempo de procesado para su capacidad maxima es de 60 minutos.'
    assert str(primera_compostadora) == str_esperado

def test_estado_de_la_maquina():
        primera_compostadora = CompostMachine(4000, 60)
        assert primera_compostadora.status() == 'El estado actual de la maquina es apagado'

def test_estado_de_la_maquina_encedido():
    primera_compostadora = CompostMachine(4000, 60)
    primera_compostadora.turn_on()
    with pytest.raises(ValueError, match= 'La maquina ya esta encendida!'):
        primera_compostadora.turn_on()

def test_estado_de_la_maquina_apagado():
    primera_compostadora = CompostMachine(4000, 60)
    primera_compostadora.turn_on()
    primera_compostadora.turn_off()
    with pytest.raises(ValueError, match= 'La maquina ya esta apagada!'):
        primera_compostadora.turn_off()

def test_cantidad_material():
    primera_compostadora = CompostMachine(4000, 60)
    assert primera_compostadora.material_amount == f'La cantidad de material que tiene la maquina es: 0 kg. '

def test_agregar_material():
    primera_compostadora = CompostMachine(7500, 60)
    primera_compostadora.turn_on()

    with pytest.raises(ValueError, match= 'La maquina debe estar apagada para ingresar material'):
        primera_compostadora.add_compost(50)

    primera_compostadora.turn_off()
    
    with pytest.raises(ValueError, match= 'La cantidad a ingresar excede la capacidad maxima!'):
        primera_compostadora.add_compost(50000)
    
    primera_compostadora.add_compost(7400)
    
    with pytest.raises(ValueError, match= 'La maquina ya no puede ingresar mas material!'):
        primera_compostadora.add_compost(200)

    primera_compostadora.add_compost(50)
    
    assert primera_compostadora.material_amount == f'La cantidad de material que tiene la maquina es: 7450 kg. '

def test_tiempo_para_procesar():
    primera_compostadora = CompostMachine(500, 10)

    primera_compostadora.add_compost(50)
    assert primera_compostadora.time_needed_to_process_compost() == 1

    primera_compostadora.add_compost(100)
    assert primera_compostadora.time_needed_to_process_compost() == 3



primera_compostadora = CompostMachine(500, 10)
print(primera_compostadora)