from django import forms

class contactform(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'p-2 form-control rounded-pill','placeholder': ' Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'p-2 form-control rounded-pill','placeholder': ' Email'}))
    message = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': 'p-2 form-control rounded-4', 'rows': 3, 'cols': 101,'placeholder': 'Message'}))
    
    
class commentform(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'p-2 form-control rounded-pill','placeholder': ' Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'p-2 form-control rounded-pill','placeholder': ' Email'}))
    website = forms.URLField(required=False,widget=forms.URLInput(attrs={'class':'p-2 form-control rounded-pill','placeholder':'Website'})) 
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'p-2 form-control rounded-4', 'rows': 3, 'cols': 101,'placeholder': 'Message'}))    
 
 
    
class ClassEnquiry(forms.Form):
    class_choice = (
        ('', 'Class'),
        ('Hospitality, Leisure & Sports Courses', 'Hospitality, Leisure & Sports Courses'),
        ('Environmental Studies & Earth Sciences', 'Environmental Studies & Earth Sciences'),
        ('Natural Sciences & Mathematics Courses', 'Natural Sciences & Mathematics Courses'),
        ('Basic English Speaking and Gramer', 'Basic English Speaking and Gramer'),
    )
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'p-2 form-control rounded-pill border-0 orange3', 'placeholder': ' Name'})) 
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'p-2 form-control rounded-pill border-0 orange3', 'placeholder': ' Email'})) 
    Classes = forms.ChoiceField(choices=class_choice, required=False, widget=forms.Select(attrs={'class': 'p-2 form-control rounded-pill border-0 orange3'})) 
    message = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': 'p-2 form-control rounded-4 border-0 orange3', 'placeholder': ' Message','rows': 2}))
