import unittest
import math
from easymsgbox import alert


class MultiplicationTestCase(unittest.TestCase):

    def setUp(self):
        self.title = 'Test title'
        self.text = 'Test text'

    def test_alert_basic(self):
        result = alert(self.title, self.text)
        self.assertEqual(result, None)
    
    def test_alert_error(self):
        result = alert(self.title, self.text, icon='error')
        self.assertEqual(result, None)
    
    def test_alert_question(self):
        result = alert(self.title, self.text, icon='question')
        self.assertEqual(result, None)
    
    def test_alert_warning(self):
        result = alert(self.title, self.text, icon='warning')
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()