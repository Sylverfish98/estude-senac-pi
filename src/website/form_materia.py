from django import forms
from .materia import Materia

CORES_PREDEFINIDAS = [
    ('#C8762B', 'Âmbar'),
    ("#1E5CCF", 'Azul'),
    ("#AD68EE", 'Lilás'),
    ("#43B268", 'Verde'),
    ("#E22020", 'Vermelho'),
]


class MateriaForm(forms.ModelForm):
    cor = forms.ChoiceField(
        choices=CORES_PREDEFINIDAS,
        widget=forms.RadioSelect(attrs={'class': 'color-radio'}),
        initial='#C8762B',
        label='Cor'
    )

    class Meta:
        model = Materia
        fields = ['nome', 'imagem', 'cor']
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Ex: Matemática, Biologia...',
                'class': 'form-input',
                'autofocus': True,
            }),
            'imagem': forms.ClearableFileInput(attrs={
                'class': 'form-file',
                'accept': 'image/*',
            }),
        }
        labels = {
            'nome': 'Nome da Matéria',
            'imagem': 'Imagem (opcional)',
        }
