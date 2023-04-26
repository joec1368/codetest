import unittest

# Question A
def reverseString(string) -> str:
  return string[::-1]

# Question B
def reverseSetence(string) -> str:
  answer = ""
  for i in string.split( ):
    answer = answer +  " " +reverseString(i) 
  return answer[1:]

class Test(unittest.TestCase):

    def testReverseString(self):
        expected = "fdsa";
        result = reverseString("asdf");
        self.assertEqual(expected, result);

    def testReverseSentence(self):
        expected = "aadd qwer";
        result = reverseSetence("ddaa rewq");
        self.assertEqual(expected, result);
        
if __name__=='__main__':
    unittest.main()