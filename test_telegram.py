from config import *
import telebot
import threading

### DEFINES ################################
DIAS_SEMANA = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
EMOJIS_NUMEROS = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟','1️⃣1️⃣','1️⃣2️⃣','1️⃣3️⃣','1️⃣4️⃣','1️⃣5️⃣','1️⃣6️⃣','1️⃣7️⃣','1️⃣8️⃣','1️⃣9️⃣','2️⃣0️⃣']

### VARIABLES ##############################
bot = telebot.TeleBot(BOT_TOKEN)
lista_semanal = {}
lista_socios = []
lista_admins = []
lista_negra = []
lista_dolorosa = {} # Para el futuro
max_miembros_diarios = 7

### INTERFAZ ###############################
def AñadirDia(dia):
    lista_semanal[dia] = []

def QuitarDia(dia):
    del lista_semanal[dia]

def PlazasLibres(dia):
    if dia in lista_semanal:
        return max_miembros_diarios - len(lista_semanal[dia])
    return 0

def ImprimirLista():
    message = '[Texto de ejemplo lol]\n'
    for dia, lista in lista_semanal.items():
        emoji_estado = '🟢'
        estado_plaza = 'DISPONIBLE'
        if PlazasLibres(dia) == 0:
            emoji_estado = '🔴'
            estado_plaza = 'COMPLETO'
        elif PlazasLibres(dia) == 1:
            emoji_estado = '🟡'
            estado_plaza = 'ÚLTIMA PLAZA'

        dia_mayus = dia.capitalize()
        message += '[' + emoji_estado + '] ' + dia_mayus + ' ' + estado_plaza + '\n\n'
        for i in range(max_miembros_diarios):
            message += EMOJIS_NUMEROS[i] + ' '
            if i < len(lista):
                message += lista[i]
            message += '\n'
        message += '\n'

    return message

### TELEGRAM ###############################
@bot.message_handler(commands=['lista'])
def on_command(message):
    bot.reply_to(message, ImprimirLista())

def recibir_mensajes():
    bot.infinity_polling()

### MAIN ###################################
if __name__ == '__main__':
    print('Iniciando el bot...')
    #hilo_bot = threading.Thread(name='Hilo_bot', target=recibir_mensajes)
    AñadirDia(DIAS_SEMANA[5])
    AñadirDia(DIAS_SEMANA[6])
    recibir_mensajes() 
    print('Fin de la ejecución')