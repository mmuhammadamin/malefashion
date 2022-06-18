from django import template

from apps.cart.models import Cart

register = template.Library()


@register.simple_tag(takes_context=True)
def get_user_cart(context):
    request = context['request']
    user = request.user
    cart = Cart.objects.filter(client=user, is_ordered=False).first()
    return cart
