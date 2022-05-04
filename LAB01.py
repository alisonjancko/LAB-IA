
ACCIONES = {'hayAves':'Sonido Espanta Aves',
'hayInsectos':'Sonido Espanta Insectos',
'hayPlagas':'Repelente para Plagas'}

class AgenteEspanta:
    """Constructor recibe acciones"""
    def __init__(self, acciones):
        self.acciones = acciones
        self.percepciones = ''

    def actuar(self, percepcion, accion_basica=''):
        """Actua segun la percepcion, devolviendo una acccion"""
        if not percepcion:
            return accion_basica
        if len(self.percepciones)!=0:
            self.percepciones+= ','
        self.percepciones += percepcion
        if self.percepciones in self.acciones.keys():
            return self.acciones[self.percepciones]
        self.percepciones = ''
        return accion_basica

print("-- Agente espanta aves, insectos u otro tipo de plagas en un sembradio --")
espanta = AgenteEspanta(ACCIONES)
percepcion = input("Indicar Percepcion: ")
while percepcion:
    accion = espanta.actuar(percepcion,'reiniciarse')
    print(accion)
    percepcion = input("Indicar Percepcion: ")