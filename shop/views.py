from django.shortcuts import render


# Create your views here.

def home_view(request):
    itens = [{'id': 1, 'name': 'camera1', 'image': 'example.jpg', 'description': 'description 1111', 'price': 110},
             {'id': 2, 'name': 'camera2', 'image': 'example.jpg', 'description': 'description 2222', 'price': 220}]
    if 'id' not in request.session:
        # alter this to return login_view()
        context = {'itens': itens}
        return render(request, "shop/home.html", context)
        # return login_view(request)
    context = {'id': request.session['id']}
    return render(request, "shop/home.html", context)


def login_view(request):
    if request.method == 'POST':
        #if username and pasword matches in databse set session id
        return home_view(request)
    return render(request, "shop/login.html")


def register_view(request):
    if request.method == 'POST' and request.POST.get('password_confirm') == request.POST.get('password'):
        # create user in db
        # request.session['id'] = user_id()
        return home_view(request)
    return render(request, "shop/register.html")


def buy_view(request, idIten):
    # retrive iten from database using idTIten
    iten = {'id': 1, 'name': 'camera1', 'image': 'example.jpg', 'description': 'description 1111', 'price': 110}
    if request.method == 'POST':
        #add purchase on database
        return home_view(request)
    context = {
        'i': iten
    }
    return render(request, "shop/buy.html", context)


def purchase_view(request):
    # if 'id' not in request.session:
    #    return login_view(request)
    # get purchases from id session
    purchases = [{'id': 1, 'iten_name': 'camera1', 'quantity': 3, 'price': 300},
                 {'id': 2, 'iten_name': 'camera2', 'quantity': 1, 'price': 140}]
    context = {
        'purchases': purchases
    }
    return render(request, "shop/purchase.html", context)


def logout_view(request):
    if 'id' in request.session:
        flush()
    return login_view(request)
