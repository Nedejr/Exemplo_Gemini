from dotenv import load_dotenv
import google.generativeai as genai
import os
from PIL import Image
import cv2


load_dotenv()
API_KEY = os.getenv('API_KEY')
genai.configure(api_key=API_KEY)

def main():
    lista_opcoes = [
        {'id': 1, 'acao': 'Bate-Papo'},
        {'id': 2, 'acao': 'Descrever Imagem'},
        {'id': 3, 'acao': 'Sair'}
    ]

    print(f"\nDigite a opção:\n")
    for op in lista_opcoes:
        print(f'Digite {op['id']} para {op['acao']}')

    opcao = input(f"\nDigite a opção: ")    

    if (opcao == '1'):
        modelo = 'gemini-pro'
        conversar_com_modelo(modelo)
    if opcao == '2':
        modelo = 'gemini-1.5-flash'
        conversar_com_modelo(modelo)
    if (opcao == '3'):
        print('Bye Bye!')
    

def conversar_com_modelo(modelo):
    model = genai.GenerativeModel(modelo)
    
    if modelo == 'gemini-pro':
        print(f"\nBem-vindo ao Gemini! Usando o modelo: {modelo}")
        print("Digite 'sair' para encerrar a conversa.")
        while True:
            prompt = input("\nVocê: ")  
            if prompt.lower() == 'sair':
                print("Obrigado por conversar comigo. Até a próxima!")
                break
             
            response = model.generate_content(prompt)
            print(response.text)
    
    if modelo == 'gemini-1.5-flash':
        while True:
            nome_imagem = input('\nInforme o nome do arquivo da imagem ou "sair" para encerrar: ')
            caminho_imagem = f'images/{nome_imagem}.jpg'
            if nome_imagem.lower() == 'sair':
                print("Obrigado por conversar comigo. Até a próxima!")
                break
            try:
                
                img_file = Image.open(caminho_imagem)
                response = model.generate_content(['Descreva esta imagem com uma mensagem: ', img_file])
                print(f'\n\n{response.text}')
                foto = cv2.imread(caminho_imagem) 
                cv2.imshow('Image', foto)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                
                
            except FileNotFoundError as error:
                print('Arquivo não encontrado!')


if __name__ == "__main__":
   main()
