# signature-pipeline

Pipeline de linha de comando que recebe um documento em PDF, recorta a região
da assinatura com o **Tesseract** e pergunta a um modelo de visão no **Ollama**
se o recorte tem assinatura manuscrita.

> Esqueleto: as funções têm só a assinatura e `pass`. A docstring de cada uma
> diz o que ela deve fazer.

## Fluxo

```mermaid
flowchart LR
    A([PDF]) --> B[load_page] --> C[pytesseract<br/>image_to_data] --> D[crops_target] --> E[ollama_ask] --> F([tem assinatura?])
```

1. `load_page`: abre a página do PDF como imagem.
2. `pytesseract.image_to_data`: lê as palavras e as posições delas (conferir com `show_box`).
3. `crops_target`: acha a âncora ("Diretora") e recorta a região acima dela.
4. `ollama_ask`: envia o recorte ao `qwen2.5vl:3b`.
5. `SignatureDetection`: valida a resposta `{"has_signature": true/false}`.

## O que implementar

| Arquivo | Funções |
|---------|---------|
| `src/signature_pipeline/tesseract_service.py` | `load_page`, `show`, `show_box`, `box`, `normalize`, `crops_target` |
| `src/signature_pipeline/ollama_service.py` | `ollama_ask` |
| `src/signature_pipeline/main.py` | `main` (junta tudo, os passos estão na docstring) |
| `src/signature_pipeline/schemas.py` | já pronto (`SignatureDetection`) |

## Requisitos

Três coisas na máquina: **Tesseract** (com o idioma português), **Ollama**
(com o modelo `qwen2.5vl:3b`) e **uv**. O uv baixa o Python 3.13 sozinho.

### Linux (Ubuntu/Debian)

```bash
# Tesseract com português
sudo apt install -y tesseract-ocr tesseract-ocr-por

# Ollama e o modelo de visão
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen2.5vl:3b

# uv
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows (PowerShell)

```powershell
# Tesseract (instalador da UB Mannheim)
winget install UB-Mannheim.TesseractOCR

# Ollama e o modelo de visão
winget install Ollama.Ollama
ollama pull qwen2.5vl:3b

# uv
winget install astral-sh.uv
```

Sem o `winget`, baixe os instaladores direto:
[Tesseract](https://github.com/UB-Mannheim/tesseract/wiki),
[Ollama](https://ollama.com/download/windows) e
[uv](https://docs.astral.sh/uv/getting-started/installation/).

Depois de instalar, **feche e abra o PowerShell** para ele enxergar os novos
comandos. No Windows, o Tesseract precisa de dois ajustes:

1. **Idioma português.** No instalador, em *Additional language data*, marque
   **Portuguese**. Se já instalou sem marcar, baixe o
   [`por.traineddata`](https://github.com/tesseract-ocr/tessdata/raw/main/por.traineddata)
   e copie para `C:\Program Files\Tesseract-OCR\tessdata\`.
2. **PATH.** O instalador não coloca o Tesseract no PATH. Adicione com:

   ```powershell
   [Environment]::SetEnvironmentVariable(
       "Path",
       [Environment]::GetEnvironmentVariable("Path", "User") + ";C:\Program Files\Tesseract-OCR",
       "User"
   )
   ```

   Outra opção é apontar o caminho no código, antes de usar o `pytesseract`:

   ```python
   pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
   ```

### Conferir a instalação (Linux e Windows)

```bash
tesseract --list-langs   # precisa aparecer "por"
ollama list              # precisa aparecer qwen2.5vl:3b
uv --version
```

## Como rodar

Linux:

```bash
uv sync
cp /caminho/do/certificado.pdf documentos/certificado.pdf
uv run signature-pipeline
```

Windows (PowerShell):

```powershell
uv sync
Copy-Item C:\caminho\do\certificado.pdf documentos\certificado.pdf
uv run signature-pipeline
```

## Problemas comuns

| Sintoma | Solução |
|---------|---------|
| `TesseractNotFoundError` | O Tesseract não está no PATH. No Windows, veja o passo 2 acima ou use o `tesseract_cmd`. |
| Erro com `por.traineddata` | Falta o idioma português. Linux: `sudo apt install tesseract-ocr-por`. Windows: copie o arquivo para a pasta `tessdata`. |
| `ollama` não é reconhecido (Windows) | Feche e abra o PowerShell depois de instalar. |
| Erro de conexão com o Ollama | O Ollama não está rodando. Linux: `ollama serve`. Windows: abra o app Ollama (ícone perto do relógio). |
| `uv` bloqueado pela política de execução (Windows) | Rode `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` e abra o PowerShell de novo. |

O documento de entrada é `PATH` e a pasta dos recortes é `RECORTES_DIR`,
ambos em `main.py`. As pastas `documentos/` e `recortes/` ficam fora do Git,
porque guardam documentos reais.

Para verificar o código:

```bash
uv run ruff check
```

## Estrutura

```
signature-pipeline/
├── documentos/                 # PDFs de entrada (fora do Git)
├── pyproject.toml              # dependências e o comando signature-pipeline
└── src/signature_pipeline/
    ├── main.py                 # main(): o pipeline completo
    ├── tesseract_service.py    # OCR, recorte e visualização
    ├── ollama_service.py       # chamada ao Ollama
    └── schemas.py              # formato da resposta do modelo
```
