from django.shortcuts import render, redirect
import requests

def index(request):
    return render(request, 'index.html')
    
def search(request):
    if request.method == 'POST':
        keyword = request.POST.get('city')

        if(' ' in keyword):
            keyword = keyword.replace(' ', '%20')

        response = requests.get(f'https://api.waqi.info/feed/{keyword}/?token=93d1c1ecfc0793f7da015365c9aee2cd88de7a5e')
        data = response.json()
        if(data['status'] == 'ok'):
            context = {'status': True, 'data': data['data']}
        else:
            context = {'status': False}
        return render(request, 'result.html', context)

    return redirect('/')

def opinion(request):
    return render(request, 'saran.html')