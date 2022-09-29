from django.views.generic import CreateView
from django.urls import reverse_lazy
from ..my_app.models import Funcionario
from ..my_app.models import InsereFuncionarioForm


class FuncionarioCreateView(CreateView):
    template_name = "my_app/form.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionarios")
