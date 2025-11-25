#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import hashlib
import qrcode
from io import BytesIO
import base64

# Lista de nomes e IDs anónimos
formandos = [
    {"id": "001", "nome": "Artur Mesquita"},
    {"id": "002", "nome": "Beatriz Duarte"},
    {"id": "003", "nome": "Beatriz Peralta"},
    {"id": "004", "nome": "Clara Pinto"},
    {"id": "005", "nome": "Clara Tomé"},
    {"id": "006", "nome": "Davi Silva"},
    {"id": "007", "nome": "David Lages"},
    {"id": "008", "nome": "Diogo Marques"},
    {"id": "009", "nome": "Francisco Vizinho"},
    {"id": "010", "nome": "Gabriel Marreiros"},
    {"id": "011", "nome": "Gonçalo Polónia"},
    {"id": "012", "nome": "Íris Rodrigues"},
    {"id": "013", "nome": "Joana Silva"},
    {"id": "014", "nome": "João Maciel"},
    {"id": "015", "nome": "Leonor Martins"},
    {"id": "016", "nome": "Leonor Garcia"},
    {"id": "017", "nome": "Magda Cerqueira"},
    {"id": "018", "nome": "Margarida Lemos"},
    {"id": "019", "nome": "Margarida Martins"},
    {"id": "020", "nome": "Maria Carolina Costa"},
    {"id": "021", "nome": "Maria Francisca Martins"},
    {"id": "022", "nome": "Matias Leite"},
    {"id": "023", "nome": "Matilde Colaço"},
    {"id": "024", "nome": "Pilar Cerqueira"},
    {"id": "025", "nome": "Safira Canelas"},
    {"id": "026", "nome": "Simão Morgado"},
    {"id": "027", "nome": "Sofia Reis"}
]

# URL base do Vercel
BASE_URL = "https://202511-junior-ai.vercel.app"

# Template HTML do certificado
template_html = '''<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Certificado de Especialista IA Júnior</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Montserrat:wght@300;400;600&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Montserrat', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        
        .certificate-container {
            width: 297mm;
            height: 210mm;
            background: white;
            box-shadow: 0 10px 50px rgba(0, 0, 0, 0.3);
            position: relative;
            overflow: hidden;
        }
        
        .certificate-border {
            position: absolute;
            top: 15mm;
            left: 15mm;
            right: 15mm;
            bottom: 15mm;
            border: 3px solid #2c3e50;
            border-radius: 10px;
        }
        
        .certificate-inner-border {
            position: absolute;
            top: 20mm;
            left: 20mm;
            right: 25mm;
            bottom: 20mm;
            border: 1px solid #95a5a6;
            border-radius: 8px;
        }
        
        .decorative-corner {
            position: absolute;
            width: 40px;
            height: 40px;
        }
        
        .corner-tl {
            top: 18mm;
            left: 18mm;
            border-top: 3px solid #e74c3c;
            border-left: 3px solid #e74c3c;
            border-radius: 8px 0 0 0;
        }
        
        .corner-tr {
            top: 18mm;
            right: 18mm;
            border-top: 3px solid #e74c3c;
            border-right: 3px solid #e74c3c;
            border-radius: 0 8px 0 0;
        }
        
        .corner-bl {
            bottom: 18mm;
            left: 18mm;
            border-bottom: 3px solid #e74c3c;
            border-left: 3px solid #e74c3c;
            border-radius: 0 0 0 8px;
        }
        
        .corner-br {
            bottom: 18mm;
            right: 18mm;
            border-bottom: 3px solid #e74c3c;
            border-right: 3px solid #e74c3c;
            border-radius: 0 0 8px 0;
        }
        
        .certificate-content {
            position: relative;
            z-index: 10;
            text-align: center;
            padding: 35mm 30mm;
        }
        
        .trophy {
            font-size: 48px;
            margin-bottom: 15px;
            display: block;
        }
        
        .certificate-title {
            font-family: 'Playfair Display', serif;
            font-size: 32px;
            font-weight: 700;
            color: #2c3e50;
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 3px;
        }
        
        .certificate-subtitle {
            font-family: 'Playfair Display', serif;
            font-size: 42px;
            font-weight: 700;
            color: #e74c3c;
            margin-bottom: 25px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        
        .awarded-to {
            font-size: 18px;
            color: #7f8c8d;
            margin-bottom: 20px;
            font-weight: 300;
            font-style: italic;
        }
        
        .recipient-name {
            font-size: 32px;
            font-weight: 600;
            color: #2c3e50;
            border-bottom: 2px solid #34495e;
            padding-bottom: 10px;
            margin: 0 auto 30px;
            width: 60%;
            min-height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .certificate-text {
            font-size: 16px;
            color: #34495e;
            line-height: 1.8;
            margin-bottom: 15px;
            font-weight: 400;
        }
        
        .course-name {
            font-weight: 600;
            color: #2c3e50;
            font-size: 18px;
        }
        
        .date-container {
            margin-top: 30px;
            font-size: 16px;
            color: #7f8c8d;
        }

        .signatures-container {
            margin-top: 45px;
            display: flex;
            justify-content: center;
            gap: 120px;
        }
        
        .signature {
            text-align: center;
        }
        
        .signature-line {
            width: 250px;
            border-top: 2px solid #2c3e50;
            margin-bottom: 8px;
        }
        
        .signature-name {
            font-size: 15px;
            color: #2c3e50;
            font-weight: 600;
        }
        
        .signature-title {
            font-size: 12px;
            color: #7f8c8d;
            font-weight: 300;
            margin-top: 3px;
        }
        
        
        .watermark {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(-45deg);
            font-size: 120px;
            color: rgba(231, 76, 60, 0.03);
            font-weight: 700;
            z-index: 1;
            pointer-events: none;
        }
        
        .qr-code-container {
            position: absolute;
            bottom: 28mm;
            right: 25mm;
            text-align: center;
            z-index: 20;
            background: white;
            padding: 8px;
            border-radius: 8px;
            border: 2px solid #e0e0e0;
        }
        
        .qr-code-container img {
            display: block;
            width: 80px;
            height: 80px;
        }
        
        .qr-code-text {
            font-size: 8px;
            color: #7f8c8d;
            margin-top: 4px;
            font-weight: 600;
        }
        
        .certificate-id {
            position: absolute;
            bottom: 20mm;
            left: 20mm;
            font-size: 10px;
            color: #95a5a6;
            font-weight: 600;
            z-index: 20;
        }
        
        @media print {
            body {
                background: white;
                padding: 0;
            }
            
            .certificate-container {
                box-shadow: none;
                width: 297mm;
                height: 210mm;
                page-break-after: avoid;
            }
            
            .qr-code-container,
            .certificate-id {
                display: block !important;
            }
            
            @page {
                size: A4 landscape;
                margin: 0;
            }
        }
    </style>
</head>
<body>
    <div class="certificate-container">
        <div class="watermark">IA</div>
        <div class="certificate-border"></div>
        <div class="certificate-inner-border"></div>
        <div class="decorative-corner corner-tl"></div>
        <div class="decorative-corner corner-tr"></div>
        <div class="decorative-corner corner-bl"></div>
        <div class="decorative-corner corner-br"></div>
        
        <div class="certificate-content">
            <span class="trophy">🏆</span>
            <h1 class="certificate-title">Certificado de Especialista</h1>
            <h2 class="certificate-subtitle">IA Júnior</h2>
            
            <p class="awarded-to">Conferido a:</p>
            
            <div class="recipient-name">
                {{NOME_FORMANDO}}
            </div>
            
            <p class="certificate-text">Por completar com sucesso</p>
            <p class="course-name">a formação "IA e Bibliotecas"</p>
            
            <div class="date-container">
                <p style="margin-bottom: 8px;">Escola Básica António Dias Simões - Ovar</p>
                <p>Data: 26 de novembro de 2025</p>
            </div>
            
            
            <div class="signatures-container">
                <div class="signature">
                    <div class="signature-line"></div>
                    <div class="signature-name">Prof. Ana Bessa</div>
                    <div class="signature-title">Docente</div>
                </div>
                <div class="signature">
                    <div class="signature-line"></div>
                    <div class="signature-name">Prof. Daniel Polónia</div>
                    <div class="signature-title">Docente</div>
                </div>
            </div>
        
        <div class="qr-code-container">
            <img src="{{QR_CODE_DATA}}" alt="QR Code">
            <div class="qr-code-text">Verificar online</div>
        </div>
        
        <div class="certificate-id">
            Certificado #{{CERT_ID}}
        </div>
    </div>
</body>
</html>'''

