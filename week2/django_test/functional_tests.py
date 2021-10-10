
from selenium import webdriver
#import unittest

# Option 1 ---------------------------------------------

browser = webdriver.Opera()
browser.get('http://localhost:8000')

#assert 'Django' in browser.title

#assert 'install' in browser.title

#assert 'To-Do' in browser.title

#assert 'To-Do' in browser.title, "Browser title was " + browser.title

#browser.quit()

# Option 2 ---------------------------------------------

#from selenium import webdriver
#import unittest

#class NewVisitorTest(unittest.TestCase):

    #def setUp(self):
        #self.browser = webdriver.Firefox()
        #self.browser = webdriver.Chrome()

    #def tearDown(self):
        #self.browser.quit()

    #def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        #self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        #self.assertIn('To-Do', self.browser.title)
        #self.assertIn('Congratulations', self.browser.title)
        #self.fail('Finish the test!')

#if __name__ == '__main__':
    #unittest.main(warnings='ignore')