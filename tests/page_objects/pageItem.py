

class PageItem():

    def __init__(self, my_driver):
        self.driver = my_driver
        self.quantity_box = 'quantity_wanted'
        self.quantity_add = '//*[@id="quantity_wanted_p"]/a[2]/span/i'


    def erase_and_add_quantity(self, quantity):
        self.driver.find_element_by_id(self.quantity_box).clear()
        self.driver.find_element_by_id(self.quantity_box).send_keys(quantity)

    def add_x_more_quantity(self, quantity):
        for x in range(quantity):
            self.driver.find_element_by_xpath(self.quantity_add).click()

    def return_quantity_box_value(self):
        return self.driver.find_element_by_id(self.quantity_box).get_attribute('value')


