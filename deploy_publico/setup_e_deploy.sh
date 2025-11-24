#!/bin/bash
# Script de Setup e Deploy Completo
# Certificados IA e Bibliotecas - EBADS Ovar

set -e  # Parar em caso de erro

echo "🚀 Setup e Deploy Automático - 202511-JuniorAI"
echo "================================================"
echo ""

# Configurações
REPO_URL="https://github.com/dpolonia/202511-JuniorAI.git"
REPO_DIR="/tmp/202511-juniorai-setup"
SOURCE_DIR="/mnt/user-data/outputs"

# Cores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

log_info() {
    echo -e "${GREEN}✓${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}⚠${NC} $1"
}

log_error() {
    echo -e "${RED}✗${NC} $1"
}

# Verificar git
if ! command -v git &> /dev/null; then
    log_error "Git não está instalado!"
    exit 1
fi

log_info "Git encontrado"

# Limpar diretório temporário
if [ -d "$REPO_DIR" ]; then
    log_warn "Removendo diretório temporário existente..."
    rm -rf "$REPO_DIR"
fi

# Clonar repositório
log_info "Clonando repositório 202511-JuniorAI..."
git clone "$REPO_URL" "$REPO_DIR" 2>&1 || {
    log_error "Falha ao clonar repositório!"
    log_warn "Certifique-se que o repositório existe: $REPO_URL"
    exit 1
}

cd "$REPO_DIR"

# Configurar git
git config user.name "Daniel Polonia" 2>/dev/null || true
git config user.email "dpolonia@ua.pt" 2>/dev/null || true

log_info "Repositório clonado com sucesso"

# Verificar se repositório está vazio
if [ -z "$(ls -A | grep -v '^\.git$')" ]; then
    log_warn "Repositório vazio - Criando commit inicial..."
    
    # Criar README inicial
    cat > README.md << 'EOF'
# 202511-JuniorAI

Certificados da formação "IA e Bibliotecas" - Escola Básica António Dias Simões, Ovar

## 🎓 Formação IA Júnior

Sistema de certificados com privacidade protegida para os formandos.

### Características
- ✅ URLs anónimos (sem nomes expostos)
- ✅ QR Codes incorporados
- ✅ Acesso por código individual
- ✅ Design profissional

---

**Formação**: IA e Bibliotecas  
**Data**: 25 de novembro de 2025  
**Escola**: EBADS Ovar  
**Formandos**: 27
EOF

    # Criar .gitignore básico
    cat > .gitignore << 'EOF'
# Ficheiros privados
CODIGOS_PRIVADOS.md
mapeamento_privado.json
*_privado*
*_PRIVADO*

# Sistema
.DS_Store
Thumbs.db
*.swp

# Python
__pycache__/
*.py[cod]
EOF

    git add README.md .gitignore
    git commit -m "Initial commit - Setup repositório 202511-JuniorAI

- Adicionar README inicial
- Configurar .gitignore
- Preparar para deploy de certificados"

    log_info "Commit inicial criado"
    
    # Push do commit inicial
    log_info "Fazendo push do commit inicial..."
    if git push origin main 2>&1; then
        log_info "Commit inicial enviado com sucesso!"
        echo ""
        log_warn "⏳ Aguarde 30 segundos para o repositório sincronizar..."
        sleep 30
    else
        log_error "Falha ao fazer push do commit inicial"
        exit 1
    fi
else
    log_info "Repositório já tem conteúdo inicial"
fi

# Agora adicionar os certificados
log_info "Adicionando certificados ao repositório..."

# Limpar ficheiros antigos (exceto .git e README.md)
find . -type f ! -path './.git/*' ! -name 'README.md' -delete 2>/dev/null || true

# Copiar certificados
log_info "Copiando 27 certificados..."
cp "$SOURCE_DIR"/certificado_*.html . 2>/dev/null || log_warn "Certificados não encontrados"

# Copiar página índice
cp "$SOURCE_DIR/index.html" . 2>/dev/null || log_warn "index.html não encontrado"

