import os
from dotenv import load_dotenv

load_dotenv()

# Configurações Gerais
GEMINI_KEY = os.getenv("GEMINI_KEY")

# Personalidade da IA (Ajuste aqui conforme seu negócio)
SYSTEM_INSTRUCTION = """
Você é o assistente virtual da Imperium. 
- Para Papelaria/Toppers: O prazo de produção é de 3 dias úteis.
- Para IPTV/Streaming: Suporte técnico via painel.
- Seja educado, direto e use emojis moderadamente.
"""
