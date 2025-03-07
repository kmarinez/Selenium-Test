import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    """ Configura WebDriver antes de la prueba y lo cierra al final. """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_dropdown_selection(driver):
    """ Prueba de selección de una opción en el menú desplegable. """
    driver.get("https://the-internet.herokuapp.com/dropdown")

    wait = WebDriverWait(driver, 30)
    dropdown_element = wait.until(EC.visibility_of_element_located((By.ID, "dropdown")))

    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text("Option 2")

    selected_option = dropdown.first_selected_option.text
    assert selected_option == "Option 2"

    print("✅ Prueba de selección en dropdown completada correctamente.")