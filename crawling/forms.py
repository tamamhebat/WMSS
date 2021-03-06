'''
Created on May 16, 2017

@author: Asus-PC
'''
from django import forms

situs_berita = [('det','Detik.com'),('kom','Kompas.com'),('lip','Liputan6.com')]
class PostForm(forms.Form):
    keyword = forms.CharField(max_length=256)
    jumlah = forms.IntegerField()
    situs = forms.ChoiceField(choices=situs_berita, widget=forms.Select(attrs={'class': 'selectpicker'}))

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=100)
    file = forms.FileField()
    
class FormInputBerita(forms.Form):
    judul_berita = forms.CharField()
    konten_berita = forms.CharField(widget=forms.Textarea)
 