"""Esqueleto do pipeline do main.py (sem web e sem API).

Só as funções que o main.py usa, com ``pass`` para implementar:

- tesseract_service.py -> load_page, show, show_box, crops_target
                          (+ box e normalize, que elas usam por dentro)
- ollama_service.py    -> ollama_ask
- schemas.py           -> SignatureDetection (já pronto)
- main.py              -> main, que junta tudo
"""
