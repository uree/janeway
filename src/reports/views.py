__copyright__ = "Copyright 2017 Birkbeck, University of London"
__author__ = "Martin Paul Eve & Andy Byers"
__license__ = "AGPL v3"
__maintainer__ = "Birkbeck Centre for Technology and Publishing"


from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.management import call_command

from submission import models
from identifiers import models as ident_models


def index(request):

    template = 'reports/index.html'
    context = {}

    return render(request, template, context)


def metrics(request):

    articles = models.Article.objects.filter(journal=request.journal, stage=models.STAGE_PUBLISHED)
    paginator = Paginator(articles, 25)

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    template = 'reports/metrics.html'
    context = {
        'articles': articles,
    }

    return render(request, template, context)


def dois(request):

    broken_dois = ident_models.BrokenDOI.objects.filter(article__journal=request.journal)

    if request.POST and 'run' in request.POST:
        call_command('doi_check')
        return redirect(reverse('reports_dois', request.journal.code))

    template = 'reports/dois.html'
    context = {
        'broken_dois': broken_dois,
    }

    return render(request, template, context)
