from django.shortcuts import redirect


def redirect_root_view(request):
    return redirect('Tripvisor_tour_list_urlpattern')
