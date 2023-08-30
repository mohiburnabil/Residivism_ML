from django.forms import ModelForm
from . import models


class Recidivism_form(ModelForm):
    class Meta:
        model = models.Recidivism
        fields = '__all__'
        # fields=['age','education']

    def __init__(self, *args, **kwargs):
        super(Recidivism_form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
