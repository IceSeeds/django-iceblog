from django.shortcuts import render
from django.http import HttpResponse

import requests
from bs4 import BeautifulSoup



def index( request ):
    target_url  = "https://www.yahoo.co.jp/"
    res         = requests.get( target_url )
    soup        = BeautifulSoup( res.text, 'html.parser' )

    wrapper = soup.select_one( "#tabpanelTopics1" )
    ul      = wrapper.select_one( "ul" )
    news    = ul.select( "li" )

    ret_list = []
    for item in news:
        text = item.get_text()
        href = item.select_one( "a" ).get( 'href' )
        ret_list.append( [text, href] )

    context = {
        "list": ret_list,
    }

    return render( request, "index.html", context )

