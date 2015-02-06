from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError

from lists.models import Item, List

# Create your views here.

def home_page(request):

	# if request.method == 'POST':
	# 	# new_item_text = request.POST['item_text']
	# 	# Item.objects.create(text=new_item_text)
	# 	Item.objects.create(text=request.POST['item_text'])
	# 	return redirect('/lists/the-only-list-in-the-world')

	# items = Item.objects.all()
	return render(request, 'home.html')


def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	return render(request, 'list.html', {'list' : list_})

def new_list(request):
	list_ = List.objects.create()
	item = Item(text=request.POST['item_text'], list=list_)
	# item = Item.objects.create(text=request.POST['item_text'], list=list_)

	try:
		item.full_clean()
		item.save()
	except ValidationError:
		list_.delete()
		error = "You can't have an empty list item"
		return render(request, 'home.html', {'error' : error})
		# pass

	return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))



	# else:
	# 	new_item_text = ''

	# item = Item()
	# item.text = request.POST.get('item_text', '')
	# item.save()

	# return render(request, 'home.html', {
	# 		'new_item_text' : new_item_text,
	# 	})

