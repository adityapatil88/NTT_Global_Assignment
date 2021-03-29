import unittest
from server import app


class InterfaceTestCase(unittest.TestCase):

    def test_multiple(self):
        tester = app.test_client(self)
        response = tester.get("/Interface")
        print(response.data)
        status = response.status_code
        self.assertEqual(status, 200)

    def test_single(self):
        tester = app.test_client(self)
        response = tester.get("/Interface?interface=FastEthernet0/0")
        status = response.status_code
        print(response.data)
        self.assertEqual(status, 200)


if __name__ == '__main__':
    unittest.main()
