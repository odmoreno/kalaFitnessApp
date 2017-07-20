from datetime import date, timedelta
from django import template

'''

'''
register = template.Library()
@register.simple_tag(name=vencimiento)
def validarFechadeVencimiento(fecha):
    return fecha + timedelta(days = 365)
