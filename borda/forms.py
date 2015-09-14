from django import forms


class PostForm(forms.Form):
    post = forms.CharField(label='', max_length=10000, widget=forms.Textarea(attrs={'id': 'post_input_field'}))
    picture = forms.ImageField(label='', required=False)