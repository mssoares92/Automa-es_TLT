# --- Arquivo: login_ilux.py ---

import time

# --- Configurações de Login ---
LOGIN_WINDOW_TITLE = "ILUX Empresarial" 
LOGIN = "ti"
PASSWORD = "123456"
# --- Fim das Configurações ---

def run_login_automation(app):
    """
    Executa o processo de automação de login no ILUX.
    Recebe a instância 'app' que foi iniciada pelo main.py
    """
    
    print(f"Aguardando a janela de login com o título: '{LOGIN_WINDOW_TITLE}'...")
    try:
        # 3. Aguardar e Conectar à Janela de Login
        dlg = app.window(title=LOGIN_WINDOW_TITLE)
        dlg.wait('visible', timeout=30)
        print("Janela de login encontrada!")

        # 4. Preencher Login, Senha e Pressionar Enter
        dlg.set_focus()
        
        # Sua pausa de 10s
        time.sleep(10) 

        print(f"Preenchendo login: {LOGIN}")
        dlg.type_keys(LOGIN)

        print("Pressionando TAB...")
        dlg.type_keys("{TAB}")
        
        time.sleep(0.5) # Pausa entre os campos

        print("Preenchendo senha...")
        dlg.type_keys(PASSWORD)

        print("Pressionando ENTER (x2)...")
        dlg.type_keys("{ENTER}")
        dlg.type_keys("{ENTER}")
        
        print("\nLogin enviado com sucesso!")
        
        # Sua pausa de 5s
        print("Aguardando 5 segundos para a tela principal carregar...")
        time.sleep(5) 
        
        return True # Retorna True para indicar sucesso no login

    except Exception as e:
        print(f"\n--- ERRO NA AUTOMAÇÃO DE LOGIN ---")
        print(f"Não foi possível interagir com a janela '{LOGIN_WINDOW_TITLE}'.")
        print(f"Verifique o título. Detalhe: {e}")
        return False # Retorna False para indicar falha