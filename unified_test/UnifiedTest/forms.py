from django import forms

from UnifiedTest.models import Page, PageAuthentication


class PageForm(forms.ModelForm):
    ref = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    url = forms.URLField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    class Meta:
        model = Page
        fields = ('ref', 'url', 'status_code', 'delay', 'response',
                  'dynamic_code', 'default_response')


class PageAuthenticationForm(forms.ModelForm):
    username = forms.CharField(required=False)
    password = forms.CharField(required=False)
    token = forms.CharField(required=False)
    header_name = forms.CharField(required=False)
    header_value = forms.CharField(required=False)
    value = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    class Meta:
        model = PageAuthentication
        fields = ('type',)
