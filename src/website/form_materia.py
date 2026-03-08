from django import forms
from .materia import Materia
import re

CORES_PREDEFINIDAS = [
    ("#C8762B", "Âmbar"),
    ("#A7C7E7", "Azul bebê"),
    ("#B5EAD7", "Verde menta"),
    ("#C7CEEA", "Lavanda"),
    ("#FFD6A5", "Pêssego"),
    ("#FFCAD4", "Rosa pastel"),
    ("#F1E3D3", "Areia"),
    ("#BEE3DB", "Verde água"),
    ("#EAC4D5", "Rosa antigo"),
    ("#D7E3FC", "Azul gelo"),
    ("#FFF1BA", "Amarelo pastel"),
    ("#E2F0CB", "Verde pastel"),
]


class MateriaForm(forms.ModelForm):
    cor = forms.ChoiceField(
        choices=[*CORES_PREDEFINIDAS, ("__custom__", "Personalizada")],
        widget=forms.RadioSelect(attrs={'class': 'color-radio'}),
        initial="#C8762B",
        label='Cor'
    )
    cor_custom_hex = forms.CharField(
        required=False,
        label="Hex personalizado",
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "#AABBCC",
                "inputmode": "text",
                "autocomplete": "off",
            }
        ),
    )

    class Meta:
        model = Materia
        fields = ["nome", "cor"]
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Ex: Matemática, Biologia...',
                'class': 'form-input',
                'autofocus': True,
            }),
        }
        labels = {
            'nome': 'Nome da Matéria',
        }

    def clean(self):
        cleaned = super().clean()
        cor = cleaned.get("cor")
        custom = (cleaned.get("cor_custom_hex") or "").strip()

        if cor == "__custom__":
            if not custom:
                self.add_error("cor_custom_hex", "Informe um hex para a cor personalizada.")
                return cleaned

            if not re.fullmatch(r"#([0-9a-fA-F]{6})", custom):
                self.add_error("cor_custom_hex", "Hex inválido. Use o formato #RRGGBB.")
                return cleaned

            cleaned["cor"] = custom.upper()
        return cleaned
