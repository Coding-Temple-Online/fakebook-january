from flask_login import current_user
from app.blueprints.ecommerce.models import Cart
from .import bp as app
import stripe
from flask import current_app, jsonify, redirect, request
from app import db

stripe.api_key = current_app.config.get('STRIPE_TEST_SECRET_KEY')

@app.route('/products')
def get_products():
    # print(stripe.Product.list()['data'])
    return jsonify([dict(
        id=p['id'],
        description=p['description'],
        image=p['images'][0],
        name=p['name'],
        price=stripe.Price.retrieve( p['metadata']['price'] )['unit_amount'],
    ) for p in stripe.Product.list()['data']])

@app.route('/products/<id>')
def get_product(id):
    # print(stripe.Product.list()['data'])
    p = stripe.Product.retrieve(id)
    return jsonify(dict(
        id=p['id'],
        description=p['description'],
        image=p['images'][0],
        name=p['name'],
        price=stripe.Price.retrieve( p['metadata']['price'] )['unit_amount'],
    ))

@app.route('/products/checkout', methods=['POST'])
def checkout():
    items = []
    cart_data = request.get_json()['cartData']

    print(cart_data)
    # # for item in Cart.query.filter_by(user_id=current_user.id).all():
    # #     stripe_product = stripe.Product.retrieve(item.product_id)
    # #     product_dict = {
    # #         'price': stripe.Price.retrieve(stripe_product['metadata']['price']),
    # #         'quantity': item.quantity
    # #     }
    # #     items.append(product_dict)
    # # try:
    # #     session = stripe.checkout.Session.create(
    # #         line_items=items,
    # #         mode='payment',
    # #         success_url='http://localhost:3000/shop',
    # #         cancel_url='http://localhost:3000/shop/cart',
    # #     )
    # # except Exception as error:
    # #     return error

    # # # After successful payment, clear items from cart
    # # [db.session.delete(item) for item in Cart.query.filter_by(user_id=current_user.id).all()]
    # # db.session.commit()

    # return redirect(session.url, code=303)
    return ''