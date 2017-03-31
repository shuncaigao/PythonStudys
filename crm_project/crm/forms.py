from django.forms import Form, ModelForm
from crm import models


class CustomerModelForm(ModelForm):
    class Meta:
        model = models.Customer
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(CustomerModelForm, self).__init__(*args, **kwargs)

        for field_name in self.base_fields:
            field = self.base_fields[field_name]
            field.widget.attrs.update({'class': 'form-control'})
