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
    skillObjects = models.Skill.objects.filter(tree=tree)
    unordered = list(skillObjects)
    orderedDict = { }
    ordered = [ ]
    orderedList = [ ]

    for skill in skillObjects:
        order = 0
        finishedOrder = False
        skillCheck = skill
        while not finishedOrder:
            if not skillCheck.parent:
                if order in orderedDict.keys():
                    orderedDict[order].append(skill)
                else:
                    orderedDict[order] = [skill]
                finishedOrder = True
            else:
                order += 1
                skillCheck = skillCheck.parent

    for skills in orderedDict.values():
        for skill in skills:
            ordered.append(skill)
        ordered.append('in')
    ordered.pop()
    lastIndex = 0
    for i in range(len(ordered)):
        if ordered[i] == 'in':
            currentList = ordered[lastIndex:i]
            if 'in' in currentList: currentList.remove('in')
            orderedList.append(currentList)
            lastIndex = i

    indexes = [0 for l in orderedList]
    index = 0
    previousSkill = None
    isFinished = False
    while not isFinished:
        # print(previousSkill, "<", orderedList[index][indexes[index]], indexes, "\n")
        if orderedList[index][indexes[index]].parent == previousSkill:
            print(orderedList[index][indexes[index]])
        
        previousSkill = orderedList[index][indexes[index]]
        if index == len(orderedList) - 1:
            index = 0
            anyPossiblePath = False
            for l in range(len(orderedList) - 1, 0, -1):
                if len(orderedList[l]) - 1 != indexes[l]:
                    anyPossiblePath = True
                    indexes[l] += 1
                    break
            if not anyPossiblePath:
                isFinished = True
        else:
            index += 1

    print(orderedList)

    return render(request, 'trees/treeRevised.html', {'tree': tree })

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

@permission_required('is.admin')
def editSkill(request, treeId, skillId):
    tree = models.Tree.objects.get(id=treeId)
    skill = models.Skill.objects.get(id=skillId)
    form = forms.AddSkill(instance=skill)

    if request.method == 'POST':
        form = forms.AddSkill(request.POST)

        if form.is_valid():
            skill.name = form.cleaned_data['name']
            skill.description = form.cleaned_data['description']
            skill.tree = form.cleaned_data['tree']
            skill.checked = form.cleaned_data['checked']
            skill.parent = form.cleaned_data['parent']

            skill.bronzeCost = form.cleaned_data['bronzeCost']
            skill.silverCost = form.cleaned_data['silverCost']
            skill.goldCost = form.cleaned_data['goldCost']
            skill.platinumCost = form.cleaned_data['platinumCost']
            skill.save()
            return redirect('trees:treeDetail', id=treeId)

    else:
        form = forms.AddSkill(instance=skill)
        form.fields['parent'].queryset = models.Skill.objects.filter(tree=tree)
    return render(request, 'trees/editSkill.html', {'form': form, 'tId': treeId, 'sId': skillId})

@permission_required('is.admin')
def cloneTree(request, id):
    tree = models.Tree.objects.get(id=id)
    form = forms.CreateTree(instance=tree)
    skills = models.Skill.objects.filter(tree=tree)
    newSkills = list(skills).copy()

    if request.method == 'POST':
        form = forms.CreateTree(request.POST)

        if form.is_valid():
            newTree = form.save()
            for skill in newSkills:
                skill.id = None
                skill.tree = newTree
                skill.save()
            return redirect('homepage')

    else:
        form = forms.CreateTree(instance=tree)
    return render(request, 'trees/cloneTree.html', {'form': form, 'id': id})












