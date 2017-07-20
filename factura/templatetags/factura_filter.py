from datetime import date, timedelta
from django import template

'''

'''
register = template.Library()

@register.filter(name='vencimiento')
def validarFechadeVencimiento(fecha):
    vencimiento = fecha + timedelta(days = 365)
    return vencimiento.strftime('%d/%m/%Y')
