"""Pipeline completo pelo terminal.

Uso:
    uv run signature-pipeline
"""

# ruff: noqa: F401  (imports que o main vai usar; tire ao implementar)
import json
from pathlib import Path

import cv2
import fitz
import matplotlib.pyplot as plt
import pytesseract
from pytesseract import Output

from signature_pipeline.ollama_service import ollama_ask
from signature_pipeline.tesseract_service import (
    crops_target,
    load_page,
    show,
    show_box,
)

# caminhos a partir da raiz do projeto: funciona de qualquer pasta
ROOT_DIR = Path(__file__).resolve().parents[2]
DOCUMENTOS_DIR = ROOT_DIR / "documentos"
RECORTES_DIR = ROOT_DIR / "recortes"

PATH = DOCUMENTOS_DIR / "certificadoDavi.png"  # troque para testar outro certificado

SYSTEM_PROMPT = "Você analisa documentos e responde só com base na imagem."

USER_PROMPT = (
    "Há alguma assinatura manuscrita (rabisco ou rubrica feita à caneta) nesta imagem? "
    'Responda em JSON: {"has_signature": true} ou {"has_signature": false}.'
)


def main() -> None:
    """Roda o pipeline em ``PATH``.

    1. Abrir o documento com ``fitz.open`` (aceita PDF, PNG e JPG) e carregar
       a página 0 (``load_page``).
    2. Converter para cinza e rodar ``pytesseract.image_to_data``
       (``lang="por"``, ``config="--psm 6"``, ``Output.DICT``).
    3. Conferir as palavras lidas com ``show_box``.
    4. Recortar com ``crops_target``, criar ``RECORTES_DIR`` e salvar cada recorte
       como ``RECORTES_DIR / f"{PATH.stem}_{n}.png"``.
       Se não houver recorte, avisar "Target não encontrado".
    5. Enviar o recorte ao modelo com ``ollama_ask``
       (``format="json"``).
    6. Ler a resposta com ``json.loads`` e imprimir ``answer["has_signature"]``.
    """
    pass


if __name__ == "__main__":
    main()
