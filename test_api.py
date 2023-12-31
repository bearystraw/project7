#Group 10 worked together to work on this project

import pytest
import requests

BASE_URL = 'http://localhost:8000'

def test_md5():
    #Test with a valid string
    response = requests.get(f'{BASE_URL}/md5/hello')
    assert response.status_code == 200
    assert response.json()['output'] == '5d41402abc4b2a76b9719d911017c592'

def test_factorial():
    #Test with a valid integer
    response = requests.get(f'{BASE_URL}/factorial/5')
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'
    assert response.json()['output'] == 120

    #Test with a negative integer
    response = requests.get(f'{BASE_URL}/factorial/-5')
    assert response.status_code == 404
    if response.headers['content-type'] == 'application/json':
        print(response.json())

def test_fibonacci():
    #Test with a valid integer
    response = requests.get(f'{BASE_URL}/fibonacci/10')
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'
    assert response.json()['output'] == [0, 1, 1, 2, 3, 5, 8]

    #Test with a negative integer
    response = requests.get(f'{BASE_URL}/fibonacci/-10')
    assert response.status_code == 404
    if response.headers['content-type'] == 'application/json':
        print(response.json())
        
def test_is_prime():
    #Test with a valid integer
    response = requests.get(f'{BASE_URL}/is-prime/7')
    assert response.status_code == 200
    assert response.json()['output'] is True

    #Test with a non-prime integer
    response = requests.get(f'{BASE_URL}/is-prime/4')
    assert response.status_code == 200
    assert response.json()['output'] is False

    #Test with an integer less than 2
    response = requests.get(f'{BASE_URL}/is-prime/1')
    assert response.status_code == 400
    assert response.json()['output'] == "Error: Input must be a positive integer greater than 1."

def test_slack_alert():
    #Test with a valid string
    response = requests.get(f'{BASE_URL}/slack-alert/test')
    assert response.status_code == 200
    assert response.json()['output'] is True

if __name__ == '__main__':
    pytest.main()
