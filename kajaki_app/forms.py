from django import forms
from django.core.exceptions import ValidationError
from kajaki_app.models import Route, Kayak, Contact


class AddRouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddRouteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class AddKayakForm(forms.ModelForm):
    class Meta:
        model = Kayak
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddKayakForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
