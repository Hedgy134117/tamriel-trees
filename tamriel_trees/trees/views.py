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
    orders = {}

    for i in range(len(skillObjects)):
        if skillObjects[i].parent == None: 
            orders[skillObjects[i].name] = {}
            continue

        finished = False
        order = 0
        currentSkill = skillObjects[i]
        while finished == False:
            if currentSkill.parent == None:
                print(order, orders)
                if order not in orders[currentSkill.name]:
                    orders[currentSkill.name][order] = [skillObjects[i].name]
                else:
                    currentSkillList = orders[currentSkill.name][order]
                    currentSkillList.append(skillObjects[i].name)
                    orders[currentSkill.name][order] = currentSkillList
                finished = True
            else:
                currentSkill = currentSkill.parent
            order += 1

    print(orders)

    return render(request, 'trees/tree.html', {'tree': tree, 'skills': skillObjects, 'orders': orders})

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