from .models import Category

def category_menu(request):

    link_menu = Category.objects.all()
    return {
        'cat_menu': link_menu
    }