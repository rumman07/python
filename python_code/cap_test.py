from platform import python_branch
import unittest
import cap 

class CapTest(unittest.TestCase):

    def testone(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, "Python")

    def testtwo(self):
        text = "monty python"
        result = cap.cap_text(text)
        self.assertEqual(result,"Monty Python")
        



if __name__ == '__main__':
    unittest.main()