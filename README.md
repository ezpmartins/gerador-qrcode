# Gerador de QR Code em Python <a href="https://skillicons.dev"> <img width="30px" align="right" src="https://skillicons.dev/icons?i=python" /> </a>


Um gerador de QR Code com interface gráfica simples, desenvolvido em Python usando as bibliotecas Tkinter e `qrcode`. Este programa permite ao usuário inserir um link e um nome de arquivo, gerar o QR Code e salvá-lo automaticamente na pasta de downloads do sistema.

## Funcionalidades

- **Interface gráfica** intuitiva com Tkinter.
- **Geração de QR Codes** a partir de links fornecidos pelo usuário.
- **Salvamento automático** do QR Code gerado na pasta de downloads do usuário.

## Pré-requisitos

- Python 3.10 ou superior
- Bibliotecas `qrcode` e `Pillow` (para suporte de imagem no `qrcode`)

Instale as dependências executando:

```bash
pip install qrcode[pil]
