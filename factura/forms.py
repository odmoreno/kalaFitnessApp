from django import forms

from .models import Facturas
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CrearFacturaForm(forms.ModelForm):

    class Meta:
        model = Facturas
        fields = ('serie', 'fecha_vencimiento', 'subtotal', 'total') # 'paciente'

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'

