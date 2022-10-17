import xml.etree.ElementTree as ET
from categoria import Categoria
from configuracion import Configuracion

from recursos_configuracion import Configuracion_Recurso

lista_objetos_recursos=[]
lista_objetos_clientes=[]
lista_objetos_categoria=[]
from recurso import Recurso
class Leer:
    def leer_xml_objetos(self,path):
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
            for categoria in lista_categorias:
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
                    objeto_configuracion=Configuracion(id_config,nom_config,descri_config,recurs)
                    configs.append(objeto_configuracion)
                objeto_categoria=Categoria(id_cat,nombre_categoria,descripcion,c_trabajo,configs)
                lista_objetos_categoria.append(objeto_categoria)
            a=lista_objetos_categoria[0].lista_configuraciones
            b=a[1].lista_recursos
            print(b[1].cantidad)       
                    



        except FileNotFoundError:
            return "ARCHIVO NO EXISTE VERIFIQUE RUTA"

interprete=Leer()
interprete.leer_xml_objetos("config_objetos.xml")