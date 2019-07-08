from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from itertools import chain

from .models import *

from django.http import HttpResponse, HttpResponseRedirect


def test_cookie(request):

    url = 'http://s7.voscast.com:10196/armnews'

    if not request.COOKIES.get('radio'):
        response = HttpResponse("Cookie Set")
        response.set_cookie('radio', url)
        return response
    else:
        return HttpResponse("Your favorite color is {0}".format(request.COOKIES['radio']))


def search_results(request):
    header_items = Header.objects.all().first()
    footer = Footer.objects.all().first()
    slider = Slider.objects.all()
    search_query = request.GET.get('search', '')

    if search_query:
        interviews = Interview.objects.filter(Q(title_hy__icontains=search_query) |
                                              Q(title_ru__icontains=search_query) |
                                              Q(title_en__icontains=search_query) |
                                              Q(body_hy__icontains=search_query) |
                                              Q(body_ru__icontains=search_query) |
                                              Q(body_en__icontains=search_query))
        programs = Programs.objects.filter(Q(title_hy__icontains=search_query) |
                                           Q(title_ru__icontains=search_query) |
                                           Q(title_en__icontains=search_query) |
                                           Q(body_hy__icontains=search_query) |
                                           Q(body_ru__icontains=search_query) |
                                           Q(body_en__icontains=search_query) |
                                           Q(program_name_hy__icontains=search_query) |
                                           Q(program_name_ru__icontains=search_query) |
                                           Q(program_name_en__icontains=search_query) |
                                           Q(author_hy__icontains=search_query))
        broadcast = Broadcast.objects.filter(Q(title_hy__icontains=search_query) |
                                             Q(title_hy__icontains=search_query) |
                                             Q(title_hy__icontains=search_query))
        blog = Blog.objects.filter(Q(title_hy__icontains=search_query) |
                                           Q(title_ru__icontains=search_query) |
                                           Q(title_en__icontains=search_query) |
                                           Q(body_hy__icontains=search_query) |
                                           Q(body_ru__icontains=search_query) |
                                           Q(body_en__icontains=search_query) |
                                           Q(program_name_hy__icontains=search_query) |
                                           Q(program_name_ru__icontains=search_query) |
                                           Q(program_name_en__icontains=search_query) |
                                           Q(author_hy__icontains=search_query))

        results = chain(interviews, programs, broadcast, blog)

    context = {
        'header_items': header_items,
        'slider': slider,
        'results': results,
        'footer': footer,
    }

    return render(request, 'mainapp/search.html', context=context)




def header(request):
    header_items = Header.objects.all().first()
    gen_pic = GeneralPicture.objects.all().first()
    top_news = TopNews.objects.all()
    yt_url = GeneralVid.objects.all().first()
    interviews = Interview.objects.all()[:4]
    programs = Programs.objects.all()[:4]
    videos = GeneralVideos.objects.all().first()
    blog = Blog.objects.all()[:4]
    partners = Partners.objects.all().first()
    footer = Footer.objects.all().first()




    context = {
        'header_items': header_items,
        'gen_pic': gen_pic,
        'top_news': top_news,
        'yt_url': yt_url,
        'interviews': interviews,
        'programs': programs,
        'videos': videos,
        'blog': blog,
        'partners': partners,
        'footer': footer,
    }

    return render(request, 'mainapp/index.html', context=context)

def interviews(request):
    header_items = Header.objects.all().first()
    interviews = Interview.objects.all()
    slider = Slider.objects.all()
    interviews_random = Interview.objects.order_by("?")[:15]
    footer = Footer.objects.all().first()

    paginator = Paginator(interviews, 4)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''


    context = {
        'header_items': header_items,
        'interviews': interviews,
        'slider': slider,
        'interviews_random': interviews_random,
        'page_object': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url,
        'footer': footer,
    }

    return render(request, 'mainapp/interviews.html', context=context)


def programs(request):
    header_items = Header.objects.all().first()
    programs = Programs.objects.all()
    slider = Slider.objects.all()
    interviews_random = Interview.objects.order_by("?")[:15]
    footer = Footer.objects.all().first()

    paginator = Paginator(programs, 3)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''


    context = {
        'header_items': header_items,
        'programs': programs,
        'slider': slider,
        'interviews_random': interviews_random,
        'page_object': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url,
        'footer': footer,
    }

    return render(request, 'mainapp/projects.html', context=context)



def broadcasts(request, brod_slug=None):
    brodcastdate = None
    slider = Slider.objects.all()
    header_items = Header.objects.all().first()
    footer = Footer.objects.all().first()
    broadcastsdat = BroadcastDate.objects.all().first()
    broadcastsdates = BroadcastDate.objects.all()
    broadcasts = Broadcast.objects.filter(published=True)

    if brod_slug:
        brodcastdate = get_object_or_404(BroadcastDate, slug=brod_slug)
        broadcasts = Broadcast.objects.filter(broadcastdate=brodcastdate)





    context = {
        'header_items': header_items,
        'brodcastdate': brodcastdate,
        'broadcastsdates': broadcastsdates,
        'broadcasts': broadcasts,
        'broadcastsdat': broadcastsdat,
        'slider': slider,
        'footer': footer,
    }

    return render(request, 'mainapp/broadcast.html', context=context)





def blog(request):
    header_items = Header.objects.all().first()
    bloging = Blog.objects.all()
    slider = Slider.objects.all()
    interviews_random = Interview.objects.order_by("?")[:15]
    footer = Footer.objects.all().first()

    paginator = Paginator(bloging, 3)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''


    context = {
        'header_items': header_items,
        'bloging': bloging,
        'slider': slider,
        'interviews_random': interviews_random,
        'page_object': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url,
        'footer': footer,
    }

    return render(request, 'mainapp/blog.html', context=context)



def aboutus(request):
    header_items = Header.objects.all().first()
    slider = Slider.objects.all()
    aboutus = AboutUs.objects.all().first()
    footer = Footer.objects.all().first()



    context = {
        'header_items': header_items,
        'slider': slider,
        'aboutus': aboutus,
        'footer': footer,
    }

    return render(request, 'mainapp/aboutus.html', context=context)




def programsDetail(request, slug):
    header_items = Header.objects.all().first()
    slider = Slider.objects.all()
    footer = Footer.objects.all().first()
    program_detail = get_object_or_404(Programs, slug=slug)
    template = 'mainapp/morepage.html'
    context = {
        'program_detail': program_detail,
        'slider': slider,
        'header_items': header_items,
        'footer': footer,
    }
    return render(request, template, context)

def blogDetail(request, slug):
    header_items = Header.objects.all().first()
    slider = Slider.objects.all()
    footer = Footer.objects.all().first()
    program_detail = get_object_or_404(Programs, slug=slug)
    template = 'mainapp/morepage.html'
    context = {
        'program_detail': program_detail,
        'slider': slider,
        'header_items': header_items,
        'footer': footer,
    }
    return render(request, template, context)



def error_404(request, exception):
    header_items = Header.objects.all().first()
    slider = Slider.objects.all()
    footer = Footer.objects.all().first()

    context = {
        'slider': slider,
        'header_items': header_items,
        'footer': footer,
    }
    return render(request, 'mainapp/error404.html', context)



