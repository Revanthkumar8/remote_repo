from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    my_dict={'insert_date':date}
    return render(request,'testApp/wish.html',context=my_dict)
