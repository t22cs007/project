from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(label="point",max_length=50)

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs) 
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control'
    # class Meta:
    #     model = Post        
    #     fields = ('title','post',)
            