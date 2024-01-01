from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from .models import Chamster
from django.db.models import Avg

# Create your views here.

def home(request):
    return render(request, "chamsterapp/index.html")

def nftGallery(request):
    query_params = [
        "search_name", "search_background", "search_fur", "search_shirt", 
        "search_pants", "search_head", "search_eyes", "search_club", 
        "search_power", "search_putting", "search_accuracy", "search_recovery", 
        "search_luck", "search_specialty", "search_tsi", "ordering"
    ]

    # Retrieve query parameters
    filters = {}
    ordering = None

    for param in query_params:
        value = request.GET.get(param)
        if param == "ordering" and value:
            ordering = value
        elif value:
            filters[param.replace('search_', '') + '__iexact'] = value

    # Filter the Chamster model based on query parameters
    chamsters = Chamster.objects.filter(**filters)

    # Apply ordering
    # ordering = request.GET.get("ordering")
    if ordering:
        if ordering == 'tsi':
            chamsters = chamsters.order_by('tsi')   
        elif ordering == '-tsi':
            chamsters = chamsters.order_by('-tsi')
        else:
            # Handle other ordering cases if needed
            pass


    # Paginate the results
    items_per_page = 24
    perpage = request.GET.get("perpage", items_per_page)
    paginator = Paginator(chamsters, perpage)
    page_number = request.GET.get("page", 1)
    total_pages = paginator.num_pages
    page_param = request.GET.get("page")
    all_items = chamsters.count()

    # Extracting unique values from attributes
    unique_values = {}
    for param in query_params[:-1]:  # Exclude 'ordering' from unique values extraction
        unique_values[param.replace('search_', 'unique_')] = (
            Chamster.objects.values(param.replace('search_', '')).distinct().order_by(param.replace('search_', ''))
        )

    # Apply pagination
    try:
        chamsters = paginator.page(page_number)
    except EmptyPage:
        chamsters = paginator.page(paginator.num_pages)

    if page_param and page_param.isdigit() and int(page_param) > 1:
        current_items = items_per_page * int(page_param)
    else:
        current_items = items_per_page
    
    main_data = {
        "chamster": chamsters, 
        "page_number" : page_number,
        "total_pages": total_pages,
        "current_items": current_items,
        "all_items": all_items, 
        **unique_values
    }

    return render(request, "chamsterapp/nft-gallery.html", main_data)

def nftProfile(request, pk=None):
    if pk:
        nft_profile = Chamster.objects.get(pk=pk)
        chamsters = Chamster.objects.all()
        average_power = chamsters.aggregate(avg_power=Avg('power'))['avg_power']
        average_accuracy = chamsters.aggregate(avg_accuracy=Avg('accuracy'))['avg_accuracy']
        average_luck = chamsters.aggregate(avg_luck=Avg('luck'))['avg_luck']
        average_recovery = chamsters.aggregate(avg_recovery=Avg('recovery'))['avg_recovery']
        average_putting = chamsters.aggregate(avg_putting=Avg('putting'))['avg_putting']

        profile_data = {
            "nft_profile": nft_profile,
            "avg_data": [
                average_power,
                average_accuracy,
                average_luck,
                average_recovery,
                average_putting,
            ],
            "radar_data": [
                nft_profile.power, 
                nft_profile.accuracy, 
                nft_profile.luck, 
                nft_profile.recovery, 
                nft_profile.putting
            ],
        }
        return render(request, "chamsterapp/nft-profile.html", profile_data)
    else:
        nft_profile = "Error"
        return render(request, "chamsterapp/nft-profile.html", {"nft_profile": nft_profile})

