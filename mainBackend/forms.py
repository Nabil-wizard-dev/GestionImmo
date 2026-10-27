from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    # PropertyImages = MultipleFileField(label='Select files', required=False)
    class Meta:
        model = Property
        fields = [ 'PropertyType', 'PropertyImages', 'PropertyPrice','PropertyOwningFiles', 'PropertyName', 'PropertyLocation']
        widgets = {
            'PropertyType': forms.Select(attrs={'class': 'form-control block w-full px-3 py-2 text-base text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-gray-500 focus:border-indigo-500 sm:text-base'}), # type: ignore

            'PropertyImages': forms.FileInput(attrs={'class':'form-control block w-full px-3 py-2 text-base text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-gray-500 focus:border-indigo-500 sm:text-base'}), # type: ignore

            'PropertyOwningFiles': forms.ClearableFileInput(attrs={'class': 'form-control block w-full px-3 py-2 text-base text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-gray-500 focus:border-indigo-500 sm:text-base'}), # type: ignore

            'PropertyPrice': forms.TextInput(attrs={'class': 'form-control block w-full px-3 py-2 text-base text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-gray-500 focus:border-indigo-500 sm:text-base'}),  # type: ignore

            'PropertyName': forms.TextInput(attrs={'class': 'form-control block w-full px-3 py-2 text-base text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-gray-500 focus:border-indigo-500 sm:text-base'}), # type: ignore 

            'PropertyLocation': forms.TextInput(attrs={'type': 'input','class': 'form-control block w-full px-3 py-2 text-base text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-gray-500 focus:border-indigo-500 sm:text-base'})  # type: ignore
        }

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['OwnerId'].widget.attrs.update({'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})
        #     self.fields['PropertyType'].widget.attrs.update({'class': 'shadow ring-2 appearance-none border rounded w-full py-2 px-3  text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})
        #     self.fields['PropertyImages'].widget.attrs.update({'class': 'shadow-lg appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})
        #     self.fields['PropertyPrice'].widget.attrs.update({'class': 'shadow bg-red-500 text-red-500 appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})
        #     self.fields['PropertyName'].widget.attrs.update({'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})
        #     self.fields['PropertyLocation'].widget.attrs.update({'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})


