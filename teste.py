# Importando as bibliotecas necessárias

# Importa a classe para controle do navegador
from selenium import webdriver  
# Importa o gerenciador de driver para o Chrome
from webdriver_manager.chrome import ChromeDriverManager  
# Importa o serviço do Chrome
from selenium.webdriver.chrome.service import Service  
# Importa as opções de configuração do Chrome
from selenium.webdriver.chrome.options import Options  
# Importa o módulo para seleção de elementos por critério
from selenium.webdriver.common.by import By  
# Importa o módulo para interagir com o sistema operacional
import os  
# Importa o módulo para adicionar pausas/tempo
import time  
# Configuração do serviço do ChromeDriver
servico = Service(ChromeDriverManager().install())

# Opções do Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Inicializa o navegador
navegador = webdriver.Chrome(service=servico, options=chrome_options)

# Obtém o caminho absoluto do diretório do script Python
diretorio_script = os.path.dirname(os.path.abspath(__file__))

# Monta o caminho absoluto para o arquivo HTML
caminho_absoluto = os.path.join(diretorio_script, "teste.html")

# Navega até o arquivo HTML local
navegador.get(f"file://{caminho_absoluto}")

# Aguarda 5 segundos antes de continuar
time.sleep(5)

# Encontra os elementos de input de login e senha
campo_login = navegador.find_element(By.NAME, "username")
campo_senha = navegador.find_element(By.NAME, "password")

# Preenche os campos de login e senha
campo_login.send_keys("rafael")
campo_senha.send_keys("123")

# Encontra o botão de login usando o XPath
botao_login = navegador.find_element(By.XPATH, "//*[@id='loginForm']/button")

# Clica no botão de login
botao_login.click()

# Aguarda 5 segundos antes de continuar
time.sleep(5)

# Encontra os elementos de input de nome, sobrenome e idade
campo_nome = navegador.find_element(By.ID, "nome")
campo_sobrenome = navegador.find_element(By.ID, "sobrenome")
campo_idade = navegador.find_element(By.ID, "idade")

# Preenche os campos de nome, sobrenome e idade
campo_nome.send_keys("Rafael")
campo_sobrenome.send_keys("Sales")
campo_idade.send_keys("33")

# Encontra o botão de envio usando o XPath
botao_enviar = navegador.find_element(By.XPATH, '//button[@type="submit" and @class="btn btn-primary"]')

# Clica no botão para enviar o formulário
botao_enviar.click()

# Aguarda alguns segundos para observar o resultado
time.sleep(5)

# Fecha o navegador
navegador.quit()
