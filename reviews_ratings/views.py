from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
# from listings.models import Listing
from .models import Comment
from accounts.models import User, Tenant
from listings.models import Listing
from django.contrib import messages, auth
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth import get_user_model
User = get_user_model()


def create_comment(request, listing_id, user_id):
    if request.method == "POST":
        user = request.user

        if not user.is_authenticated:
            messages.error(request, "You need to be logged in to leave a comment")
            return render(request, "listings/listing.html")

        if user.groups.filter(name="landlords").count() != 0:
            messages.error(request, "You must be logged in as a tenant to leave a comment")
            return redirect("listing")

        tenant = get_object_or_404(Tenant, pk=user_id)
        if tenant.user_id == user.id:
            email = request.POST.get("email")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")

        listing = get_object_or_404(Listing, pk=listing_id)
        rating = request.POST.get("rating")
        text = request.POST.get("text")

        if not email and not first_name and not email:
            messages.error(request, "Kindly make sure all fileds are filled")
            return render(request, "reviews_ratings/comments.html")

        comment = Comment.objects.create(
            listing=listing,
            tenant = tenant,
            rating = rating,
            text = text,
        )
        comment.save()
        messages.success(request, "You have successfully left a comment for this listing")
        return render(request, "listings/listing.html", {"listing":listing})
          

    else:
        return HttpResponse(status=500)

def commenting(request, listing_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            messages.error(request, "Kindly Login to live a comment")
            return redirect("login")
        if user.groups.filter(name="landlords").count() !=0:
            messages.error(request, "Make sure you are a tenant to live a comment")
            return redirect("index")

        listing = get_object_or_404(Listing, pk=listing_id)
        
        if listing.tenant_id == user.id:
            return HttpResponse(status=500)
        else:
            
            return render(request, "reviews_ratings/comments.html", {"listing":listing})
    else:
        return HttpResponse(status=500)


