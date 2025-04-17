import os
import sys
import subprocess
import shutil

def create_executable():
    """Cria um executável usando PyInstaller"""
    
    # Verificar e instalar dependências
    dependencies = ['flask', 'PyPDF2', 'reportlab', 'pikepdf', 'werkzeug', 'pyinstaller']
    
    for dep in dependencies:
        try:
            __import__(dep)
        except ImportError:
            print(f"Instalando {dep}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
    
    # Criar estrutura de diretórios
    os.makedirs('templates', exist_ok=True)
    
    # Configuração do PyInstaller
    pyinstaller_cmd = [
        'pyinstaller',
        '--name=PDFtoPDFA_Converter',
        '--onefile',
        '--windowed',
        '--add-data=templates;templates',
        '--icon=icon.ico',  # Opcional
        'app.py'
    ]
    
    # Executar
    print("Criando executável...")
    subprocess.check_call(pyinstaller_cmd)
    print("\nExecutável criado na pasta 'dist'")

if __name__ == "__main__":
    create_executable()