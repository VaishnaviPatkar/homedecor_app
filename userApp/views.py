from django.shortcuts import render, redirect
from adminApp.models import item_category, item,payment
from django.http import HttpResponse
from userApp.models import userInfo, myCart ,orderMaster
from django.contrib import messages

# Create your views here.


def home(request):
    items = item_category.objects.all()
    return render(request, "homeDecor.html", {"items": items})


def home_page(request):
    return redirect(home)

def show_item(request, id):
    cats = item_category.objects.all()
    items = item.objects.filter(category=id)
    return render(request, "show_item.html", {"items": items, "cats": cats})


def view_item(request, id):
    cats = item_category.objects.all()
    items = item.objects.filter(id=id)
    return render(request, "view.html", {"items": items, "cats": cats})


def login(request):
    if (request.method == "GET"):
        return render(request, 'login.html', {})
    else:
        userName = request.POST["uname"]
        password = request.POST["pwd"]
        try:
            # if alredy present
            user = userInfo.objects.get(userName=userName, password=password)
        except:
            message = "Please try again"
            return render(request, 'login.html', {"message": message})
        else:
            # if logn is successful we create session
            request.session['userName'] = userName
            return redirect(home)


def signup(request):
    if (request.method == "GET"):
        return render(request, 'signup.html', {})
    else:
        userName = request.POST["uname"]
        password = request.POST["pwd"]
        try:
            user = userInfo.objects.get(userName=userName, password=password)
        except:
            user = userInfo(userName, password)
            user.save()
            # return HttpResponse("login successfully")
            return redirect(home)
        else:
            message = "This user alredy exist"
            return render(request, 'signup.html', {"message": message})


def logout(request):
    # session is deleted
    request.session.clear()
    return redirect(home)


def addToCart(request):
    if ('userName' in request.session):
        user = userInfo.objects.get(userName=request.session['userName'])
        # GET ITEM INFORMATION
        item_id = request.POST['I_id']
        myitem = item.objects.get(id=item_id)
        qyt = request.POST['qyt']
        try:
            it = myCart.objects.get(user=user,item=myitem)
        except:
            cart = myCart()
            cart.user = user
            cart.item = myitem
            cart.qyt = qyt
            cart.save() 
            messages.info(request,"Successfully added to cart ")
            return redirect(showCartItems)
            
        else:
            messages.info(request,"Item alredy present in cart")
            return redirect(showCartItems)

    else:
        return redirect(login)


def showCartItems(request):
    if (request.method == "GET"):
        my_item = myCart.objects.filter(user=request.session['userName'])
        total = 0
        for it in my_item:
            total += it.qyt * it.item.item_price
        request.session['total'] = total
        return render(request, 'showCartItems.html', {'my_item': my_item})
    else:
        cart_id = request.POST['cart_id']
        item = myCart.objects.get(id=cart_id)
        action = request.POST['action']
        if (action == 'delete'):
            item.delete()
            return redirect(showCartItems)
        else:
            qyt = request.POST['qyt']
            item.qyt = qyt
            item.save()
            return redirect(showCartItems)


def make_payment(request):
    if (request.method == "GET"):
        return render(request, 'make_payment.html', {})
    else:
        card_number = request.POST['card_number']
        car_name = request.POST['car_name']
        Expire = request.POST['Expire']
        Cvv = request.POST['Cvv']
        try:
            buyer = payment.objects.get(card_no=card_number, name=car_name, expiry=Expire, cvv=Cvv)
        except:
            return redirect(make_payment)
        else:
            owner = payment.objects.get(card_no='12345',name ='Vaishnavi naresh patkar',expiry='12/2024',cvv='123')
            buyer.balance -= float(request.session['total'])
            owner.balance += float(request.session['total'])
            buyer.save()
            owner.save()

            myorder = orderMaster()
            myorder.user = userInfo.objects.get(userName = request.session['userName'])
            myorder.amount = request.session['total']
            products = myCart.objects.filter(user = myorder.user)
            details = ' '
            for product in products:
                details += product.item.item_name + ' '
                product.delete()
            myorder.details = details
            myorder.save()
            return redirect(home)
            

