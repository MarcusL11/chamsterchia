from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from .models import Chamster

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

    # Apply pagination
    try:
        page = request.GET.get("page", 1)
        chamsters = paginator.page(page)
    except EmptyPage:
        chamsters = paginator.page(paginator.num_pages)

    # Extracting unique values from attributes
    unique_values = {}
    for param in query_params[:-1]:  # Exclude 'ordering' from unique values extraction
        unique_values[param.replace('search_', 'unique_')] = (
            Chamster.objects.values(param.replace('search_', '')).distinct().order_by(param.replace('search_', ''))
        )

    main_data = {"chamster": chamsters, **unique_values}

    return render(request, "chamsterapp/nft-gallery.html", main_data)
    