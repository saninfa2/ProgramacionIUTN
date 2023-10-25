import pytest
from funcionesTest import *
   
#test funcion medir_ultima_palabra - TEST 1
def test_medir_ultima_palabra():
    assert medirUltimaPalabra("hola como estas") == len("estas")
    assert medirUltimaPalabra("hola") == len("hola")
    assert not medirUltimaPalabra("hola") == len("holas")
    
    
#test funcion definirIdentificador - TEST 2
def test_definir_identificador():
    assert definirIdentificador("Sabina ", "Fabrega", "44746656") == "Sabina7447"
    assert definirIdentificador("Juan ", "Boe", "12345566") == "Juan3123"
    assert definirIdentificador("Lupe ", "Linguini", "00123001") == "Lupe8001"
    assert not definirIdentificador("Lupe ", "Linguini", "00123001") == "Lup4001"
 
#TEST 3   
def test_verificar_multiplo():
    numero1 = 8
    numero2= 3
    numero3 = 14
    numero4 = 7
    numero5 = 0
    assert not verificarMultiplo(numero1, numero2) == False
    assert verificarMultiplo(numero3, numero4) == True
    assert not verificarMultiplo(numero5, numero1) == False
    
# test de agregar espaciado - TEST 4
def test_agregar_espaciado():
    assert agregarEspaciado("hello") == "h e l l o "
    assert not agregarEspaciado("hello") == "b a y"
    assert agregarEspaciado(" ") == "  "
    
#test de square - TEST 5
def test_square():
    assert square(9)==81
    assert square(-9)==81
    assert not square(9)==-81
    
# test de la funcion vector_modulus - TEST 6
def test_modulos_of_vector():
    assert vector_modulus((3,4)) == 5
    assert not vector_modulus((3,4)) == 25
    
#test de numero primo - TEST 7
def test_is_prime():
    number_prime = 2
    number_prime2 = 4
    assert numberPrime(number_prime) == True
    assert not numberPrime(number_prime) == False
    assert numberPrime(number_prime2) == False
    
#test de frecuencia de un digito en un número - TEST 8
def test_count_occurrence():
    number_occurrence = 122222
    digit = 2
    assert countOccurrence(number_occurrence, digit) == 5
    assert not countOccurrence(number_occurrence, digit) == False
    
#test de sumar los digitos de un numeros entero - TEST 9
def test_sum_digits():
    assert sumOfDigit(14) == 5
    assert not sumOfDigit(14) == 0
    assert sumOfDigit(44746656) == 42

#test calcular temperatura media dada temperatura maxima y minima
def test_temperature_media():
    maxTemp = 30.0
    minTemp = -2.0
    assert mediarTemperatura(maxTemp, minTemp) == (maxTemp+minTemp)/2  
    assert not mediarTemperatura(maxTemp, minTemp) == (maxTemp+minTemp)/3