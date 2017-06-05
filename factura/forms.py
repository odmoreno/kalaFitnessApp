from django import forms

from .models import Facturas
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from kala import settings


class CrearFacturaForm(forms.ModelForm):
    fecha_vencimiento = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Facturas
        fields = ('empresa', 'paciente','serie', 'fecha_vencimiento', 'subtotal', 'total')

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Crear', css_class='btn btn-primary'))
    helper.form_method = 'POST'

