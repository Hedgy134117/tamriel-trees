from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from . import models
from . import forms

@permission_required('is.admin')
def createTree(request):
    form = forms.CreateTree()
    
    if request.method == 'POST':
        form = forms.CreateTree(request.POST)

        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = forms.CreateTree()
    return render(request, 'trees/createTree.html', {'form': form})

def treeDetail(request, id):
    tree = models.Tree.objects.get(id=id)
    skills = models.Skill.objects.filter(tree=tree)
    return render(request, 'trees/tree.html', {'tree': tree, 'skills': skills})

@permission_required('is.admin')
def addSkill(request, id):
    tree = models.Tree.objects.get(id=id)
    form = forms.AddSkill(initial={'tree': tree})
    form.fields['parent'].queryset = models.Skill.objects.filter(tree=tree)

    if request.method == 'POST':
        form = forms.AddSkill(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.tree = models.Tree.objects.get(id=id)
            instance.save()
            return redirect('trees:treeDetail', id=id)
    else:
        form = forms.AddSkill(initial={'tree': tree})
        form.fields['parent'].queryset = models.Skill.objects.filter(tree=tree)
    return render(request, 'trees/addSkill.html', {'form': form, 'id': id})