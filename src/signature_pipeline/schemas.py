"""Formato da resposta do modelo (pronto: é o contrato entre as etapas)."""

from pydantic import BaseModel, Field


class SignatureDetection(BaseModel):
    has_signature: bool = Field(description="True se o documento tem assinatura manuscrita.")
