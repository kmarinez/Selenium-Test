import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    """ Configura WebDriver antes de la prueba y lo cierra al final. """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_fail(driver):
    """ Prueba de inicio de sesión fallida con credenciales incorrectas. """
    driver.get("https://the-internet.herokuapp.com/login")

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")

    username.send_keys("usuario_incorrecto")
    password.send_keys("clave_incorrecta")

    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    wait = WebDriverWait(driver, 30)
    error_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.error")))

    assert "Your username is invalid!" in error_message.text

    print("❌ Prueba de inicio de sesión fallida correctamente.")