import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestMensagemErro(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Configura o WebDriver e abre o navegador."""
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://practice.automationtesting.in/")  # URL do site
        cls.driver.implicitly_wait(10)

    def acessar_menu_conta(self):
        """Método auxiliar para acessar o menu 'Minha Conta'."""
        my_account_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))
        )
        my_account_menu.click()

    def preencher_campos_e_clicar(self, email, senha, acao="login"):
        """Método auxiliar para preencher os campos de login/registro e clicar no botão."""
        if acao == "login":
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_field.send_keys(email)
            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys(senha)
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "login"))
            )
        elif acao == "register":
            email_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "reg_email"))
            )
            email_field.send_keys(email)
            password_field = self.driver.find_element(By.ID, "reg_password")
            password_field.send_keys(senha)
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "register"))
            )

        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.driver.execute_script("arguments[0].click();", button)

    def verificar_mensagem_erro(self, mensagem_esperada):
        """Método auxiliar para verificar a mensagem de erro exibida."""
        error_message = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "ul.woocommerce-error li"))
        )
        self.assertIn(mensagem_esperada, error_message.text,
                      f"A mensagem de erro não foi exibida ou está incorreta. Mensagem: {error_message.text}")
        print(f"Mensagem de erro exibida corretamente: {error_message.text}")

    def test_mensagem_erro_login_incorreto(self):
        """Verificar mensagem de erro ao tentar login com dados incorretos."""
        self.acessar_menu_conta()
        self.preencher_campos_e_clicar(" ", "senha_incorreta")
        self.verificar_mensagem_erro("Error: Username is required.")

    def test_mensagem_erro_username_vazio(self):
        """Verificar mensagem de erro ao tentar login com nome de usuário vazio."""
        self.acessar_menu_conta()
        self.preencher_campos_e_clicar("", "senhaSegura123")
        self.verificar_mensagem_erro("Error: Username is required.")

    def test_mensagem_erro_email_vazio(self):
        """Verificar mensagem de erro ao tentar registrar com e-mail vazio."""
        self.acessar_menu_conta()
        self.preencher_campos_e_clicar("", "senhaSegura123", acao="register")
        self.verificar_mensagem_erro(
            "Error: Please provide a valid email address.")

    def test_mensagem_erro_senha_vazia(self):
        """Verificar mensagem de erro ao tentar registrar com senha vazia."""
        self.acessar_menu_conta()
        self.preencher_campos_e_clicar(
            "valid.email@example.com", "", acao="register")
        self.verificar_mensagem_erro(
            "Error: Please enter an account password.")

    def test_mensagem_erro_email_senha_vazios(self):
        """Verificar mensagem de erro ao tentar registrar com e-mail e senha vazios."""
        self.acessar_menu_conta()
        self.preencher_campos_e_clicar("", "", acao="register")
        self.verificar_mensagem_erro(
            "Error: Please provide a valid email address.")

    @classmethod
    def tearDownClass(cls):
        """Fecha o navegador após os testes."""
        print("Fechando o navegador...")
        time.sleep(5)
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(argv=['', 'TestMensagemErro'], exit=False)
