from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def main():
    # Configura el navegador Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Navega a la página de Amazon
    driver.get("https://www.amazon.com/")
    
    
    # Extrae el HTML de la página
    html_content = driver.page_source
    
    # Cierra el navegador
    driver.quit()
    
    # Analiza el HTML con BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Encuentra los elementos que contienen la información de teléfonos
    phone_elements = soup.find_all('div', {'class': 'a-section a-spacing-none'})
    
    # Extrae la información de los teléfonos
    phone_info = [element.get_text() for element in phone_elements]
    
    print(phone_info)

if __name__ == "__main__":
    main()
