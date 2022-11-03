import re
import random
from datetime import datetime


def encontrar_fecha(string):
    x = re.search(r"(\d{2}|\d{1})(/|.|-)(\d{2}|\d{1})(/|.|-)(\d{4})", string)
    if x is not None:
        return x.group()
    else:
        return None    

def encontrar_fecha_hora(string):
    x = re.search(r"(\d{2}|\d{1})(/|.|-)(\d{2}|\d{1})(/|.|-)(\d{4}) (\d{2})(:)(\d{2})", string)
    if x is not None:
        return x.group()
    else:
        return None  

def generar_numero():
    numero = random.randint(1000, 10000)
    return numero

def verificar_fecha(fecha_inicio,fecha_fin,fecha):
    fecha_inicio=fecha_inicio.split('/')
    fecha_inicio=datetime(int(fecha_inicio[2]),int(fecha_inicio[1]),int(fecha_inicio[0]))#date time esta en año/mes/dia
    fecha_fin=fecha_fin.split('/')
    fecha_fin=datetime(int(fecha_fin[2]),int(fecha_fin[1]),int(fecha_fin[0]))
    fecha=fecha.split('/')
    fecha=datetime(int(fecha[2]),int(fecha[1]),int(fecha[0]))
    if fecha>=fecha_inicio and fecha<=fecha_fin:
        return True
    else:
        return False    