# Copiar configuração Vercel
cp "$SOURCE_DIR/vercel.json" . 2>/dev/null || log_warn "vercel.json não encontrado"

# Copiar .gitignore atualizado
cp "$SOURCE_DIR/.gitignore" . 2>/dev/null || log_warn ".gitignore não encontrado"

# Copiar README completo
cp "$SOURCE_DIR/README.md" . 2>/dev/null || log_warn "README.md não encontrado"

# Copiar scripts
cp "$SOURCE_DIR/gerar_certificados_anonimos.py" . 2>/dev/null || log_warn "Script de geração não encontrado"

# NÃO copiar ficheiros privados
log_warn "Ficheiros privados NÃO serão copiados (CODIGOS_PRIVADOS.md, mapeamento_privado.json)"

# Contar ficheiros
NUM_CERT=$(ls -1 certificado_*.html 2>/dev/null | wc -l)
log_info "Total de certificados copiados: $NUM_CERT"

# Verificar alterações
if [ -z "$(git status --porcelain)" ]; then
    log_warn "Nenhuma alteração detectada."
    cd /
    rm -rf "$REPO_DIR"
    exit 0
fi

# Mostrar status
echo ""
echo "Ficheiros alterados:"
echo "-------------------"
git status --short
echo ""

# Adicionar ficheiros
log_info "Adicionando ficheiros ao git..."
git add .

# Commit
COMMIT_MSG="Adicionar certificados IA Júnior com privacidade protegida

- 27 certificados com IDs anónimos (001-027)
- QR codes incorporados em cada certificado
- Página de acesso por código
- Sistema de privacidade implementado
- URLs sem nomes de formandos

Formação: IA e Bibliotecas
Escola: EBADS Ovar
Data: 25 de novembro de 2025
Formandos: $NUM_CERT"

log_info "Criando commit..."
git commit -m "$COMMIT_MSG"

# Push
echo ""
log_info "Fazendo push para o GitHub..."
if git push origin main 2>&1; then
    log_info "Push realizado com sucesso!"
    echo ""
    echo "════════════════════════════════════════════"
    echo "✅ DEPLOY CONCLUÍDO COM SUCESSO!"
    echo "════════════════════════════════════════════"
    echo ""
    echo "🌐 Próximos passos:"
    echo ""
    echo "1. Conectar ao Vercel:"
    echo "   → Vá a: https://vercel.com/new"
    echo "   → Importe: dpolonia/202511-JuniorAI"
    echo "   → Clique em 'Deploy'"
    echo ""
    echo "2. Após deploy no Vercel:"
    echo "   → Obtenha o URL: https://202511-juniorai.vercel.app"
    echo "   → (ou o URL que o Vercel atribuir)"
    echo ""
    echo "3. Se o URL for diferente:"
    echo "   → Edite gerar_certificados_anonimos.py"
    echo "   → Atualize BASE_URL com o novo URL"
    echo "   → Execute: python3 gerar_certificados_anonimos.py"
    echo "   → Execute novamente este script"
    echo ""
    echo "📱 Site (após Vercel):"
    echo "   https://202511-juniorai.vercel.app"
    echo ""
    echo "📊 GitHub:"
    echo "   https://github.com/dpolonia/202511-JuniorAI"
    echo ""
    echo "════════════════════════════════════════════"
    echo ""
else
    log_error "Falha ao fazer push!"
    echo ""
    echo "Possíveis causas:"
    echo "1. Sem permissões de escrita"
    echo "2. Credenciais não configuradas"
    echo "3. Problemas de rede"
    echo ""
    cd /
    rm -rf "$REPO_DIR"
    exit 1
fi

# Limpar
cd /
rm -rf "$REPO_DIR"
log_info "Diretório temporário removido"

echo ""
echo "🎉 Processo concluído!"
echo ""
echo "⚠️  LEMBRE-SE:"
echo "   • Configurar projeto no Vercel"
echo "   • Distribuir códigos aos alunos (ver CODIGOS_PRIVADOS.md)"
echo "   • NÃO fazer upload de ficheiros privados"
echo ""
