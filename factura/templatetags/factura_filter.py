# -*- coding: utf-8 -*-
from datetime import date, timedelta
from django import template

'''
Funcion: getFechadeVencimiento
Entradas: - fecha actual
Salidas:  - fecha de vencimiento

Funcion que retorna la fecha de vencimiento, un año después
'''
register = template.Library()

@register.filter(name='vencimiento')
def getFechadeVencimiento(fecha = date.today()):
    vencimiento = fecha + timedelta(days = 365)
    return vencimiento.strftime('%Y-%m-%d')