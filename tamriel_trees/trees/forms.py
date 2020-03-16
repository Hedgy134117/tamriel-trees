from django import forms
from . import models

class CreateTree(forms.ModelForm):
    class Meta:
        model = models.Tree
        fields = '__all__'

class mAddSkill(forms.ModelForm):
    class Meta:
        model = models.mSkill
        fields = '__all__'

# class AddSkill(forms.ModelForm):
#     class Meta:
#         model = models.Skill
#         fields = '__all__'

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(AddSkill, self).get_form(request, obj, **kwargs)
    #     form.base_fields['parent'].queryset = models.Skill.objects.filter(tree=obj.tree)