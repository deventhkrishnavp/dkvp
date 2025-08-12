from django.shortcuts import render
from .form import StudForm
def std(request):
    if request.method == 'POST':

            try:
                return render('/')
            except:
                pass
    else:
        form=StudForm()
        return render(request,'index.html',{'form':form})