from asyncio import tasks
from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order
    is successfully created.
    """
    order = Order.objects.get(id = order_id)
    subject = f'Order no. {order.id}'
    message = f'Dear {order.first_name}, \n\n' \
            f'You have successfully places an order.' \
            f'Your order ID is {order.id}'
    mail_send = send_mail(subject,message,'admin@myshop.com',[order.email])
    return mail_send