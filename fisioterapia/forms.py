from django import forms
from django.forms import NumberInput, ModelForm, Select, TextInput
from django.forms.extras.widgets import  SelectDateWidget

from paciente.models import Paciente
from kalaapp.models import Usuario, Rol
from django.contrib.auth.models import User
from fisioterapia.models import Ficha



class ComentarioForm(forms.Form):
     Destino= forms.ModelMultipleChoiceField(queryset=Paciente.objects.all())
     comentario = forms.CharField(widget=forms.Textarea)

class DateTypeInput(forms.DateInput):
    input_type = 'date'

class FichaForm(ModelForm):
    class Meta:
         model = Ficha

         fields = [#'fecha',
                   'altura', 'peso', 'imc', 'musculo', 'grasa_visceral', 'grasa_porcentaje',
                   'cuello', 'hombros', 'pecho', 'brazo_derecho', 'brazo_izquierdo', 'antebrazo_derecho',
                   'antebrazo_izquierdo', 'cintura', 'cadera', 'muslo_derecho', 'muslo_izquierdo',
                   'pantorrilla_derecha', 'pantorrilla_izquierda', 'flexiones', 'sentadillas', 'saltoLargo',
                   'suspension', 'abdomen_bajo', 'abdomen_alto', 'espinales', 'lumbares', 'trenSuperior', 'trenInferior'
                   ]
         labels = {
              'altura': 'Altura', 'peso': 'Peso', 'imc': 'Imc', 'musculo': 'Musculo',
              'grasa_visceral': 'Grasa Viseral', 'grasa_porcentaje': 'Grasa Porcentual', 'cuello': 'Cuello',
              'hombros': 'Hombros', 'pecho': 'Pecho', 'brazo_derecho':  'Brazo Derecho', 'brazo_izquierdo': 'Brazo Izquierdo', 'antebrazo_derecho': 'Antebrazo Derecho',
                  'antebrazo_izquierdo': 'Antebrazo Izquierdo', 'cintura': 'Cintura', 'cadera': 'Cadera', 'muslo_derecho': 'Muslo Derecho', 'muslo_izquierdo': 'Muslo Izquierdo',
                  'pantorrilla_derecha': 'Pantorilla Derecha', 'pantorrilla_izquierda': 'Pantorilla Izquierda', 'flexiones': 'Flexiones', 'sentadillas': 'Sentadillas', 'saltoLargo': 'Salto Largo',
                  'suspension': 'Suspension', 'abdomen_bajo': 'Abdomen Bajo', 'abdomen_alto': 'Abdomen Alto', 'espinales': 'Espinales', 'lumbares': 'Lumbares',
                  'trenSuperior': 'Tren Superior', 'trenInferior': 'Tren Inferior',
         }
         widgets = {
             #'fecha': DateTypeInput(attrs={'class': u'form-control'}),
             'altura': NumberInput(attrs={'class': u'form-control', 'placeholder': u'Altura en centimetros', 'min': '1.0', 'step': '0.1'}),
             'peso': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Peso en Kilogramos', 'min': '1.0',
                        'step': '0.1'}),
             'imc': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Indice de masa corporal', 'min': '1.0',
                        'step': '0.1'}),
             'musculo': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Porcentaje muscular', 'min': '1.0',
                        'step': '0.1'}),
             'grasa_visceral': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Grasa visceral', 'min': '1.0',
                        'step': '0.1'}),
             'grasa_porcentaje': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Altura en centimetros', 'min': '1.0',
                        'step': '0.1'}),
             'cuello': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Cuello', 'min': '1.0',
                        'step': '0.1'}),
             'hombros': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Hombros', 'min': '1.0',
                        'step': '0.1'}),
             'pecho': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'pecho', 'min': '1.0',
                        'step': '0.1'}),
             'brazo_derecho': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Brazo Derecho', 'min': '1.0',
                        'step': '0.1'}),
             'brazo_izquierdo': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Brazo izquierdo', 'min': '1.0',
                        'step': '0.1'}),
             'antebrazo_derecho': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Antebrazo derecho', 'min': '1.0',
                        'step': '0.1'}),
             'antebrazo_izquierdo': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Antebrazo izquierdo', 'min': '1.0',
                        'step': '0.1'}),
             'cintura': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Cintura', 'min': '1.0',
                        'step': '0.1'}),
             'cadera': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Cadera', 'min': '1.0',
                        'step': '0.1'}),
             'muslo_derecho': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Muslo Derecho', 'min': '1.0',
                        'step': '0.1'}),
             'muslo_izquierdo': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Muslo Izquierdo', 'min': '1.0',
                        'step': '0.1'}),
             'pantorrilla_derecha': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Pantorrilla derecha', 'min': '1.0',
                        'step': '0.1'}),
             'pantorrilla_izquierda': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Pantorrilla izquierda', 'min': '1.0',
                        'step': '0.1'}),
             'flexiones': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'flexiones', 'min': '1',
                        'step': '1'}),
             'sentadillas': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Sentadillas', 'min': '1',
                        'step': '1'}),
             'saltoLargo': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Salto Largo', 'min': '1',
                        'step': '1'}),
             'abdomen_alto': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Abdomen Alto', 'min': '1',
                        'step': '1'}),
             'abdomen_bajo': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Abdomen Bajo', 'min': '1',
                        'step': '1'}),
             'espinales': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Espinales', 'min': '1',
                        'step': '1'}),
             'lumbares': NumberInput(
                 attrs={'class': u'form-control', 'placeholder': u'Lumbares', 'min': '1',
                        'step': '1'}),
             'suspension':  Select(attrs={'class': u'form-control'}),
             'trenInferior': TextInput(attrs={'class': u'form-control','placeholder': u'Ingresar Hora'}),
             'trenSuperior': TextInput(attrs={'class': u'form-control', 'placeholder': u'Ingresar Hora'}),
         }