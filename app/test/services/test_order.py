import pytest


def test_create_order_service(create_order):
    single_order = create_order.json
    pytest.assume(create_order.status.startswith('200'))
    pytest.assume(single_order['_id'])
    pytest.assume(single_order['client_name'])
    pytest.assume(single_order['client_dni'])
    pytest.assume(single_order['client_address'])
    pytest.assume(single_order['client_phone'])
    pytest.assume(single_order['date'])
    pytest.assume(single_order['total_price'])
    pytest.assume(single_order['size'])


def test_get_order_by_id_service(client, create_order, order_uri):
    current_order = create_order.json
    response = client.get(f'{order_uri}id/{current_order["_id"]}')
    pytest.assume(response.status.startswith('200'))
    returned_size = response.json
    for param, value in current_order.items():
        pytest.assume(returned_size[param] == value)


def test_get_orders_service(client, create_orders, order_uri):
    response = client.get(order_uri)
    pytest.assume(response.status.startswith('200'))
    returned_orders = {order['_id']: order for order in response.json}
    for order in create_orders:
        pytest.assume(order.json['_id'] in returned_orders)
