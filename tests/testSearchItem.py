import unittest
from selenium import webdriver
import time
from tests.page_objects.pageIndex import PageIndex
from tests.page_objects.pageItems import PageItems
from tests.page_objects.pageItem import PageItem
from selenium.webdriver.chrome.options import Options


class SearchCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print ("Creando nuestra base de datos")
        print ("Base de datos creada")

    @classmethod
    def tearDownClass(cls):
        print ("Eliminando BD")
        print ("BD Eliminada")

    def setUp(self):
        option = Options()
        # option.add_argument("start-maximized")
        option.add_argument("incognito")
        # option.add_argument("headless")
        self.driver = webdriver.Chrome('C:/Users/julep/PycharmProjects/TiendaDeRopa/tests/drivers/Chromedriver.exe', options=option)

        # self.driver.set_window_position(-1000, 0)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)
        # self.driver.maximize_window()
        # self.driver.set_window_size(800,600)
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)
        self.itemPage = PageItem(self.driver)

    @unittest.skip("Not needed now")
    def test_search_no_elements(self):
        try:
            self.indexPage.search('hola')
            self.assertEqual(self.itemsPage.return_no_element_text(), 'No results were found for your search "pepe"')
        except:
            self.driver.save_screenshot('error.png')

    @unittest.skip("Not needed now")
    def test_search_find_dresses(self):
        self.indexPage.search('dress')
        self.assertTrue('DRESS' in self.itemsPage.return_section_title())

    # @unittest.skip("Not needed now")
    def test_search_find_tshirts(self):
        self.indexPage.search('t-shirts')
        self.assertTrue('T-SHIRTS' in self.itemsPage.return_section_title())

    @unittest.skip("Not needed now")
    def test_meter_ropa_en_el_carrito(self):
        self.indexPage.search('t-shirts')
        self.itemsPage.click_orange_button()
        self.itemPage.erase_and_add_quantity('25')
        self.itemPage.add_x_more_quantity(3)
        self.assertEqual(self.itemPage.return_quantity_box_value(), '28')


    def test_selections(self):
        self.indexPage.search('t-shirts')
        self.itemsPage.select_by_text('Product Name: A to Z')
        self.itemsPage.select_by_value('reference:asc')
        self.itemsPage.select_by_index(3)
        time.sleep(3)

    @unittest.skip("Not needed now")
    def test_dresses_options(self):
        self.indexPage.click_dresses()
        self.itemsPage.click_checkbox(2)
        self.itemsPage.click_checkbox(4)
        self.itemsPage.click_colors(2)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()