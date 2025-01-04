from django import forms

class LocationWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [
            forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split(',')
        return ['', '', '']

    def format_output(self, rendered_widgets):
        return '<div class="form-row">{}</div>'.format(''.join(
            '<div class="col">{}</div>'.format(widget) for widget in rendered_widgets
        ))

class LocationField(forms.MultiValueField):
    widget = LocationWidget

    def __init__(self, *args, **kwargs):
        fields = [
            forms.CharField(),
            forms.CharField(),
            forms.CharField(),
        ]
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        return ','.join(data_list)