# The following tests check if a page is accessible
# Tests that are commented out can be enabled once the
# route is setup. Will provide better status checks as
# continues in the app and help catch bugs before merging.


def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200

def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200


def test_api(app, client):
    res = client.get('/api/')
    assert res.status_code == 200


# def test_survey(app, client):
#     res = client.get('/survey/')
#     assert res.status_code == 200


# def test_statistics(app, client):
#     res = client.get('/statistics/')
#     assert res.status_code == 200


# def test_about(app, client):
#     res = client.get('/statistics/')
#     assert res.status_code == 200
