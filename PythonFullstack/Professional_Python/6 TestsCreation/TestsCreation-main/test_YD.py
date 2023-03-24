import unittest
import YD


class TestYD(unittest.TestCase):

    def test_success_create_folder(self):
        self.assertEqual(YD.create_folder('test'), 201)
  
    @unittest.expectedFailure 
    def test_create_folder(self):
        self.assertEqual(YD.create_folder('test'), 401)

if __name__ == '__main__':
    unittest.main()