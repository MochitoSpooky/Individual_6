from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    usuario = forms.CharField(max_length=100)
    contraseña = forms.CharField(widget=forms.PasswordInput())
    tipo_usuario = forms.ChoiceField(choices=[('moderador', 'Moderador'), ('fotofans', 'FotoFans')])
