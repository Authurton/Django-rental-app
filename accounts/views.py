from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import Group
from django.contrib import messages, auth
from .models import Landlord, Tenant
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
from contacts.models import Contact
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from listings.models import Listing
from django.db.models import Q
User = get_user_model()


def login(request):
    if request.method == 'POST':
      email = request.POST['email']
      password = request.POST['password']
      

      user = auth.authenticate(email=email, password=password)
      if user is not None:
              auth.login(request, user)
              messages.success(request, 'You are now logged in')
              return redirect("login_after")
      else:
              messages.error(request, 'Invalid credentials')
              return redirect('login')

    else:
        return render(request, 'accounts/login.html')

def login_after(request):
        if request.method == "GET":
                user = request.user
                
                if user.groups.filter(name='landlords').count() == 0:
                        return redirect("index")                             
                else:
                        
                        # return redirect(reverse("land_diff", kwargs={"user_id":user.id}))
                        return render(request, "accounts/final_dash.html")
        else:
                return HttpResponse(status=500)

def logout(request):
        # logout(request)
        if request.method == 'POST':
                auth.logout(request)
                messages.success(request, 'You are now logged out')
        return redirect('index')


# def register(request):
#         if request.user.is_authenticated:
#                 return redirect('index')
#         return render(request, 'accounts/register.html')

def register(request):

        if request.method =='POST':
        
# Get form values
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                email = request.POST['email']
                password = request.POST['password']
                password2 = request.POST['password2']
                
                landlord = False

                try:
                        if request.POST['landlord']:
                                landlord = True
                except KeyError:
                        landlord = False
                if password == password2:


                        if email is not None and first_name is not None and last_name is not None and password is not None and password2 is not None:
                                # print('not none')
                                if not email or not first_name or not last_name or not password or not password2:
                                        
                                        return render(request, "accounts/register.html",{"error":"Please fill in all required fields"})

                                if User.objects.filter(email=email).exists():
                                        messages.error(request,'Email already exists')
                                        return render(request, 'accounts/register.html')
                                        # return render(request, 'accounts/register.html', {'error': 'Email already exists'})
                                # user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                # password=None)
                                
                                user = get_user_model().objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
                                # group = Group.objects.get(id=group)
                                
                                if landlord:
                                        if Group.objects.filter(name='landlords').exists():
                                                landlord_group = Group.objects.get(name='landlords')
                                        else:
                                                Group.objects.create(name='landlords').save()
                                                landlord_group = Group.objects.get(name='landlords')
                                        landlord_group.user_set.add(user)
                                        # user.landlords.add(landlord_group)
                                        
                                        Landlord.objects.create(user=user).save()
                                else:
                                        Tenant.objects.create(user=user).save()
                                user.save()
                        
                        messages.success(request, 'You are now registered, you can login')
                        return redirect('login')
                else:

                        return render(request,"accounts/register.html", {"error":"Passwords do not match"})

        else:
                return render(request,'accounts/register.html')

def land_diff(request, user_id):
        user = request.user
        if request.method == "GET":
                
                landlord = get_object_or_404(Landlord, pk=user_id)
                if landlord.user_id == user.id:
                        phone = request.POST.get("phone")
                        whatsapp = request.POST.get("whatsapp")
                        if Landlord.objects.filter(phone__isnull=True):
                                return render(request, "accounts/landlord_edit.html", {"user":user})
                        else:
                                return render(request, "accounts/landlord_dash.html", {"user":user})

        return HttpResponse(status=500)

def dashboard(request):
        user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
        context = {
                'contacts': user_contacts,
        }
        return render(request, 'accounts/dashboard.html', context)

def landlord_dash(request):
        user_listings = Listing.objects.order_by('-list_date').filter(landlord_id=request.user.id)
        context={
                "listings":user_listings,
        }
        return render(request, "accounts/final_dash.html", context)

