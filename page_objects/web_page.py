from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class AccessWebPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = "https://clikalia.es/"


# Elementos:
# No es correcto utilizar xpath absoluto para pruebas automaticas. Per analizando la página web sería necesario añadir más 
# IDs para en caso de cambios en la pagina web no afectar tanto el funcionamiento de los casos de prueba. Esto afecta la refactrización constante de código y fallos desnecesarios.
        self.reject_cookies = (By.ID, "onetrust-reject-all-handler")
        self.btn_sale = (By.ID, "sale")
        self.input_province = (By.XPATH, "/html/body/main/div/header/div[2]/div[2]/div[2]/div[1]")
        self.select_province = (By.XPATH, "/html/body/main/div/header/div[2]/div[2]/div[2]/div[2]/div/div/button[14]")
        self.btn_found_home = (By.XPATH, "/html/body/main/div/header/div[2]/div[2]/div[2]/div[1]/div/div/button[1]") ## clase = bg-button-primary-surface-default
        self.select_home = (By.XPATH, "/html/body/main/div/div[2]/section/div[1]/a[6]/div/div[2]/div[5]/button[1]/span")
        self.visit_in_person = (By.XPATH, "/html/body/main/form/div/div/div/main/div[2]/div[2]/div[2]/div/div/div[2]")
        self.btn_continue = (By.XPATH, "/html/body/main/form/div/div/div/footer/button/span/span[2]")
        self.select_data = (By.XPATH, "/html/body/main/form/div/div/div/main/div/div[2]/div[1]/div/div/div[2]/div[2]/div/button[8]/div")
        self.select_time = (By.XPATH, "/html/body/main/form/div/div/div/main/div/div[2]/div[2]/div[1]/button[11]")
        self.btn_continue_step2 = (By.XPATH, "/html/body/main/form/div/div/div/footer/button[2]")
        self.input_name = (By.XPATH, "/html/body/main/form/div/div/div/main/div/div[2]/div[1]/div/div[2]/input")
        self.input_lastname = (By.XPATH, "/html/body/main/form/div/div/div/main/div/div[2]/div[2]/div/div[2]/input")


    def open_webpage(self):
             self.driver.get(self.base_url)
             self.wait.until(EC.element_to_be_clickable(self.reject_cookies)).click()

    def search_home(self, province: str):
            self.wait.until(EC.element_to_be_clickable(self.btn_sale)).click()
            time.sleep(7)
            self.wait.until(EC.visibility_of_element_located(self.input_province)).click()
            time.sleep(7)
            #self.wait.until(EC.visibility_of_element_located(self.input_province)).send_keys(province)
            self.wait.until(EC.element_to_be_clickable(self.select_province)).click()
            time.sleep(5)
            self.wait.until(EC.element_to_be_clickable(self.btn_found_home)).click()
            time.sleep(7)

    def select_a_home(self):
            time.sleep(7)
            element = self.wait.until(EC.element_to_be_clickable(self.select_home))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(5)
            self.wait.until(EC.element_to_be_clickable(self.select_home)).click()


    def visit(self, name: str, lastname: str):
            element = self.wait.until(EC.element_to_be_clickable(self.visit_in_person))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(7)
            self.wait.until(EC.element_to_be_clickable(self.visit_in_person)).click()
            time.sleep(7)
            self.wait.until(EC.element_to_be_clickable(self.btn_continue)).click()
            time.sleep(10)
            self.wait.until(EC.element_to_be_clickable(self.select_data)).click()
            self.wait.until(EC.element_to_be_clickable(self.select_time)).click()
            time.sleep(5)
            self.wait.until(EC.element_to_be_clickable(self.btn_continue_step2)).click()
            self.wait.until(EC.visibility_of_element_located(self.input_name)).send_keys(name)
            self.wait.until(EC.visibility_of_element_located(self.input_lastname)).send_keys(lastname)
            time.sleep(4)