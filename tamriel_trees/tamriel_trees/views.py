from django.shortcuts import render, redirect
from trees.models import Tree

def homepage(request):
    allTrees = Tree.objects.all()
    allTreesNames = { }
    for tree in allTrees:
        if tree.user in allTreesNames:
            allTreesNames[tree.user].append(tree)
        else:
            allTreesNames[tree.user] = [tree]
    trees = []
    for tree in allTrees:
        if tree.user == request.user:
            trees.append(tree)

    print(allTreesNames)

    if request.user.is_superuser:
        return render(request, 'homepage.html', {'trees': allTreesNames, 'admin': True})
    else:
        return render(request, 'homepage.html', {'trees': trees, 'admin': False})