from django.shortcuts import render, redirect
from .forms import ItemForm
from django.contrib import auth, messages
from .models import Item

def show_items(request):
    items = Item.objects.all()
    return render(request, 'tasks/show_items.template.html', {
        'items':items
    })

# Create your views here.
def create_item(request):
    if request.method == "POST":
        # create the form and fill it in with the user input
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New item has been added successfully!")
            return redirect(create_item)
        else:
             return render(request, "tasks/create_item.template.html", {
                'form':form
            })
    else:
        form = ItemForm()
        return render(request, "tasks/create_item.template.html", {
            'form':form
        })