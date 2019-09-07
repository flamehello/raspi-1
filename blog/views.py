from django.shortcuts import render
def index(requet):
        kl=requet.POST.get('hello')
        print(kl)
        return render(requet,'index.html')