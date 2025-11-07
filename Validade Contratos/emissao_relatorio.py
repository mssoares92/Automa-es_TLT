# --- Arquivo: emissao_relatorio.py ---

import time
import os
import pyautogui
import logging

# Configuração básica do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Configurações do Relatório ---

# Caminho para a pasta com seus "prints"
BASE_IMAGENS = os.path.join(os.path.dirname(__file__), 'imagens_rpa')

# --- Fim das Configurações ---

def find_and_click(image_name, confidence=0.9, wait_time=10):
    """
    Função auxiliar para encontrar uma imagem na tela e clicar nela.
    Tenta por 'wait_time' segundos antes de desistir.
    """
    image_path = os.path.join(BASE_IMAGENS, image_name)
    if not os.path.exists(image_path):
        logging.error(f"Arquivo de imagem não encontrado: {image_path}")
        return False
        
    logging.info(f"Procurando por '{image_name}' na tela...")
    
    start_time = time.time()
    while time.time() - start_time < wait_time:
        try:
            # Tenta localizar o centro da imagem na tela
            center_location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
            
            if center_location:
                logging.info(f"Imagem '{image_name}' encontrada em {center_location}. Clicando...")
                pyautogui.click(center_location)
                return True
        except pyautogui.ImageNotFoundException:
            pass # Imagem ainda não apareceu, tenta novamente
        
        time.sleep(0.5) # Pausa antes de tentar novamente

    logging.error(f"Imagem '{image_name}' não encontrada após {wait_time} segundos.")
    return False

def generate_report():
    """
    Navega pelo menu principal, executando os 3 primeiros passos
    APENAS com pyautogui (sem focar a janela).
    """
    
    logging.info("\n--- MÓDULO DE RELATÓRIO (Passos 1-3) INICIADO (Modo PyAutoGUI Puro) ---")
    
    try:
        # 1. (REMOVIDO) A ETAPA DE FOCO DO PYWINAUTO FOI RETIRADA.
        
        # Garante que o robô tenha tempo de ver a tela após o login
        logging.info("Aguardando 1 segundo antes de procurar a primeira imagem...")
        time.sleep(3) 

        # 2. CLICAR EM "LOCACAO"
        # O robô procura '1_locacao.png' em QUALQUER LUGAR da tela.
        if not find_and_click('1_locacao.png'):
            return False # Se não achar, para o robô
        time.sleep(3) # Pausa para o próximo item aparecer

        # 3. CLICAR EM "RELATÓRIOS"
        # Procura '2_relatorios.png'
        if not find_and_click('2_relatorios.png'):
            return False
        time.sleep(3) # Pausa para a lista de relatórios carregar

        # 4. CLICAR EM "CONTRATOS" (O item com o checkbox)
        # Procura '3_contratos.png'
        if not find_and_click('3_contratos.png'):
            logging.error("Falha ao clicar em '3_contratos.png'.")
            return False
        time.sleep(3)
        
        # 5. CLICAR NO "BOTÃO RELATORIOS" (Botão na parte inferior da tela)
        # Procura '4_btn_relatorios.png'
        if not find_and_click('4_btn_relatorios.png'):
            logging.error("Falha ao clicar em '4_btn_relatorios.png'.")
            return False
        time.sleep(3)

        # 6. CLICAR EM "TIPO DE RELATÓRIO" (O item com o checkbox STATUS)
        # Procura '6_tipo_relatorio.png'
        if not find_and_click('6_tipo_relatorio.png'):
            logging.error("Falha ao clicar em '6_tipo_relatorio.png'.")
            return False
        time.sleep(3)

        # 7. CLICAR EM "STATUS" (O item com o checkbox STATUS)
        # Procura '7_status.png'
        if not find_and_click('7_status.png'):
            logging.error("Falha ao clicar em '7_status.png'.")
            return False
        time.sleep(3)

         # 8. CLICAR EM "INCLUIDO" (CLIQUE NO ITEM INCLUIDO)
        # Procura '8_incluido.png'
        if not find_and_click('8_incluido.png'):
            logging.error("Falha ao clicar em '8_incluido.png'.")
            return False
        time.sleep(3)

         # 9. CLICAR EM "ADD" (CLIQUE "MAIS" PARA ADICIONAR O FILTRO"")
        # Procura '9_add.png'
        if not find_and_click('9_add.png'):
            logging.error("Falha ao clicar em '9_add.png'.")
            return False
        time.sleep(3)

           # 10. CLICAR EM "GERADO" (CLIQUE NO ITEM GERADO)
        # Procura '10_gerado.png'
        if not find_and_click('10_gerado.png'):
            logging.error("Falha ao clicar em '10_gerado.png'.")
            return False
        time.sleep(3)

          # 11. CLICAR EM "ADD" (CLIQUE "MAIS" PARA ADICIONAR O FILTRO"")
        # Procura '9_add.png'
        if not find_and_click('9_add.png'):
            logging.error("Falha ao clicar em '9_add.png'.")
            return False
        time.sleep(3)

           # 12. CLICAR EM "check" (CLIQUE "check" PARA FINALIZAR"")
        # Procura '9_add.png'
        if not find_and_click('11_check.png'):
            logging.error("Falha ao clicar em '11_check.png'.")
            return False
        time.sleep(3)


        
        
        # --- FIM DOS PASSOS SOLICITADOS ---
        logging.info("Passos 1, 2 e 3 concluídos com sucesso.")
        logging.info("Pronto para os próximos comandos de automação.")
        
        return True # Indica que esta parte foi um sucesso

    except Exception as e:
        logging.error(f"\n--- ERRO CRÍTICO AO GERAR RELATÓRIO ---")
        logging.error(f"Ocorreu um erro inesperado: {e}")
        return False