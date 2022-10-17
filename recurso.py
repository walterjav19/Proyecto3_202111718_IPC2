class Recurso:
    def __init__(self,id,nombre,abreviatura,metrica,tipo,valor):
        self.id=id
        self.nombre=nombre
        self.abreviatura=abreviatura
        self.metrica=metrica
        self.tipo=tipo
        self.valor=float(valor)

    def get_id(self):
        return self.id

    def set_id(self,id):
        self.id=id

    def get_nombre(self):
        return self.nombre

    def set_id(self,nombre):
        self.nombre=nombre        

    def get_abreviatura(self):
        return self.abreviatura

    def set_abreviatura(self,abreviatura):
        self.abreviatura=abreviatura

    def get_metrica(self):
        return self.metrica

    def set_metrica(self,metrica):
        self.metrica=metrica          
    
    def get_tipo(self):
        return self.tipo

    def set_tipo(self,tipo):
        self.tipo=tipo

    def get_valor(self):
        return self.valor

    def set_valor(self,valor):
        self.valor=valor                  