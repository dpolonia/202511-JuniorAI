# 🚀 GUIA DE DEPLOY - Certificados Anónimos

## ✅ Sistema Pronto

Todos os certificados estão prontos com:
- ✅ IDs anónimos (001-027) - sem nomes nos URLs
- ✅ QR Codes incorporados
- ✅ Página de acesso por código
- ✅ 27 formandos

---

## ⚡ DEPLOY RÁPIDO (3 opções)

### Opção 1: Script Automático (RECOMENDADO)

```bash
cd /caminho/para/certificados
./deploy.sh
```

✅ Faz tudo automaticamente
✅ Copia apenas ficheiros públicos
✅ Commit e push para GitHub
✅ Vercel faz deploy automático

### Opção 2: Upload Manual via Web

1. Vá a: https://github.com/dpolonia/202511-JuniorAI
2. Clique em "Add file" → "Upload files"
3. Arraste estes ficheiros:
   - Todos os `certificado_*.html` (27 ficheiros)
   - `index.html`
   - `vercel.json`
   - `README.md`
   - `.gitignore`
   - `gerar_certificados_anonimos.py`

⚠️ **NÃO** faça upload de:
   - `CODIGOS_PRIVADOS.md`
   - `mapeamento_privado.json`

4. Commit: "Adicionar certificados anónimos com QR codes"
5. Aguarde 1-2 minutos
6. Verifique: https://202511-juniorai.vercel.app

### Opção 3: Git Command Line

```bash
# Clonar
git clone https://github.com/dpolonia/202511-JuniorAI.git
cd 202511-JuniorAI

# Copiar ficheiros públicos
cp /caminho/certificado_*.html .
cp /caminho/index.html .
cp /caminho/vercel.json .
cp /caminho/README.md .
cp /caminho/gerar_certificados_anonimos.py .

# Deploy
git add .
git commit -m "Adicionar certificados anónimos"
git push origin main
```

---

## 🔗 Após Deploy

### Verificar
- Site: https://202511-juniorai.vercel.app
- Dashboard: https://vercel.com/daniels-projects-cfa01595/202511-juniorai

### Testar
1. Abra https://202511-juniorai.vercel.app
2. Insira código "001"
3. Verificar se certificado do Artur Mesquita aparece
4. Verificar se QR code está visível
5. Testar impressão (Ctrl+P)

---

## 📱 Distribuir aos Alunos

### Método 1: Email Individual

Use o ficheiro **CODIGOS_PRIVADOS.md** para ver os códigos.

```
Assunto: Certificado IA e Bibliotecas

Olá [Nome],

Parabéns! O teu certificado está online.

Acede aqui: https://202511-juniorai.vercel.app
Código: [XXX]

O certificado tem um QR code para partilhares.

Cumprimentos,
Daniel Polónia
EBADS Ovar
```

### Método 2: Link Direto

Envie o link direto do certificado:
`https://202511-juniorai.vercel.app/certificado_[XXX].html`

Exemplo:
`https://202511-juniorai.vercel.app/certificado_001.html`

### Método 3: Cartões Impressos

Imprima cartões com:
```
┌──────────────────────┐
│  🏆 CERTIFICADO      │
│                      │
│  CÓDIGO: [XXX]       │
│                      │
│  202511-juniorai        │
│  .vercel.app         │
│                      │
│  [Nome do Aluno]     │
└──────────────────────┘
```

---

## 🔐 Segurança

### Ficheiros Públicos (GitHub)
- Certificados HTML (sem problema - nomes só aparecem dentro)
- index.html
- vercel.json
- README.md

### Ficheiros Privados (NÃO publicar)
- **CODIGOS_PRIVADOS.md** - Lista de códigos
- **mapeamento_privado.json** - Mapeamento ID→Nome

⚠️ Guarde os ficheiros privados em local seguro!
⚠️ Não faça commit destes ficheiros!

---

## ❓ Resolução de Problemas

### "Deploy falhou"
- Verifique credenciais do GitHub
- Confirme permissões de escrita no repositório
- Tente opção manual via web

### "Certificado não aparece"
- Aguarde 2-3 minutos após deploy
- Limpe cache do browser (Ctrl+F5)
- Verifique se ficheiro foi enviado

### "QR code não funciona"
- QR code aponta para o mesmo URL do certificado
- Verifique URL: https://202511-juniorai.vercel.app/certificado_XXX.html

### "Aluno perdeu código"
- Consulte CODIGOS_PRIVADOS.md
- Reenvie o código por email
- Ou envie link direto

---

## 🔧 Manutenção Futura

### Adicionar Formandos
1. Edite `gerar_certificados_anonimos.py`
2. Adicione à lista `formandos` com novo ID
3. Execute: `python3 gerar_certificados_anonimos.py`
4. Faça novo deploy

### Alterar URL
Edite `BASE_URL` em `gerar_certificados_anonimos.py`

### Regenerar Todos
```bash
python3 gerar_certificados_anonimos.py
./deploy.sh
```

---

## 📊 Checklist Final

Antes de partilhar com alunos:

- [ ] Deploy concluído
- [ ] Site acessível (https://202511-juniorai.vercel.app)
- [ ] Página de busca funciona
- [ ] Testado código 001
- [ ] QR code visível
- [ ] Impressão testada
- [ ] Códigos privados guardados
- [ ] Ficheiros privados NÃO no GitHub

---

## 📞 Links Úteis

- **Site**: https://202511-juniorai.vercel.app
- **GitHub**: https://github.com/dpolonia/202511-JuniorAI
- **Vercel**: https://vercel.com/daniels-projects-cfa01595/202511-juniorai
- **Códigos**: Consulte CODIGOS_PRIVADOS.md (local)

---

**Sistema implementado**: URLs anónimos + QR Codes  
**Formandos**: 27  
**Privacidade**: ✅ Protegida  
**Deploy**: Automatizado  
**Custo**: €0 (gratuito)

🎉 **Está pronto para uso!**
