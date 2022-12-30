from django.shortcuts import render

# Create your views here.
def filters(request):
    import datetime
    datetime=datetime.date.today()



    data={'data':'I love my soul ','datetime':datetime,'c':1}
    return render(request,'filters.html',data,datetime)

def usdf(request):
    d={'data':'I am waiting my girl '}
    return render(request,'usdf.html',d)


  
  