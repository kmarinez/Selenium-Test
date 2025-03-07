from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar WebDriver
driver = webdriver.Chrome()

# Abrir la página de inicio de sesión
driver.get("https://the-internet.herokuapp.com/login")

# Encontrar los campos de usuario y contraseña
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

# Ingresar credenciales incorrectas
username.send_keys("usuario_incorrecto")
password.send_keys("clave_incorrecta")

# Hacer clic en el botón de Login
login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()

# Esperar hasta que aparezca el mensaje de error
wait = WebDriverWait(driver, 30)
error_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.error")))

# Verificar que el mensaje de error es correcto
assert "Your username is invalid!" in error_message.text

print("❌ Prueba de inicio de sesión fallida correctamente.")

# Cerrar navegador
input("Presiona ENTER para cerrar el navegador...")
driver.quit()