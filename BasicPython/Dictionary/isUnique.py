import unittest
def unique(str):
    charSet = {}
    for char in str:
        if char in charSet:
            return False
        charSet[char] = True
    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s432fad'), ('')]
    dataF = [('232ds2'), ('hb asdfsfsss')]

    def tesUnique(self):
        #true check
        for testCase in self.dataT:
            actualResult = unique(testCase)
            self.assertTrue(actualResult)
if __name__ == "__main__":
    str = "abc"
    print(unique(str))
    unittest.main()