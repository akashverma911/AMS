from django import forms

class AvailabilityForm(forms.Form):
  TYPES = (
      ('Sm', 'Small'),
      ('Md', 'Medium'),
      ('La', 'Large'),
  )
  vehicle_category = forms.ChoiceField(choices=TYPES,required=True)
  book_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M",]) 
