from neonize.client import NewClient
from neonize.events import ConnectedEv, MessageEv
from brain import processar_mensagem

def on_message(client: NewClient, message: MessageEv):
    # Ignora mensagens de grupos ou enviadas por você
    if message.Info.IsFromMe or message.Info.IsGroup:
        return

    # Extrai o texto da mensagem
    msg_text = message.Message.conversation or message.Message.extendedTextMessage.text
    
    if msg_text:
        print(f"Cliente disse: {msg_text}")
        
        # Chama a IA no outro arquivo
        resposta = processar_mensagem(msg_text)
        
        # Envia de volta
        client.send_message(message.Info.RemoteJid, resposta)

client = NewClient("sessao_whatsapp.db")
client.event_handler.register(MessageEv)(on_message)

print("Aguardando conexão...")
client.connect()
