from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def takeSnap(url):
    #coding=utf-8                                                                                                                                                                              
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    URL=url

    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)


    driver.get(URL)

    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
    driver.find_element_by_tag_name('body').screenshot('static/output.jpg')


def home(request):
    return render(request, 'home.html',context=None)
    
def snap(request):
    takeSnap(request.GET.get("url"))
    return HttpResponse("static/output.jpg")
    