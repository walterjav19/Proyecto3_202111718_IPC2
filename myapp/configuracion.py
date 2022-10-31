class Configuracion:
    def __init__(self,id,nombre,descripcion,lista_recursos,num):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.lista_recursos=lista_recursos
        self.num=num
    

    def set_lista_recursos(self,lista):
        self.lista_recursos=lista