from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()

pedidos = navegador.find_elements(By.CSS_SELECTOR, 'href="#/orders/')