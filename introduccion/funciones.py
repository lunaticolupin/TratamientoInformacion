def apply_IVA(precio, porcentaje):
    '''
    Función que aplica un IVA a una cantidad.
    Parámetros:
        precio: Es un valor real con el precio al que aplicar el IVA.
        porcentaje: Es el porcentaje del IVA a aplicar.
    Devuelve:
        El precio final tras aplicar el IVA.
    '''
    return precio + precio * porcentaje / 100


def apply_discount(precio, descuento):
    return precio - descuento


def precio_basket(basket, function):
    '''
    Función que calcula el precio de una cesta de la compra una vez aplicada
    una función a los precios iniciales.
    Parámetros:
        basket: Es un diccionario formado por pares precio:descuento.
        function: Es una función que toma dos valores reales y devuelve otro.
        Normalmente para aplicar descuentos o IVA.
    Devuelve:
        El precio final de la cesta de la compra una vez aplicada la función
        sobre los precios iniciales.
    '''
    total = 0
    for precio, discount in basket.items():
        total += function(precio, discount)
    return total


print('El precio de la compra tras aplicar los descuentos es: ', precio_basket({1000: 20, 500: 10, 100: 1}, apply_discount))
print('El precio de la compra tras aplicar el IVA es: ', precio_basket({1000: 20, 500: 10, 100: 1}, apply_IVA))
