import unittest
import app

class TestDockerapp(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_save_value(self):
        response = self.app.post('/', data=dict(submit='save', key='3', cache_value='three'))
        assert response.status_code == 200
        assert b'3' in response.data
        assert b'three' in response.data

    def test_load_value(self):
        self.app.post('/', data=dict(submit='save', key='3', cache_value='three'))
        response = self.app.post('/', data=dict(submit='load', key='3'))
        assert response.status_code == 200
        assert b'3' in response.data
        assert b'three' in response.data

if __name__=='__main__':
    unittest.main()
