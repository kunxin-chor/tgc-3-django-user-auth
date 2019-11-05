from django import forms
from .models import Item
from pyuploadcare.dj.forms import ImageField
class ItemForm(forms.ModelForm):
    photo = ImageField(label='Image')
    class Meta:
      model = Item
      fields = ('name', 'done', 'category', 'tags', 'photo')