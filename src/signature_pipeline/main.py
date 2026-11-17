"""Pipeline completo pelo terminal.

Uso:
    uv run signature-pipeline
"""

# ruff: noqa: F401  (imports que o main vai usar; tire ao implementar)
from pathlib import Path

import cv2
import fitz
import matplotlib.pyplot as plt
import pytesseract
from pytesseract import Output

from signature_pipeline.ollama_service import ollama_ask
from signature_pipeline.schemas import SignatureDetection
from signature_pipeline.tesseract_service import (
    crops_target,
    load_page,
    show,
    show_box,
)

PATH = Path("documentos/certificado.pdf")
RECORTES_DIR = Path("recortes")

SYSTEM_PROMPT = "Você analisa documentos e responde só com base na imagem."

USER_PROMPT = (
    "Há alguma assinatura manuscrita (rabisco ou rubrica feita à caneta) nesta imagem? "
    'Responda em JSON: {"has_signature": true} ou {"has_signature": false}.'
)


def main() -> None:
    """Roda o pipeline em ``PATH``.

    1. Abrir o PDF com ``fitz.open`` e carregar a página 0 (``load_page``).
    2. Converter para cinza e rodar ``pytesseract.image_to_data``
       (``lang="por"``, ``config="--psm 6"``, ``Output.DICT``).
    3. Conferir as palavras lidas com ``show_box``.
    4. Recortar com ``crops_target`` e salvar em ``RECORTES_DIR/target_{n}.png``.
       Se não houver recorte, avisar "Target não encontrado".
    5. Enviar o recorte ao modelo com ``ollama_ask``
       (``format=SignatureDetection.model_json_schema()``).
    6. Validar com ``SignatureDetection.model_validate_json`` e imprimir o resultado.
    """
    pass


if __name__ == "__main__":
    main()
