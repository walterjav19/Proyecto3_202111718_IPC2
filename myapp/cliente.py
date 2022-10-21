class Cliente:
    def __init__(self,nit,nom_cliente,usuario,clave,direccion,correo,lista_instancias,num):
        self.nit=nit
        self.nom_cliente=nom_cliente
        self.usuario=usuario
        self.clave=clave
        self.direccion=direccion
        self.correo=correo
        self.lista_instancias=lista_instancias
        self.num=num


    def set_lista_instancias(self,lista):
        self.lista_instancias=lista