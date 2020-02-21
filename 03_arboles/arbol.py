class ArbolBin:
    _nodoID = 0
    _pregunta = ""
    _nodoSi = None
    _nodoNo = None

    def __init__(self, nuevoNodoID, nuevaPregunta):
        self._nodoID = int(nuevoNodoID)
        self._pregunta = str(nuevaPregunta)


class ArbolDecision:
    nodoRaiz = None

    def crearRaiz(self, nuevoNodoID, nuevaPregunta):
        self.nodoRaiz = ArbolBin(nuevoNodoID, nuevaPregunta)
        print("Nodo raíz creado %d " % nuevoNodoID)

    def agregarNodoSi(self, nodoExistenteID, nuevoNodoID, nuevaPregunta):
        if (self.nodoRaiz is None):
            print("ERROR: no hay nodo raíz")
            return

        if (self.buscaArbolAgregarNodoSi(self.nodoRaiz, nodoExistenteID, nuevoNodoID, nuevaPregunta)):
            print(f"Nodo agregado {nuevoNodoID} en respuesta \"si\" del nodo {nodoExistenteID}")
        else:
            print("Nodo {nodoExistenteID} no encontrado")

    def buscaArbolAgregarNodoSi(self, nodoActual, nodoExistenteID, nuevoNodoID, nuevaPregunta):
        if (nodoActual._nodoID == nodoExistenteID):
            if (nodoActual._nodoSi is None):
                nodoActual._nodoSi = ArbolBin(nuevoNodoID, nuevaPregunta)
            else:
                print(f"ADVERTENCIA: Sobreescribio el nodo previo (id={nodoActual._nodoSi.nodoID}) ligado a la respuesta SI del nodo {nodoExistenteID}")
                nodoActual._nodoSi = ArbolBin(nuevoNodoID, nuevaPregunta)
            return True
        else:
            if(nodoActual._nodoSi is not None):
                if(self.buscaArbolAgregarNodoSi(nodoActual._nodoSi, nodoExistenteID, nuevoNodoID, nuevaPregunta)):
                    return True
                else:
                    if(nodoActual._nodoNo is not None):
                        return self.buscaArbolAgregarNodoSi(nodoActual._nodoNo, nodoExistenteID, nuevoNodoID, nuevaPregunta)
                    else:
                        return False
            return False

    def agregarNodoNo(self, nodoExistenteID, nuevoNodoID, nuevaPregunta):
        if (self.nodoRaiz is None):
            print("ERROR: no hay nodo raiz")
            return
        else:
            if (self.buscaArbolAgregarNodoNo(self.nodoRaiz, nodoExistenteID, nuevoNodoID, nuevaPregunta)):
                print(f"Nodo agregado {nuevoNodoID} a la respuesta \"no\" del nodo {nodoExistenteID}")
            else:
                print(f"Nodo {nodoExistenteID} no encontrado")

    def buscaArbolAgregarNodoNo(self, nodoActual, nodoExistenteID, nuevoNodoID, nuevaPregunta):
        if (nodoActual._nodoID == nodoExistenteID):
            if (nodoActual._nodoNo is None):
                nodoActual._nodoNo = ArbolBin(nuevoNodoID, nuevaPregunta)
            else:
                print(f"ADVERTENCIA: Sobreescribio el nodo previo (id={nodoActual._nodoNo._nodoID}) ligado a la respuesta No del nodo {nodoExistenteID}")
            return True
        else:
            if (nodoActual._nodoSi is not None):
                if(self.buscaArbolAgregarNodoNo(nodoActual._nodoSi, nodoExistenteID, nuevoNodoID, nuevaPregunta)):
                    return True
                else:
                    if (nodoActual._nodoNo is not None):
                        return self.buscaArbolAgregarNodoNo(nodoActual._nodoNo, nodoExistenteID, nuevoNodoID, nuevaPregunta)
                    else:
                        return False
            else:
                return False
 
                

    def consultarArbolBin(self, nodoActual=None):
        if (nodoActual is None):
            self.consultarArbolBin(self.nodoRaiz)
            return

        if (nodoActual._nodoSi is None):

            if(nodoActual._nodoNo is None):
                print(nodoActual._pregunta)
            else:
                print(f"ERROR: La respuesta \"SI\" de la pregunta \"{nodoActual._pregunta}\" no existe")

            return

        if (nodoActual._nodoNo is None):
            print(f"ERROR: La respuesta \"NO\" de la pregunta \"{nodoActual._pregunta}\" no existe")
            return

        self.pidePregunta(nodoActual)

    def pidePregunta(self, nodoActual):
        respuesta = input(f"{nodoActual._pregunta} (\"Si\" o \"No\") ")
        respuesta = respuesta.lower()

        if (respuesta == "si"):
            self.consultarArbolBin(nodoActual._nodoSi)
        elif (respuesta == "no"):
            self.consultarArbolBin(nodoActual._nodoNo)
        else:
            print("Debe responder \"Si\" o \"No\")")
            self.pidePregunta(nodoActual)

    def salidaArbolBin(self, tag="", nodoActual=None):
        if (tag == "" and nodoActual is None):
            self.salidaArbolBin("1", self.nodoRaiz)
            return

        if (nodoActual is None):
            return

        print(f"[{tag}] nodoID = {nodoActual._nodoID}, pregunta/respuesta = {nodoActual.pregunta} ")
        self.salidaArbolBin(tag + ".1", nodoActual._nodoSi)
        self.salidaArbolBin(tag + ".2", nodoActual._nodoNo)


def main():
    arbol = ArbolDecision()
    respuesta = ""

    print("Arbol de decisión")
    arbol.crearRaiz(1, "El animal come carne?")
    arbol.agregarNodoSi(1, 2, "El animal tiene rayas?")
    arbol.agregarNodoNo(1, 3, "El animal tiene rayas?")
    arbol.agregarNodoSi(2, 4, "El animal es un tigre")
    arbol.agregarNodoNo(2, 5, "El animal es un leopardo")
    arbol.agregarNodoSi(3, 6, "El animal es una cebra")
    arbol.agregarNodoNo(3, 7, "El animal es un caballo")

    print("Consulta el árbol de decisión")

    while(respuesta != "si"):
        arbol.consultarArbolBin()
        respuesta = input("Salir (si/no) ").lower()


main()
