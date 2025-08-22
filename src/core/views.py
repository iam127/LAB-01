from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Item

def item_list(request):
    """Display all items"""
    items = Item.objects.all()
    return render(request, 'core/item_list.html', {'items': items})

def add_item(request):
    """Add new item via POST request"""
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        
        if name:
            Item.objects.create(name=name, description=description)
            messages.success(request, 'Item added successfully!')
        else:
            messages.error(request, 'Name is required!')
    
    return redirect('item_list')