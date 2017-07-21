from datetime import date, timedelta
from django import template

'''

'''
register = template.Library()

@register.filter(name='vencimiento')
def getFechadeVencimiento(fecha = date.today()):
    vencimiento = fecha + timedelta(days = 365)
    return vencimiento.strftime('%Y-%m-%d')