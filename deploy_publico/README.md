# 🏆 Certificados IA e Bibliotecas (Sistema Privado)

Certificados da formação "IA e Bibliotecas" realizada na Escola Básica António Dias Simões - Ovar em 25 de novembro de 2025.

**Sistema com privacidade protegida**: URLs não contêm nomes de formandos.

## 🔗 Acesso Online

**URL do Projeto**: https://202511-juniorai.vercel.app

**Repositório GitHub**: https://github.com/dpolonia/202511-JuniorAI

**Projeto Vercel**: https://vercel.com/daniels-projects-cfa01595/202511-juniorai

## 🔐 Sistema de Privacidade

Este projeto implementa um sistema de certificados com IDs anónimos:

- ✅ **URLs não contêm nomes** - Apenas códigos numéricos (001-027)
- ✅ **QR Codes únicos** - Cada certificado tem um QR code para partilha
- ✅ **Página de acesso controlado** - Formandos inserem código para aceder
- ✅ **Proteção de privacidade** - Nomes não aparecem em URLs públicos

### Como Funciona

1. Cada formando recebe um **código de 3 dígitos** (001 a 027)
2. Acede a https://202511-juniorai.vercel.app
3. Insere o código
4. Acede ao certificado personalizado
5. Pode partilhar através do QR code incorporado

## 📋 Conteúdo do Projeto

### Ficheiros Públicos (para deploy)
- **27 certificados HTML** - `certificado_001.html` a `certificado_027.html`
- **index.html** - Página de acesso com busca por código
- **vercel.json** - Configuração do Vercel
- **gerar_certificados_anonimos.py** - Script para regenerar certificados

### Ficheiros Privados (NÃO fazer deploy)
- **CODIGOS_PRIVADOS.md** - Lista de códigos por formando
- **mapeamento_privado.json** - Mapeamento completo ID → Nome

⚠️ **IMPORTANTE**: Os ficheiros privados contêm a lista de nomes e NÃO devem ser enviados para o GitHub!

## 🚀 Deploy

### Método 1: Deploy Automático (Recomendado)

```bash
cd /caminho/para/os/ficheiros
./deploy.sh
```

O script irá:
1. Clonar o repositório
2. Copiar os certificados
3. Fazer commit
4. Push para o GitHub
5. Vercel faz deploy automaticamente

### Método 2: Deploy Manual via GitHub Web

1. Aceda a https://github.com/dpolonia/202511-JuniorAI
2. Clique em "Add file" → "Upload files"
3. Arraste APENAS os ficheiros públicos:
   - Todos os `certificado_*.html`
   - `index.html`
   - `vercel.json`
   - `.gitignore`
   - `README.md`
4. **NÃO** faça upload de:
   - `CODIGOS_PRIVADOS.md`
   - `mapeamento_privado.json`
5. Commit: "Adicionar certificados anónimos"
6. Aguarde deploy no Vercel (1-2 minutos)

### Método 3: Deploy via Git Command Line

```bash
# Clonar repositório
git clone https://github.com/dpolonia/202511-JuniorAI.git
cd 202511-JuniorAI

# Copiar apenas ficheiros públicos
cp /caminho/certificado_*.html .
cp /caminho/index.html .
cp /caminho/vercel.json .

# Commit e push
git add .
git commit -m "Adicionar certificados anónimos"
git push origin main
```

## 📱 Distribuir Códigos aos Formandos

Consulte o ficheiro **CODIGOS_PRIVADOS.md** (privado) para ver a lista completa de códigos.

### Email Individual (Recomendado)

```
Assunto: Certificado IA e Bibliotecas

Olá [Nome],

Parabéns por completar a formação "IA e Bibliotecas"!

Para acederes ao teu certificado:
1. Vai a: https://202511-juniorai.vercel.app
2. Insere o código: [XXX]
3. Clica em "Aceder ao Certificado"

O certificado tem um QR code para partilhares facilmente.

Cumprimentos,
Daniel Polónia
```

## 🔧 Manutenção

### Regenerar Certificados

```bash
python3 gerar_certificados_anonimos.py
```

### Adicionar Novos Formandos

1. Edite `gerar_certificados_anonimos.py`
2. Adicione à lista `formandos`
3. Execute o script
4. Faça novo deploy

### Alterar URL Base

Edite a variável `BASE_URL` em `gerar_certificados_anonimos.py`

## 📊 Estrutura dos Certificados

Cada certificado contém:
- Nome completo do formando
- Data e local da formação
- QR Code único apontando para o próprio certificado
- ID do certificado no canto inferior esquerdo
- Design profissional otimizado para impressão

## 🖨️ Impressão

Para imprimir um certificado:
1. Abra o certificado no browser
2. Ctrl+P (Windows) ou Cmd+P (Mac)
3. Selecione orientação "Landscape"
4. Imprima ou guarde como PDF

O QR code será impresso junto com o certificado.

## 🔒 Segurança e Privacidade

### O que é público:
- URLs dos certificados (mas sem nomes nos URLs)
- Conteúdo dos certificados (nomes aparecem dentro do certificado)
- QR codes

### O que é privado:
- Lista de códigos por formando
- Mapeamento ID → Nome
- Estes ficheiros NÃO estão no GitHub

### Boas Práticas:
- Distribua códigos individualmente (email, mensagem privada)
- Não publique a lista completa de códigos
- Guarde `CODIGOS_PRIVADOS.md` em local seguro
- Não faça commit de ficheiros privados

## ❓ FAQ

### Como um formando acede ao certificado?
1. Vai a https://202511-juniorai.vercel.app
2. Insere o código de 3 dígitos
3. Acede ao certificado

### E se um formando perder o código?
Consulte `CODIGOS_PRIVADOS.md` e forneça o código novamente.

### Posso partilhar o certificado nas redes sociais?
Sim! Cada certificado tem um QR code que pode ser partilhado.
O URL não contém o nome do formando.

### Como verificar se um certificado é autêntico?
Scan do QR code no certificado - deve apontar para https://202511-juniorai.vercel.app

## 📞 Suporte Técnico

- **Dashboard Vercel**: https://vercel.com/daniels-projects-cfa01595/202511-juniorai
- **Repositório GitHub**: https://github.com/dpolonia/202511-JuniorAI
- **Documentação completa**: Consulte os ficheiros .md incluídos

## 🎓 Estatísticas

- **Total de formandos**: 27
- **Formato**: HTML5 + CSS3
- **QR Codes**: Incorporados (Base64)
- **Privacidade**: URLs anónimos
- **Impressão**: A4 Landscape
- **Custo**: Gratuito (GitHub + Vercel)

---

**Projeto criado com Claude AI** 🤖  
**Para**: Escola Básica António Dias Simões - Ovar  
**Data**: 25 de novembro de 2025  
**Formação**: IA e Bibliotecas
