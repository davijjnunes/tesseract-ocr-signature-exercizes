"""OCR e recorte com o Tesseract."""

import fitz
import numpy as np


def load_page(doc: fitz.Document, page_num: int = 0, scale: float = 2, dpi: int = 300) -> np.ndarray:
    """Carrega a página do PDF como imagem BGR, com a melhor qualidade possível.

    - PDF escaneado (uma imagem cobrindo a página): extrai a imagem original,
      tira o ruído e amplia ``scale`` vezes com Lanczos.
    - PDF digital: renderiza no ``dpi`` pedido.
    """
    pass


def show(title: str, image: np.ndarray, height_max: int = 900) -> None:
    """Mostra a imagem numa janela do OpenCV, reduzida até ``height_max`` de altura.

    Espera uma tecla e fecha a janela.
    """
    pass


def show_box(result: dict, image: np.ndarray) -> None:
    """Desenha uma caixa e o texto em cada palavra do OCR com confiança > 60.

    ``result`` é a saída de ``pytesseract.image_to_data(..., output_type=Output.DICT)``.
    Usa ``box`` para desenhar e ``show`` para exibir.
    """
    pass


def box(
    result: dict, image: np.ndarray, index: int, color: tuple[int, int, int] = (0, 0, 255)
) -> tuple[int, int, np.ndarray]:
    """Desenha o retângulo da palavra ``index`` e devolve ``(x, y, imagem)``."""
    pass


def normalize(word: str) -> str:
    """Remove pontuação nas bordas e padroniza acentos e caixa.

    Exemplo: ``"DECLARAÇÃO:"`` -> ``"declaração"``.
    """
    pass


def crops_target(
    result: dict,
    image: np.ndarray,
    target: tuple[str, ...] = ("Diretora",),
    min_conf: float = 60,
    up: int = 8,
    down: int = 1,
    side: int = 12,
) -> list[tuple[np.ndarray, tuple[int, int, int, int]]]:
    """Retorna uma lista de ``(recorte, (x, y, w, h))`` para cada ocorrência do target.

    - Compara com ``normalize`` (o target pode estar dentro da palavra).
    - Ignora palavras com confiança abaixo de ``min_conf``.
    - A margem é medida em alturas da palavra: ``up`` acima, ``down`` abaixo e
      ``side`` para cada lado do centro, sem sair da imagem.
    """
    pass
