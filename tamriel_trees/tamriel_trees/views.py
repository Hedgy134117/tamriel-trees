from django.shortcuts import render, redirect
from trees.models import Tree

def homepage(request):
    allTrees = Tree.objects.all()
    trees = []
    for tree in allTrees:
        if tree.user == request.user:
            trees.append(tree)

    return render(request, 'homepage.html', {'trees': trees})