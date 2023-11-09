from django.forms import ModelForm
from models import Asset

class AssetForm(ModelForm):
    class meta:
        model = Asset
        fields = ['category', 'name', 'info', 'details', 'image']

