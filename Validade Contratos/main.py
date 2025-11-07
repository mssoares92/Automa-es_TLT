# --- Arquivo: main.py ---

import os
import time
from pywinauto.application import Application

# Importa as FUNÇÕES dos outros arquivos
from login_ilux import run_login_automation
from emissao_relatorio import generate_report

# --- Configurações Globais ---
ILUX_PROCESS_NAME = "ILUXEmpresarial.exe"
ILUX_PATH = r"C:\ILUX\ILUXEmpresarial.exe"
# --- Fim das Configurações ---


# --- Ponto de Partida ---
if __name__ == "__main__":
    
    # === AVISO DE SEGURANÇA ===
    print("="*40)
    print("ATENÇÃO: A senha está visível no arquivo 'login_ilux.py'.")
    print("Considere usar variáveis de ambiente ou 'dotenv' \npara um projeto em produção.")
    print("="*40 + "\n")
    
    # 1. Fechar processos antigos
    print(f"Fechando instâncias anteriores de '{ILUX_PROCESS_NAME}'...")
    os.system(f'taskkill /F /IM {ILUX_PROCESS_NAME} 2> nul')
    time.sleep(3) # Dá um tempo para os processos morrerem

    # 2. Iniciar o App
    app = None
    try:
        print(f"Iniciando {ILUX_PATH}...")
        # 'backend="uia"' é o mais moderno e recomendado para apps Windows
        app = Application(backend="uia").start(ILUX_PATH)
    except Exception as e:
        print(f"ERRO CRÍTICO: Não foi possível iniciar o executável em '{ILUX_PATH}'.")
        print(f"Verifique o caminho. Detalhe: {e}")
        exit() # Sai do script se não puder iniciar

    # 3. Rodar Login
    # Passamos o objeto 'app' para a função de login
    print("--- MÓDULO DE LOGIN INICIADO ---")
    if run_login_automation(app):
        
        # 4. Se o login deu certo (retornou True), gerar o relatório
        # Reutilizamos o MESMO objeto 'app'
        generate_report()

    else:
        print("Ocorreu um erro no login. O robô não continuará.")

    # 5. (Opcional) Fechar o ILUX no final
    # print("Fechando o ILUX...")
    # app.kill()

    print("\n--- Automação principal finalizada ---")