# 🚀 GUIA DE SETUP - Repositório GitHub e Vercel

## ⚠️ IMPORTANTE: Começar por Aqui

Este guia irá configurar tudo do zero, incluindo:
1. Criar repositório GitHub
2. Fazer commit inicial
3. Adicionar certificados
4. Configurar Vercel

---

## 📋 PRÉ-REQUISITOS

Certifique-se que tem:
- ✅ Conta GitHub (https://github.com)
- ✅ Conta Vercel (https://vercel.com)
- ✅ Acesso ao GitHub como dpolonia

---

## PASSO 1: Criar Repositório GitHub

### 1.1 Criar Novo Repositório

1. Vá a: **https://github.com/new**
2. Preencha:
   - **Owner**: dpolonia
   - **Repository name**: `202511-JuniorAI`
   - **Description**: `Certificados IA e Bibliotecas - EBADS Ovar`
   - **Visibilidade**: Public ✅
   - **Initialize**: ❌ NÃO selecionar "Add a README file"
3. Clique em **"Create repository"**

### 1.2 Confirmar URL

Confirme que o repositório foi criado em:
`https://github.com/dpolonia/202511-JuniorAI`

---

## PASSO 2: Upload Inicial (Preparar Repositório)

### Opção A: Via GitHub Web Interface (MAIS FÁCIL)

#### 2.1 Criar Ficheiros Iniciais

Na página do repositório vazio, clique em **"creating a new file"**

**Ficheiro 1: README.md**
```markdown
# 202511-JuniorAI

Certificados da formação "IA e Bibliotecas" - Escola Básica António Dias Simões, Ovar

## 🎓 Formação IA Júnior

Sistema de certificados com privacidade protegida.

### Características
- ✅ URLs anónimos
- ✅ QR Codes incorporados
- ✅ Acesso por código individual

---

**Formação**: IA e Bibliotecas  
**Data**: 25 de novembro de 2025  
**Escola**: EBADS Ovar  
**Formandos**: 27
```

Commit: "Initial commit"

**Ficheiro 2: .gitignore**

Clique em "Add file" → "Create new file"

Nome: `.gitignore`

Conteúdo:
```
# Ficheiros privados
CODIGOS_PRIVADOS.md
mapeamento_privado.json
*_privado*

# Sistema
.DS_Store
Thumbs.db

# Python
__pycache__/
```

Commit: "Add gitignore"

### Opção B: Via Git Command Line

```bash
# Criar diretório local
mkdir 202511-JuniorAI
cd 202511-JuniorAI

# Inicializar git
git init
git branch -M main

# Criar README.md
cat > README.md << 'EOF'
# 202511-JuniorAI

Certificados IA e Bibliotecas - EBADS Ovar

Sistema em configuração...
EOF

# Criar .gitignore
cat > .gitignore << 'EOF'
CODIGOS_PRIVADOS.md
mapeamento_privado.json
EOF

# Commit inicial
git add .
git commit -m "Initial commit"

# Conectar ao GitHub
git remote add origin https://github.com/dpolonia/202511-JuniorAI.git
git push -u origin main
```

---

## PASSO 3: Conectar ao Vercel

Agora que o repositório tem conteúdo inicial, conecte ao Vercel:

### 3.1 Importar Projeto

1. Vá a: **https://vercel.com/new**
2. Selecione **"Import Git Repository"**
3. Encontre e selecione: **dpolonia/202511-JuniorAI**
4. Clique em **"Import"**

### 3.2 Configurar Projeto

- **Project Name**: `202511-juniorai` (ou deixar sugestão do Vercel)
- **Framework Preset**: Other
- **Root Directory**: `./`
- Deixe tudo mais como está

5. Clique em **"Deploy"**

### 3.3 Obter URL do Vercel

Após deploy (30-60 segundos):
- Vercel mostrará o URL, algo como:
  - `https://202511-juniorai.vercel.app`
  - ou `https://202511-juniorai-xxx.vercel.app`

**⚠️ ANOTE ESTE URL** - será necessário no próximo passo!

---

## PASSO 4: Adicionar Certificados

Agora que o repositório está conectado ao Vercel, adicione os certificados:

### 4.1 Se o URL do Vercel for DIFERENTE

Se o URL não for exatamente `https://202511-juniorai.vercel.app`:

1. Extraia os ficheiros
2. Edite `gerar_certificados_anonimos.py`
3. Altere linha 28:
   ```python
   BASE_URL = "https://SEU-URL-AQUI.vercel.app"
   ```
4. Execute:
   ```bash
   python3 gerar_certificados_anonimos.py
   ```

### 4.2 Upload dos Certificados

**Via GitHub Web:**

1. Vá a: https://github.com/dpolonia/202511-JuniorAI
2. Clique em **"Add file" → "Upload files"**
3. Arraste estes ficheiros:
   - Todos os `certificado_*.html` (27 ficheiros)
   - `index.html`
   - `vercel.json`
   - `README.md` (atualizado)
   - `gerar_certificados_anonimos.py`

4. ⚠️ **NÃO** faça upload de:
   - `CODIGOS_PRIVADOS.md`
   - `mapeamento_privado.json`

5. Commit message: "Adicionar certificados IA Júnior"
6. Clique em **"Commit changes"**

**Via Git Command Line:**

```bash
cd 202511-JuniorAI

# Copiar certificados
cp /caminho/certificado_*.html .
cp /caminho/index.html .
cp /caminho/vercel.json .
# ... outros ficheiros públicos

# Commit e push
git add .
git commit -m "Adicionar certificados IA Júnior"
git push origin main
```

### 4.3 Aguardar Deploy

- Vercel detecta o push automaticamente
- Deploy completa em 1-2 minutos
- Verifique em: `https://SEU-URL.vercel.app`

---

## PASSO 5: Verificar e Testar

### 5.1 Testar Site

1. Abra: `https://202511-juniorai.vercel.app` (ou seu URL)
2. Deve ver a página de busca
3. Insira código: **001**
4. Deve abrir certificado do Artur Mesquita
5. Verifique se QR code está visível
6. Teste impressão (Ctrl+P)

### 5.2 Verificar Dashboard

**GitHub**: https://github.com/dpolonia/202511-JuniorAI
- ✅ 27 certificados HTML
- ✅ index.html
- ✅ vercel.json
- ✅ README.md

**Vercel**: https://vercel.com (seu projeto)
- ✅ Status: Ready
- ✅ URL funcionando
- ✅ Deployments: 2+ (inicial + certificados)

---

## PASSO 6: Distribuir aos Alunos

### 6.1 Consultar Códigos

Abra o ficheiro **CODIGOS_PRIVADOS.md** (local, privado)

### 6.2 Enviar Emails

Template:
```
Olá [Nome],

O teu certificado da formação "IA e Bibliotecas" está online!

🔗 Acede aqui: https://202511-juniorai.vercel.app
🔢 Código: [XXX]

O certificado tem um QR code para partilhares.

Cumprimentos,
Daniel Polónia
EBADS Ovar
```

---

## ✅ CHECKLIST FINAL

Antes de distribuir aos alunos:

- [ ] Repositório criado no GitHub
- [ ] Commit inicial feito
- [ ] Projeto conectado ao Vercel
- [ ] URL do Vercel obtido
- [ ] Certificados gerados com URL correto
- [ ] Certificados enviados para GitHub
- [ ] Deploy completado no Vercel
- [ ] Site testado (https://202511-juniorai.vercel.app)
- [ ] Código 001 testado
- [ ] QR code visível
- [ ] Impressão testada
- [ ] Ficheiros privados guardados localmente
- [ ] Ficheiros privados NÃO no GitHub

---

## 🔗 LINKS IMPORTANTES

Após setup completo:

- **Site**: https://202511-juniorai.vercel.app
- **GitHub**: https://github.com/dpolonia/202511-JuniorAI
- **Vercel Dashboard**: https://vercel.com (login necessário)
- **Códigos Privados**: CODIGOS_PRIVADOS.md (local)

---

## ❓ PROBLEMAS COMUNS

### "Repositório não foi criado"
→ Vá a https://github.com/new e crie manualmente

### "Vercel não encontra o repositório"
→ Certifique-se que o repositório tem conteúdo inicial
→ Faça refresh na página do Vercel

### "URL do Vercel é diferente"
→ Edite gerar_certificados_anonimos.py
→ Regenere certificados
→ Faça novo upload

### "Certificados não aparecem"
→ Verifique se fez upload de todos os ficheiros HTML
→ Aguarde 2-3 minutos para deploy
→ Limpe cache (Ctrl+F5)

---

## 📞 SUPORTE

Se precisar de ajuda:
1. Verifique este guia passo a passo
2. Consulte logs no dashboard do Vercel
3. Verifique commits no GitHub

---

**Tempo estimado**: 10-15 minutos  
**Dificuldade**: Fácil  
**Custo**: €0 (totalmente gratuito)

🎉 **Boa sorte com o setup!**
