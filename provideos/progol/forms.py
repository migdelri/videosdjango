from django import forms
from .models import tbl_usuarios ,tbl_videos

class UserForm(forms.ModelForm):
    class Meta:
        model = tbl_usuarios
        fields = '__all__'


class FormVideos(forms.ModelForm):
    #forms.fields('idUsuario').readonly
    #idUsuario = forms.CharField(widget=forms.TextInput(attrs={"class": "special"}))
    class Meta:
        model = tbl_videos
        model.idUsuario.field.editable = False
        fields = '__all__'
    
   
class VideoForm(forms.ModelForm):
    class Meta:
        model = tbl_videos
        model.idUsuario.field.editable = True
        fields = '__all__'      
