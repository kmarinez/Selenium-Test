from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar WebDriver
driver = webdriver.Chrome()

# Abrir la página del dropdown
driver.get("https://the-internet.herokuapp.com/dropdown")

# Esperar hasta que el dropdown esté visible
wait = WebDriverWait(driver, 30)
dropdown_element = wait.until(EC.visibility_of_element_located((By.ID, "dropdown")))

# Seleccionar la opción "Option 2"
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Option 1")

# Verificar que la opción seleccionada es correcta
selected_option = dropdown.first_selected_option.text
assert selected_option == "Option 1"

print("✅ Prueba de selección en dropdown completada correctamente.")

# Cerrar navegador
input("Presiona ENTER para cerrar el navegador...")
driver.quit()
