from django import forms

from .models import Facturas
from kalaapp.models import Empresa
from paciente.models import Paciente
from datetime import datetime, date
from django.db.models.functions import Concat
from django.db.models import Value
from kala import settings


class CrearFacturaForm(forms.ModelForm):

    class Meta:
        model = Facturas
        fields = ('empresa', 'paciente','serie', 'fecha_vencimiento', 'subtotal', 'total')

    def __init__(self, *args, **kwargs):
        super(CrearFacturaForm, self).__init__(*args, **kwargs)

        empresas = Empresa.objects.filter(estado='A')\
            .values_list('pk', 'nombre')\
            .order_by('nombre')
        pacientes = Paciente.objects.filter(estado='A')\
            .values_list('pk', 'usuario__nombre', 'usuario__apellido')\
            .annotate(nombre_completo=Concat('usuario__apellido',Value(' '),'usuario__nombre'))\
            .values_list('pk', 'nombre_completo')\
            .order_by('nombre_completo')

        self.fields['empresa'] = forms.ChoiceField(choices=empresas)
        self.fields['paciente'] = forms.ChoiceField(choices=pacientes)
        self.fields['fecha_vencimiento'] = forms.DateField(widget=forms.DateInput(), input_formats=settings.DATE_INPUT_FORMATS)


        # Validamos que el autor no sea menor a 3 caracteres
    def clean_serie(self):
        data = self.cleaned_data

        serie = data.get('serie')

        if len(serie) < 3:
            self.add_error('serie', "La serie de la factura debe contener mas de tres caracteres")

        return serie

    def clean_subtotal(self):
        data = self.cleaned_data

        subtotal = data.get('subtotal')

        if subtotal <= 0:
            self.add_error('subtotal', "El subtotal debe ser un valor positivo")

        return subtotal

    # Validamos que el texto no sea mayor a 400 caracteres
    def clean_total(self):
        data = self.cleaned_data

        total = data.get('total')

        if total <= 0:
            self.add_error('total', "El subtotal debe ser un valor positivo")

        return total

    def clean_fecha_vencimiento(self):
        data = self.cleaned_data

        fecha_vencimiento = data.get('fecha_vencimiento')
        fecha_actual = datetime.now().date()

        if fecha_actual > fecha_vencimiento:
            self.add_error('fecha_vencimiento', "La fecha de vencimiento debe ser mayor o igual al dia de hoy")

        elif fecha_vencimiento > date(2099, 12, 31):
            self.add_error('fecha_vencimiento', "La fecha de vencimiento debe ser menor o igual a 31/12/2099")

        return fecha_vencimiento