# Criar diretório de saída
output_dir = '.'
os.makedirs(output_dir, exist_ok=True)

# Gerar certificados
certificados_gerados = []

for formando in formandos:
    cert_id = formando['id']
    nome = formando['nome']
    
    # Nome do ficheiro anónimo
    nome_ficheiro = f"certificado_{cert_id}.html"
    
    # URL do certificado
    url_certificado = f"{BASE_URL}/{nome_ficheiro}"
    
    # Gerar QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(url_certificado)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Converter imagem para base64
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    img_str = base64.b64encode(buffer.getvalue()).decode()
    qr_code_data = f"data:image/png;base64,{img_str}"
    
    # Criar HTML personalizado
    html_content = template_html.replace('{{NOME_FORMANDO}}', nome)
    html_content = html_content.replace('{{QR_CODE_DATA}}', qr_code_data)
    html_content = html_content.replace('{{CERT_ID}}', cert_id)
    
    # Salvar ficheiro
    caminho_completo = os.path.join(output_dir, nome_ficheiro)
    with open(caminho_completo, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    certificados_gerados.append({
        'id': cert_id,
        'nome': nome,
        'ficheiro': nome_ficheiro,
        'url': url_certificado
    })
    
    print(f"✓ Certificado criado: {nome_ficheiro} ({nome})")

# Salvar mapeamento (apenas para referência interna - não deploy)
mapeamento = {
    'base_url': BASE_URL,
    'data_geracao': '2025-11-25',
    'formacao': 'IA e Bibliotecas',
    'instituicao': 'Escola Básica António Dias Simões - Ovar',
    'certificados': certificados_gerados
}

with open(os.path.join(output_dir, 'mapeamento_privado.json'), 'w', encoding='utf-8') as f:
    json.dump(mapeamento, f, ensure_ascii=False, indent=2)

print(f"\n✓ Total de {len(formandos)} certificados criados com IDs anónimos!")
print(f"✓ QR codes gerados e incorporados!")
print(f"✓ Mapeamento salvo em mapeamento_privado.json (NÃO fazer deploy deste ficheiro!)")
