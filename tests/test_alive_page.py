import unittest

class BasicTests(unittest.TestCase):

    def setUp(self):
        print("Start")

    def test_alive_page(self):

        response = self.app.get("/alive")
        assert response.status_code != 200
        assert b"About This App" in response.data

if __name__ == "__main__":
    unittest.main()