from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')


def ref(request):
    return render(request, 'main/ref.html')


def token_investing(request):
    return render(request, 'main/token_investing.html')


def airdrop(request):
    return render(request, 'main/airdrop.html')


def nft_collection(request):
    return render(request, 'main/nft_collection.html')


