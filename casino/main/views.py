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


def home_view(request):
    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
    domain_url = 'https://127.0.0.1:8000/'
    product = {
        'name': 'Coffee',
        'description': 'A really good local coffee.',
        'local_price': {
            'amount': '5.00',
            'currency': 'USD'
        },
        'pricing_type': 'fixed_price',
        'redirect_url': domain_url + 'success/',
        'cancel_url': domain_url + 'cancel/',
        'metadata': {
            'customer_id': request.user.id if request.user.is_authenticated else None,
            'customer_username': request.user.username if request.user.is_authenticated else None,
        },
    }
    charge = client.charge.create(**product)

    return render(request, 'main/payments.html', {
        'charge': charge,
    })


def success_view(request):
    return render(request, 'main/success.html', {})


def cancel_view(request):
    return render(request, 'main/cancel.html', {})


#Эта залупа должна вызываться каждый раз когда платеж подтверждается xd
#(Этот блок кода проверяет подпись и полезную нагрузку запроса, а затем генерирует на их основе событие)

@csrf_exempt
@require_http_methods(['POST'])
def coinbase_webhook(request):
    logger = logging.getLogger(__name__)

    request_data = request.body.decode('utf-8')
    request_sig = request.headers.get('X-CC-Webhook-Signature', None)
    webhook_secret = settings.COINBASE_COMMERCE_WEBHOOK_SHARED_SECRET

    try:
        event = Webhook.construct_event(request_data, request_sig, webhook_secret)
        if event['type'] == 'charge:confirmed':
            logger.info('Payment confirmed.')
            customer_id = event['data']['metadata']['customer_id']
            customer_username = event['data']['metadata']['customer_username']

    except (SignatureVerificationError, WebhookInvalidPayload) as e:
        return HttpResponse(e, status=400)

    logger.info(f'Received event: id={event.id}, type={event.type}')
    return HttpResponse('ok', status=200)