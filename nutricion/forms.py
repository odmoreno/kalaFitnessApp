from datetimewidget.widgets import DateWidget, TimeWidget
from django import forms
from django.forms import NumberInput, ModelForm, Select, TextInput, Textarea, RadioSelect
from nutricion.models import ficha_nutricion, HorarioNut


class HorizontalRadioSelect(forms.RadioSelect):
    template_name = 'nutricion/horizontal_select.html'

class HorariosForm(ModelForm):
    class Meta:
        model = HorarioNut
        fields = [ 'fecha', 'hora', 'detalle', 'estado' ]
        labels = {'fecha':'Fecha', 'hora': 'Hora', 'detalle': 'Detalle', 'estado': 'Estado'}
        widgets = {
            'fecha': DateWidget(attrs={'id':"yourdatetimeid", 'class': u'form-control'}, usel10n = True, bootstrap_version=3),
            'hora': TimeWidget(attrs={'id':"yourdatetimeid", 'class': u'form-control'}, usel10n = True, bootstrap_version=3),
            'detalle': Textarea(
                attrs={'class': u'form-control', 'placeholder': u'Ingrese respuesta ...', 'rows': 10, 'cols': 40,
                       'style': 'height: 6em;'}),
            'estado': Select(attrs={'class': u'form-control'}),
                   }

class FichaForm(ModelForm):
    class Meta:
         model = ficha_nutricion

         fields = ['lacteos', 'vegetales', 'frutas', 'cho', 'carnes', 'comidas_rapidas', 'frituras',
                   'enlatados', 'gaseosas', 'energizantes', 'infusiones', 'lacteos_input', 'vegetales_input', 'frutas_input', 'cho_input', 'carnes_input', 'comidas_rapidas_input',
                   'frituras_input', 'enlatados_input', 'gaseosas_input', 'energizantes_input', 'infusiones_input',
                   'pregunta1', 'pregunta2', 'pregunta3', 'pregunta4', 'pregunta5', 'pregunta6',
                   'proteina', 'grasas', 'carbohidratos', 'dieta'
                   ]
         labels = {
              'lacteos': 'Lacteos', 'vegetales': 'Vegetales', 'frutas': 'Frutas', 'cho': 'CHO', 'carnes': 'Carnes',
             'comidas_rapidas':'Comidas Rapidas', 'frituras': 'Frituras', 'enlatados': 'Alimentos Enlatados', 'gaseosas': 'Bebidas Gaseosas',
             'energizantes': 'Bebidas Energizantes', 'infusiones': 'Infusiones', 'lacteos_input': 'Veces', 'vegetales_input': 'Veces', 'frutas_input': 'Veces', 'cho_input': 'Veces', 'carnes_input': 'Veces',
             'comidas_rapidas_input': 'Veces', 'frituras_input': 'Veces', 'enlatados_input': 'Veces', 'gaseosas_input': 'Veces', 'energizantes_input': 'Veces', 'infusiones_input': 'Veces',
             'pregunta1': 'Sufre algun tipo de enfermedad digestiva?', 'pregunta2':'Cuando esta solo le da por comer mas?', 'pregunta3': 'Cuantas horas de sueno realiza?',
             'pregunta4': 'Cuantas comidas realiza en el dia?', 'pregunta5': 'Como son las preparaciones de las comidas?', 'pregunta6': 'Que cantidad de agua consume?',
             'proteina': 'Proteinas', 'grasas': 'Grasas', 'carbohidratos': 'Carbohidratos'
         }
         widgets = {
             'lacteos':  Select(attrs={'class': u'form-control'}),
             'vegetales': Select(attrs={'class': u'form-control'}),
             'frutas': Select(attrs={'class': u'form-control'}),
             'cho': Select(attrs={'class': u'form-control'}),
             'carnes': Select(attrs={'class': u'form-control'}),
             'comidas_rapidas': Select(attrs={'class': u'form-control'}),
             'frituras': Select(attrs={'class': u'form-control'}),
             'enlatados': Select(attrs={'class': u'form-control'}),
             'gaseosas': Select(attrs={'class': u'form-control'}),
             'energizantes': Select(attrs={'class': u'form-control'}),
             'infusiones': Select(attrs={'class': u'form-control'}),
             'lacteos_input': HorizontalRadioSelect(),
             'vegetales_input': HorizontalRadioSelect(),
             'frutas_input': HorizontalRadioSelect(),
             'cho_input': HorizontalRadioSelect(),
             'carnes_input': HorizontalRadioSelect(),
             'comidas_rapidas_input': HorizontalRadioSelect(),
             'frituras_input': HorizontalRadioSelect(),
             'enlatados_input': HorizontalRadioSelect(),
             'gaseosas_input': HorizontalRadioSelect(),
             'energizantes_input': HorizontalRadioSelect(),
             'infusiones_input': HorizontalRadioSelect(),
             'pregunta1': Textarea(attrs={'class': u'form-control', 'placeholder': u'Ingrese respuesta ...','rows': 10,'cols': 40,'style': 'height: 6em;'}),
             'pregunta2': Textarea(attrs={'class': u'form-control', 'placeholder': u'Ingrese respuesta ...','rows': 10,'cols': 40,'style': 'height: 6em;'}),
             'pregunta3': Textarea(attrs={'class': u'form-control', 'placeholder': u'Ingrese respuesta ...','rows': 10,'cols': 40,'style': 'height: 6em;'}),
             'pregunta4': Textarea(attrs={'class': u'form-control', 'placeholder': u'Ingrese respuesta ...','rows': 10,'cols': 40,'style': 'height: 6em;'}),
             'pregunta5': Textarea(attrs={'class': u'form-control', 'placeholder': u'Ingrese respuesta ...','rows': 10,'cols': 40,'style': 'height: 6em;'}),
             'pregunta6': Textarea(attrs={'class': u'form-control', 'placeholder': u'Ingrese respuesta ...','rows': 10,'cols': 40,'style': 'height: 6em;'}),
             'proteina': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'%', 'min': '1', 'max': '100',
                        'step': '1'}),
             'grasas': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'%', 'min': '1', 'max': '100',
                        'step': '1'}),
             'carbohidratos': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'%', 'min': '1', 'max': '100',
                        'step': '1'}),
             'dieta': Textarea(attrs={'class': u'form-control', 'placeholder': u'Tipo de dieta ...','rows': 10,'cols': 40,'style': 'height: 6em;'})

         }
         error_messages = {
             'lacteos_input': {
                 'max_length': ("This writer's name is too long."),
             },
         }