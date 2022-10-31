import xml.etree.ElementTree as ET

from .consumo import Consumo

from .cliente import Cliente
from .instancia import Instancia
from .categoria import Categoria
from .configuracion import Configuracion
from .recurso import Recurso
from .recursos_configuracion import Configuracion_Recurso
from myapp import categoria

lista_objetos_recursos=[]
lista_objetos_clientes=[]
lista_objetos_categoria=[]
listado_objetos_consumo=[]


class Leer:
    recursos_nuevos=0
    categorias_nuevas=0
    clientes_nuevos=0
    consumos_nuevos=0
    num_clientes=0
    num_categoria=0
    num_configuracion=0
    def leer_xml_objetos(self,path):
        self.recursos_nuevos=0
        self.categorias_nuevas=0
        self.clientes_nuevos=0        
        try:
            tree=ET.parse(path)
            root=tree.getroot()
            for lista in root:
                if lista.tag=='listaRecursos':
                    lista_recursos=lista
                elif lista.tag=='listaCategorias':
                    lista_categorias=lista
                elif lista.tag=='listaClientes':
                    lista_clientes=lista
            
            

            #obtenemos los recursos        
            for recurso in lista_recursos:
                self.recursos_nuevos+=1
                id_recurso=recurso.attrib['id']
                for subelem in recurso:
                    if subelem.tag=='nombre':
                        nombre=subelem.text
                    elif subelem.tag=='abreviatura':
                        abreviatura=subelem.text
                    elif subelem.tag=='metrica':
                        metrica=subelem.text
                    elif subelem.tag=='tipo':
                        tipo=subelem.text
                    elif subelem.tag=='valorXhora':
                        valor=subelem.text        

                recurso=Recurso(id_recurso,nombre,abreviatura,metrica,tipo,valor)
                lista_objetos_recursos.append(recurso) 
            

            #obtenemos las categorias
            if lista_objetos_categoria==[]:
                for categoria in lista_categorias:
                    self.num_configuracion=0
                    self.categorias_nuevas+=1
                    id_cat=categoria.attrib['id']
                    configs=[]
                    #dentro de categorias
                    for subelem in categoria:
                        if subelem.tag=="nombre":
                            nombre_categoria=subelem.text
                        elif subelem.tag=="descripcion":
                            descripcion=subelem.text
                        elif subelem.tag=="cargaTrabajo":
                            c_trabajo=subelem.text
                        elif subelem.tag=="listaConfiguraciones":
                            list_configs=subelem
                    #print(id_cat,nombre_categoria,descripcion,c_trabajo)

                    #dentro de configuracion
                    for config in list_configs:
                        id_config=config.attrib['id']
                        recurs=[]                   
                        for subelem in config:
                            if subelem.tag=="nombre":
                                nom_config=subelem.text
                            elif subelem.tag=="descripcion":
                                descri_config=subelem.text 
                            elif subelem.tag=="recursosConfiguracion":
                                list_recu=subelem       
                        #print(id_config,nom_config,descri_config,list_recu)
                        for recu in list_recu:
                            objeto_config_recurso=Configuracion_Recurso(recu.attrib['id'],recu.text)
                            recurs.append(objeto_config_recurso)
                        objeto_configuracion=Configuracion(id_config,nom_config,descri_config,recurs,self.num_configuracion)
                        configs.append(objeto_configuracion)
                        self.num_configuracion+=1
                    objeto_categoria=Categoria(id_cat,nombre_categoria,descripcion,c_trabajo,configs,self.num_categoria)
                    lista_objetos_categoria.append(objeto_categoria)
                    self.num_categoria+=1
            else:
                for categoria in lista_categorias:
                    self.num_configuracion=0
                    self.categorias_nuevas+=1
                    id_cat=categoria.attrib['id']
                    configs=[]
                    #dentro de categorias
                    for subelem in categoria:
                        if subelem.tag=="nombre":
                            nombre_categoria=subelem.text
                        elif subelem.tag=="descripcion":
                            descripcion=subelem.text
                        elif subelem.tag=="cargaTrabajo":
                            c_trabajo=subelem.text
                        elif subelem.tag=="listaConfiguraciones":
                            list_configs=subelem
                    #print(id_cat,nombre_categoria,descripcion,c_trabajo)

                    #dentro de configuracion
                    for config in list_configs:
                        id_config=config.attrib['id']
                        recurs=[]                   
                        for subelem in config:
                            if subelem.tag=="nombre":
                                nom_config=subelem.text
                            elif subelem.tag=="descripcion":
                                descri_config=subelem.text 
                            elif subelem.tag=="recursosConfiguracion":
                                list_recu=subelem       
                        #print(id_config,nom_config,descri_config,list_recu)
                        for recu in list_recu:
                            objeto_config_recurso=Configuracion_Recurso(recu.attrib['id'],recu.text)
                            recurs.append(objeto_config_recurso)
                        objeto_configuracion=Configuracion(id_config,nom_config,descri_config,recurs,self.num_configuracion)
                        configs.append(objeto_configuracion)
                        self.num_configuracion+=1
                    objeto_categoria=Categoria(id_cat,nombre_categoria,descripcion,c_trabajo,configs,len(lista_objetos_categoria))
                    lista_objetos_categoria.append(objeto_categoria)
                    self.num_categoria+=1   


            #obtenemos los clientes
            if lista_objetos_clientes==[]:
                for cliente in lista_clientes:
                    global clientes_nuevos
                    self.clientes_nuevos+=1
                    list_instancias=[]
                    nit=cliente.attrib['nit']
                    for subelem in cliente:
                        if subelem.tag=="nombre":
                            nom_cliente=subelem.text
                        elif subelem.tag=="usuario":
                            usuario=subelem.text
                        elif subelem.tag=="clave":
                            clave=subelem.text
                        elif subelem.tag=="direccion":
                            direccion=subelem.text
                        elif subelem.tag=="correoElectronico":
                            correo=subelem.text
                        elif subelem.tag=="listaInstancias":
                            instancias=subelem    
                    #print(nit,nom_cliente,usuario,clave,direccion,correo)                            

                    for instancia in instancias:
                        id_instancia=instancia.attrib['id']
                        for subelem in instancia:
                            if subelem.tag=="idConfiguracion":
                                id_confi=subelem.text
                            elif subelem.tag=="nombre":
                                nombre_instancia=subelem.text
                            elif subelem.tag=="fechaInicio":
                                fecha_inicio=subelem.text
                            elif subelem.tag=="estado":
                                estado=subelem.text
                            elif subelem.tag=="fechaFinal":
                                fecha_final=subelem.text
                        objeto_instancia=Instancia(id_instancia,id_confi,nombre_instancia,fecha_inicio,estado,fecha_final)        
                        list_instancias.append(objeto_instancia)        

                    objeto_cliente=Cliente(nit,nom_cliente,usuario,clave,direccion,correo,list_instancias,self.num_clientes)
                    lista_objetos_clientes.append(objeto_cliente)
                    self.num_clientes+=1
            else:
                for cliente in lista_clientes:
                    global clientes_nuevos
                    self.clientes_nuevos+=1
                    list_instancias=[]
                    nit=cliente.attrib['nit']
                    for subelem in cliente:
                        if subelem.tag=="nombre":
                            nom_cliente=subelem.text
                        elif subelem.tag=="usuario":
                            usuario=subelem.text
                        elif subelem.tag=="clave":
                            clave=subelem.text
                        elif subelem.tag=="direccion":
                            direccion=subelem.text
                        elif subelem.tag=="correoElectronico":
                            correo=subelem.text
                        elif subelem.tag=="listaInstancias":
                            instancias=subelem    
                    #print(nit,nom_cliente,usuario,clave,direccion,correo)                            

                    for instancia in instancias:
                        id_instancia=instancia.attrib['id']
                        for subelem in instancia:
                            if subelem.tag=="idConfiguracion":
                                id_confi=subelem.text
                            elif subelem.tag=="nombre":
                                nombre_instancia=subelem.text
                            elif subelem.tag=="fechaInicio":
                                fecha_inicio=subelem.text
                            elif subelem.tag=="estado":
                                estado=subelem.text
                            elif subelem.tag=="fechaFinal":
                                fecha_final=subelem.text
                        objeto_instancia=Instancia(id_instancia,id_confi,nombre_instancia,fecha_inicio,estado,fecha_final)        
                        list_instancias.append(objeto_instancia)        

                    objeto_cliente=Cliente(nit,nom_cliente,usuario,clave,direccion,correo,list_instancias,len(lista_objetos_clientes))
                    lista_objetos_clientes.append(objeto_cliente)
                              
                
                        


        except FileNotFoundError:
            print("ARCHIVO NO EXISTE VERIFIQUE RUTA") 

    def leer_consumo(self,path):
        self.consumos_nuevos=0
        try:
            tree=ET.parse(path)
            root=tree.getroot()
            for consumo in root:
                self.consumos_nuevos+=1
                nit=consumo.attrib['nitCliente']
                id_instancia=consumo.attrib['idInstancia']
                for subelem in consumo:
                    if subelem.tag=="tiempo":
                        tiempo=subelem.text 
                    elif subelem.tag=="fechaHora":
                        fechaHora=subelem.text
                objeto_consumo=Consumo(nit,id_instancia,tiempo,fechaHora)
                listado_objetos_consumo.append(objeto_consumo)                   
        except:
            print("ARCHIVO NO EXISTE VERIFIQUE RUTA") 

