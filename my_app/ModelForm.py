from django import forms
from ..my_app.models import Funcionario


class InsereFuncionarioForm(forms.ModelForm):

    chefe = forms.BooleanField(
        label='Chefe?',
        required=True,
    )

    biografia = forms.CharField(
        label='Biografia',
        required=False,
        widget=forms.TextArea
    )


class Meta:
    # Modelo base
    model = Funcionario

    # Campos que estarão no form
    fields = [
        'nome',
        'sobrenome',
        'cpf',
        'remuneracao'
    ]

    # Campos que não estarão no form
    exclude = [
        'tempo_de_servico'
    ]
