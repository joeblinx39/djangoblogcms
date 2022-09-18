from django import forms
from .models import Post, Category, Comment
from tinymce.widgets import TinyMCE

# choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment')]

choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for item in choices:
    choice_list.append(item)

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 30, 'rows': 20, 'class': 'form-control'}))
    

    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'header_image', 'body', 'snippet')
        
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'value':'', 'id': 'user', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            # 'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 30, 'rows': 20, 'class': 'form-control'}))
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'snippet')
        
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

        }


        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body',)
        
        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }


        