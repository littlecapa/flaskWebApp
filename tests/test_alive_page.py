import unittest

import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        print("Start")

    def test_alive_page(self):

        response = app.test_client().get("/alive")
        assert response.status_code == 200
        assert b"About This App" in response.data
    
    def test_fail(self):
        assert 1 == 2
    

if __name__ == "__main__":
    unittest.main()