from django.shortcuts import render


# Create your views here.
# renders to my page one which is also my index
def page1(request):
    return render(request, "cssApp/page1.html")


# renders to my page two
def page2(requet):
    return render(requet, "cssApp/page2.html")


# renders to my page 3
def page3(request):
    return render(request, "cssApp/page3.html")
