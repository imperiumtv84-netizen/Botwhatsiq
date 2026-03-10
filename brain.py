import google.generativeai as genai
from config import GEMINI_KEY, SYSTEM_INSTRUCTION

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction=SYSTEM_INSTRUCTION
)

def processar_mensagem(texto_cliente):
    try:
        response = model.generate_content(texto_cliente)
        return response.text
    except Exception as e:
        print(f"Erro na IA: {e}")
        return "Desculpe, estou processando muitas mensagens. Pode repetir?"
