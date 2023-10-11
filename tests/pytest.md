# How to write tests with Pytest
### Why write tests?
- By writing tests you can increase stability and catch errors before they are ever merged. This helps reduce down time and catches bugs before they are a problem.

### What is Pytest?
- [Pytest](https://docs.pytest.org/en/latest/index.html) is a unity testing framework for python. It allows us to make small readable tests for various functionality in python applications

### Getting started
- Before writing tests be sure you are able to run the tests first. Assuming you are already in your `pipenv shell` simple run `python -m pytest`
- To write a test create a new file in the tests directory with the extension of _test.py(Ex: home_test.py).  
- Create functions like in the example below that can assert what you would expect. The simplest test for a route would be to assert the correct status code like in the example below. You can find a list of status codes [here](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes).
```
    def test_index(app, client):
        res = client.get('/') # gets the route route.
        assert res.status_code == 200 # expects a status of 200
```

For more detailed information about Pytest visit the [official docs](https://docs.pytest.org/en/latest/index.html) or for a short tutorial click [here](https://dev.to/po5i/how-to-add-basic-unit-test-to-a-python-flask-app-using-pytest-1m7a). 