def listing_dashboard(request, user_id): 
        
        if request.method == "POST":
                
                user = get_user_model()
                
                if 'photos' in request.FILES:
                        photos = request.FILES['photos/%Y/%m/&d']
                
                # landlord = False

                # try:
                #         if request.POST['landlord']:
                #                 landlord = True
                #         first_name = request.POST.get('first_name')
                #         last_name = request.POST.get('last_name')
                #         phone = request.POST.get('phone')
                #         whatsapp = request.POST.get('whatsapp')
                #         email = request.POST.get("email")
                #         photo = request.POST.get("photo")

                # except KeyError:
                #         landlord = False
                landlord = get_object_or_404(Landlord, pk=user_id)
                if landlord.user_id == user.id:
                        phone = request.POST['phone']
                        whatsapp = request.POST['whatsapp']
                        email = request.POST["email"]
                        first_name = request.POST["first_name"]
                        last_name = request.POST["last_name"]
                        photo_landlord = request.FILES["photo_landlord"]

                
                address = request.POST.get('address')
                
                city = request.POST.get('city')
                price = request.POST.get('price')
                room_type = request.POST.get('room_type')
                bedroom = request.POST.get('bedroom')
                bathroom = request.POST.get("bathroom")
                garage = request.POST.get('garage')
                wifi = request.POST.get('wifi') 
                is_published = request.POST.get('is_published', True)
                description = request.POST.get('description')
                photo_main = request.FILES.get('photo_main')
                photo_1 = request.FILES.get('photo_1')
                photo_2 = request.FILES.get('photo_2')
                photo_3 = request.FILES.get('photo_3')
                photo_4 = request.FILES.get('photo_4')
                photo_5 = request.FILES.get('photo_5')
                photo_6 = request.FILES.get('photo_6')

                

                # fs = FileSystemStorage()
                # filename = fs.save(photo_main, photos)
                # upload_file_url = fs.url(filename)
                


                if address is not None and city is not None and price is not None and room_type is not None and bathroom is not None and garage is not None and photo_main is not None and photo_1 is not None and photo_2 is not None and photo_3 is not None:
                        if not address or not city or not price or not  room_type or not bedroom or not bathroom or not  garage or not description or not photo_main or not photo_1 or not photo_2 or not photo_3:

                                messages.error(request, 'Kindly fill in all the required fields')

                                return render(request, 'accounts/landlord_dash.html')

                        if Listing.objects.filter(address=address).exists():
                                messages.error(request, 'This listing already exists')
                                return render(request, 'accounts/landlord_dash.html')
                                
                        # if request.POST.get('landlord'):
                        #         landlord = True

                        listing = Listing.objects.create(
                                landlord=landlord,                       
                                address=address,
                                city = city,
                                price = price,
                                room_type = room_type,
                                bedroom = bedroom,
                                bathroom = bathroom,
                                garage = garage,
                                wifi  = wifi,
                                # is_published = is_published,
                                description = description,
                                photo_main = photo_main,
                                photo_1 = photo_1,
                                photo_2 = photo_2,
                                photo_3 = photo_3,
                                photo_4 = photo_4,
                                photo_5 = photo_5,
                                photo_6 = photo_6,
                        )

                        
                        # if is_published == 'on':
                        #         is_published = True
                        # else:
                        #         is_published = False
                        
                        
                        # landlord = Landlord(email=email,first_name=first_name,last_name=last_name,phone=phone,whatsapp=whatsapp, photo=photo)
                        # landlord.save()
                        # listing.append(landlord)
                        listing.save()
                messages.success(request, 'You have successfully uploaded your listing, thank you')
                return render(request, "accounts/final_dash.html", {"landlord":landlord})

        else:
                return render(request, 'accounts/landlord_dash.html')
                

                

def landlord_edit(request, user_id):
        if request.method == "GET":
                user = request.user
                # if not user.is_authenticated:
                #         return redirect("login")
                # if user.groups.filter(name="landlords").count() == 0:
                        
                #         return render(request, "accounts/lanlord_edit.html", {"landlord":landlord})
                
                # landlord = get_object_or_404(Landlord, pk=landlord_id)
                if Group.objects.filter(name='landlords').exists():
                        try:
                                landlord = Landlord.objects.get(pk=user_id)
                                
                        except Landlord.DoesNotExist:
                                messages.error(request, "An error has occurred")
                                return render(request, "accounts/landlord_edit.html", {"landlord":landlord})
                
                if landlord.user_id == user.id:
                        return render(request, "accounts/landlord_edit.html", {"landlord":landlord})
                else:
                        messages.error(request, "An error occured, kindly make sure you are a landlord")
                        return render(request, 'accounts/landlord_edit.html', {"landlord":landlord})

        else:
                messages.error(request, "An error occured, kindly make sure you are a landlord")
                return render(request, 'accounts/landlord_edit.html', {"landlord":landlord})


