import pytest

ORDERS = [(f"ORD-{i:05d}", i % 7 + 1, 250 + (i % 40) * 25) for i in range(5000)]


def order_total(orders):
    lines = [[order_id, qty, price, qty * price] for order_id, qty, price in orders]
    lines = sorted(lines, key=lambda line: line[0])
    amounts = [line[3] for line in lines]
    return sum(amounts)


def find_order(orders, order_id):
    for order in orders:
        if order[0] == order_id:
            return order
    return None


def count_bulk_orders(orders):
    return sum(1 for _, qty, _ in orders if qty >= 5)


@pytest.mark.benchmark
def test_order_total():
    assert order_total(ORDERS) == 14744750


@pytest.mark.benchmark
def test_find_order():
    assert find_order(ORDERS, "ORD-04999") is not None


@pytest.mark.benchmark
def test_count_bulk_orders():
    assert count_bulk_orders(ORDERS) == 2142
