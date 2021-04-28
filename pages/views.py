from django.shortcuts import get_object_or_404, render
from listings.models import Listing
from listings.choices import bedroom_choices, room_type_choices, price_choices
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'room_type_choices': room_type_choices,
        'price_choices': price_choices,
        'listings': paged_listings
    }
    return render(request,'pages/index.html', context)

    


# def comment(request):
#     pass
   
#     return render(request, 'pages/comments.html')


