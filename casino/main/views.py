import logging

from coinbase_commerce.client import Client
from coinbase_commerce.error import SignatureVerificationError, WebhookInvalidPayload
from coinbase_commerce.webhook import Webhook
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from casino import settings

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


