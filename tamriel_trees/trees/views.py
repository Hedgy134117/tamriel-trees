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

def mTreeDetail(request, id):
    return render(request, "trees/mTree.html", {'skills': models.mSkill.objects.filter(tree_field=models.Tree.objects.get(id=id)), 'id': id})

@permission_required('is.admin')
def mAddSkill(request, id):
    tree = models.Tree.objects.get(id=id)
    form = forms.mAddSkill(initial={'tree_field': tree})
    form.fields['parent'].queryset = models.mSkill.objects.filter(tree_field=tree)

    if request.method == 'POST':
        form = forms.mAddSkill(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.tree = models.Tree.objects.get(id=id)
            instance.save()
            return redirect('trees:mTreeDetail', id=id)
    else:
        form = forms.mAddSkill(initial={'tree_field': tree})
        form.fields['parent'].queryset = models.mSkill.objects.filter(tree_field=tree)
    return render(request, 'trees/mAddSkill.html', {'form': form, 'id': id})

@permission_required('is.admin')
def mEditSkill(request, tree_id, skill_id):
    tree = models.Tree.objects.get(id=tree_id)
    skill = models.mSkill.objects.get(id=skill_id)
    form = forms.mAddSkill(instance=skill)

    if request.method == 'POST':
        form = forms.mAddSkill(request.POST)

        if form.is_valid():
            skill.name = form.cleaned_data['name']
            skill.description = form.cleaned_data['description']
            skill.tree_field = form.cleaned_data['tree_field']
            skill.checked = form.cleaned_data['checked']
            skill.parent = form.cleaned_data['parent']

            skill.bronzeCost = form.cleaned_data['bronzeCost']
            skill.silverCost = form.cleaned_data['silverCost']
            skill.goldCost = form.cleaned_data['goldCost']
            skill.platinumCost = form.cleaned_data['platinumCost']
            skill.save()
            return redirect('trees:mTreeDetail', id=tree_id)

    else:
        form = forms.mAddSkill(instance=skill)
        form.fields['parent'].queryset = models.mSkill.objects.filter(tree_field=tree)
    return render(request, 'trees/mEditSkill.html', {'form': form, 'tree_id': tree_id, 'skill_id': skill_id})


@permission_required('is.admin')
def mCloneTree(request, id):
    tree = models.Tree.objects.get(id=id)
    form = forms.CreateTree(instance=tree)
    skills = models.mSkill.objects.filter(tree_field=tree)
    newSkills = list(skills).copy()

    if request.method == 'POST':
        form = forms.CreateTree(request.POST)

        if form.is_valid():
            newTree = form.save()
            for skill in newSkills:
                skill.id = None
                skill.tree_field = newTree
                skill.save()
            return redirect('homepage')

    else:
        form = forms.CreateTree(instance=tree)
    return render(request, 'trees/mCloneTree.html', {'form': form, 'id': id})












