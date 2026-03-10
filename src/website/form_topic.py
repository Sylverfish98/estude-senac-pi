from django import forms

from .topic import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["nome", "link", "data_estudo"]
        widgets = {
            "materia": forms.Select(
                attrs={
                    "class": "form-input",
                    "placeholder": "Selecione uma máteria",
                    "autofocus": False,
                }
            ),
            "nome": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Ex: Regra de três, Funções...",
                    "autofocus": True,
                }
            ),
            "link": forms.URLInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Link (opcional)",
                }
            ),
            "data_estudo": forms.DateInput(
                attrs={
                    "class": "form-input",
                    "type": "date",
                }
            ),
            "index": forms.NumberInput(
                attrs={
                    "class": "form-input",
                    "min": 0,
                }
            ),
        }
        labels = {
            "materia": "Matéria",
            "nome": "Nome do tópico",
            "link": "Link (opcional)",
            "data_estudo": "Data para estudar (opcional)",
            "index": "Ordem (index)",
        }

class TopicFormRequiresSubject(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["materia", "nome", "link", "data_estudo"]
        widgets = {
            "materia": forms.Select(
                attrs={
                    "class": "form-input",
                    "placeholder": "Selecione uma máteria",
                    "autofocus": False,
                }
            ),
            "nome": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Ex: Regra de três, Funções...",
                    "autofocus": True,
                }
            ),
            "link": forms.URLInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Link (opcional)",
                }
            ),
            "data_estudo": forms.HiddenInput(
                attrs={
                    "class": "form-input",
                    "type": "string",

                }
            ),
            "index": forms.NumberInput(
                attrs={
                    "class": "form-input",
                    "min": 0,
                }
            ),
        }
        labels = {
            "materia": "Matéria",
            "nome": "Nome do tópico",
            "link": "Link (opcional)",
            "data_estudo": "Data para estudar (opcional)",
            "index": "Ordem (index)",
        }
