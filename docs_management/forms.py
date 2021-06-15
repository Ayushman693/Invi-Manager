from django import forms



from docs_management.models import ExtractedDoc


class ExtractedDocUpdateForm(forms.ModelForm):
    class Meta:
        model = ExtractedDoc
        fields = ["invoice_number", "summary"]

    def update_instance(self, instance, commit=True):
        for f in instance._meta.fields:
            if f.attname in self.fields:
                setattr(instance, f.attname, self.cleaned_data[f.attname])
        if commit:
            try:
                instance.save()
            except BaseException:
                return False
        return instance
