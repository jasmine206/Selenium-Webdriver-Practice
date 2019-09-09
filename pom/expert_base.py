from driver_api import DriverAPI


class ExpertBase:
    def __init__(self, driver):
        self.driver = DriverAPI(driver)
