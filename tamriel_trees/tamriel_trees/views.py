from django.shortcuts import render, redirect
from trees.models import Tree

def homepage(request):
    allTrees = Tree.objects.all()
    trees = []
    for tree in allTrees:
        if tree.user == request.user:
            trees.append(tree)

    if request.user.is_superuser:
        return render(request, 'homepage.html', {'trees': allTrees})
    else:
        return render(request, 'homepage.html', {'trees': trees})