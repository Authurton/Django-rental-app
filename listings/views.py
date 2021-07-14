from django.shortcuts import get_object_or_404, render
from .models import Listing
from reviews_ratings.models import Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages, auth
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import bedroom_choices, room_type_choices, price_choices
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id )
    comments = Comment.objects.order_by("-create_date")[:2]
    context = {
        'listing':listing,
        "comment":comments
    }

    return render(request, 'listings/listing.html', context)

def listing_upload(request, user_id):
    user = request.user
    if request.method == "GET":
        if not user.is_authenticated:
            return HttpResponse(status=500)
        else:
            return render(request, "accounts/landlord_dash.html", {"user":user})
    else:
        return HttpResponse(status=500)

def edit_listing(request, listing_id):
    if request.method == "GET":
        pass

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    
    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    #city
    if 'city' in request.GET:
        city = request.GET['city']

        # if not city:
        #     messages.error(request, 'Kindly provide a city')
        # return render(request, 'pages/index.html')

        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    #provinces
    if 'room_type' in request.GET:
        room_type = request.GET['room_type']
        if room_type:
            queryset_list = queryset_list.filter(room_type__iexact=room_type)

    #bedrooms
    if 'bedroom' in request.GET:
        bedroom = request.GET['bedroom']
        if bedroom:
            queryset_list = queryset_list.filter(bedroom__lte=bedroom)

    #prices
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {

        'bedroom_choices': bedroom_choices,
        'room_type_choices': room_type_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'pages/search.html', context )
    