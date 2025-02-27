import ntplib
import time
import os
from statistics import mean

SERVIDORES_NTP = [
    "time.apple.com",
    "ntp.ubuntu.com",
    "time2.google.com",
    "time3.google.com",
    "time4.google.com",
    "pool.ntp.org",
]

def obter_horario_ntp(servidor):
    cliente = ntplib.NTPClient()
    try:
        orig_time = time.time()  
        resposta = cliente.request(servidor, version=3)
        dest_time = time.time() 
        
        print(f"\n** HORAS **: ")
        print(f"Servidor: {servidor}")
        print(f"Horário que enviou a requisição: {orig_time}")
        print(f"Horário que o NTP recebeu a requisição: {resposta.recv_time}")
        print(f"Horário que o NTP enviou a resposta: {resposta.tx_time}")
        print(f"Horário que a resposta foi recebida: {dest_time}")

        delay = ((dest_time - orig_time) - (resposta.tx_time - resposta.recv_time)) / 2
        print('\nDELAY = ((Horário que a resposta foi recebida - Horário que enviou a requisição) - (Horário que o NTP enviou a resposta - Horário que o NTP recebeu a requisição)) / 2')
        print(f"Delay calculado: {delay} segundos")
        horario_ajustado = resposta.tx_time - delay 
        print(f'\nHORÁRIO: {horario_ajustado} - DELAY: {delay} = {horario_ajustado}')

        return horario_ajustado
    except Exception as erro:
        print(f"Erro ao consultar {servidor}: {erro}")
        return None


def obter_media_horario_ntp():
    horarios_ntp = []
    for servidor in SERVIDORES_NTP:
        timestamp = obter_horario_ntp(servidor)
        if timestamp:
            print(
                f"{servidor}: {time.strftime('%d-%m-%Y %H:%M:%S', time.gmtime(timestamp))} (UTC)")
            horarios_ntp.append(timestamp)

    if not horarios_ntp:
        print("Nenhum servidor disponível!")
        return None

    media_horario_ntp = mean(horarios_ntp)
    return media_horario_ntp


def definir_horario_sistema(timestamp):
    horario_formatado = time.strftime(
        '%d-%m-%Y %H:%M:%S', time.localtime(timestamp))
    print(f"Sincronizando sistema para: {horario_formatado}")

    os.system(
        f'date {horario_formatado[:10]} && time {horario_formatado[11:]}')


def sincronizar_horario_sistema():
    media_horario_ntp = obter_media_horario_ntp()
    if media_horario_ntp is None:
        return

    print(
        f"\nMédia dos horários NTP: {time.strftime('%d-%m-%Y %H:%M:%S', time.gmtime(media_horario_ntp))} (UTC)")

    definir_horario_sistema(media_horario_ntp)
    print("Hora sincronizada com sucesso!")


# Executar sincronização
sincronizar_horario_sistema()