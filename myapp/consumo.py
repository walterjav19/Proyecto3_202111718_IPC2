class Consumo:
    def __init__(self,nit,id_instancia,tiempo,fecha,hora):
        self.nit=nit
        self.id_instancia=id_instancia
        self.tiempo=float(tiempo)
        self.fecha=fecha
        self.hora=hora

    def set_n_factura(self,correlativo):
        self.correlativo=correlativo    

    def set_n(self,n):
        self.n=n

    def set_Consumo(self,consumo):
        self.consumo=consumo          