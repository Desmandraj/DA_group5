import unittest
import os
class Testrecon(unittest.TestCase):
    def test(self):
        os.system("C:\\Users\\65887\\desktop\\DA_group5\\DA_group5\\DA_group5\\spiders\\getindexpage.py")

class Testresponse(unittest.TestCase):
    def test(self):
        os.system("C:\\Users\\65887\\desktop\\DA_group5\\DA_group5\\DA_group5\\spiders\\getphotodir.py")

class Testimage(unittest.TestCase):
    def test(self):
        os.system("C:\\Users\\65887\\desktop\\DA_group5\\DA_group5\\DA_group5\\spiders\\getreqchangeheader.py")
if __name__ == '__main__':
    unittest.main()