def landlord_update(request,user_id):
        if request.method == 'POST':
                user = request.user
                if not user.is_authenticated:
                        return redirect('login')
                if 'photos' in request.FILES:
                        photos = request.FILES['photos/%Y/%m/&d']

                if user.groups.filter(name='landlords').count() == 0:
                        return redirect('index')
                landlord = get_object_or_404(Landlord, pk=user_id)
                if landlord.user_id == user.id:
                # if landlord_id=request.user.id
                        phone = request.POST['phone']
                        whatsapp = request.POST['whatsapp']
                        photo_landlord = request.FILES.get('photo_landlord')
                        
                        if not phone and not whatsapp and not photo_landlord:
                                messages.error(request, 'Kindly fill in all the required fields')
                                return render(request, 'accounts/landlord_edit.html', {'landlord':landlord})

                        if phone.strip():
                                Landlord.objects.filter(pk=user_id).update(phone=phone)
                                
                        if whatsapp.strip():
                                Landlord.objects.filter(pk=user_id).update(whatsapp=whatsapp)

                        if photo_landlord:
                                Landlord.objects.filter(pk=user_id).update(photo_landlord=photo_landlord)
                        
                        messages.success(request, 'Your cridentials have been updated')
                        return render(request, 'accounts/landlord_dash.html', {"landlord":landlord})
                        
                else:
                        return HttpResponse(status=500)

        else:
                
                return HttpResponse(status=500)

def edit_info(request, user_id):
        if request.method == "GET":
                user = request.user
                if Group.objects.filter(name='landlords').exists():
                        try:
                                landlord = Landlord.objects.get(pk=user_id)
                                
                        except Landlord.DoesNotExist:
                                messages.error(request, "An error has occurred")
                                return render(request, "accounts/final_dash.html", {"landlord":landlord})
                
                if landlord.user_id == user.id:
                        return render(request, "accounts/edit_info.html", {"landlord":landlord})
                else:
                        messages.error(request, "An error occured, kindly make sure you are a landlord")
                        return render(request, 'accounts/final_dash.html', {"landlord":landlord})

        else:
                messages.error(request, "An error occured, kindly make sure you are a landlord")
                return render(request, 'accounts/landlord_edit.html', {"landlord":landlord})


def edit_info_save(request, user_id):
        if request.method == "POST":
                user = request.user
                landlord = get_object_or_404(Landlord, pk=user_id)
                if landlord.user_id == user.id:
                        phone = request.POST.get("phone")
                        whatsapp = request.POST.get("whatsapp")
                        photo_landlord = request.FILES.get('photo_landlord')

                        if 'photos' in request.FILES:
                                photos = request.FILES['photos/%Y/%m/&d']

                        if not phone and not whatsapp and not photo_landlord:
                                messages.error(request, 'Kindly fill in all the required fields')
                                return render(request, 'accounts/edit_info.html', {'landlord':landlord})

                        if phone.strip():
                                Landlord.objects.filter(pk=user_id).update(phone=phone)
                                
                        if whatsapp.strip():
                                Landlord.objects.filter(pk=user_id).update(whatsapp=whatsapp)

                        if photo_landlord:
                                Landlord.objects.filter(pk=user_id).update(photo_landlord=photo_landlord)
                        else:
                                Landlord.objects.filter(pk=user_id).update(photo_landlord=photo_landlord)

                        messages.success(request, 'Your cridentials have been updated')
                        return render(request, 'accounts/final_dash.html', {"landlord":landlord})
                else:
                        return HttpResponse(status=500)
        else:
                return HttpResponse(status=500)

        