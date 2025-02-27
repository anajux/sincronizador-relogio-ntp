# ⏰ Sincronizador de Relógio com NTP

Este é um projeto acadêmico que implementa um sincronizador de relógio utilizando o protocolo NTP (Network Time Protocol). Ele consulta vários servidores NTP, calcula a média dos horários obtidos e ajusta o relógio do sistema para garantir precisão em sistemas distribuídos.

## 🚀 Funcionalidades

Consulta múltiplos servidores NTP para obter o horário correto

Calcula a média dos horários para maior precisão

Ajusta o relógio do sistema automaticamente

Exibe informações detalhadas sobre a sincronização

## 📌 Tecnologias Utilizadas

Python

Biblioteca ntplib para comunicação com servidores NTP

time para manipulação de datas e horas

os para ajuste do relógio do sistema

## 📦 Instalação

Clone este repositório:
git clone https://github.com/anajux/sincronizador-ntp.git

cd sincronizador-ntp

Instale as dependências:
pip install ntplib

Execute o sincronizador:
python sincronizador.py

## ⚠️ Permissões Necessárias

Para modificar o horário do sistema, é necessário executar o script como administrador:


sudo python sincronizador.py  # Linux/Mac


python sincronizador.py       # Windows (executar como administrador)

## 🖥️ Como Funciona

O script faz requisições a vários servidores NTP

Calcula a média dos horários retornados

Ajusta o relógio do sistema de acordo com o horário sincronizado

## 📜 Licença

Este projeto é de uso acadêmico e distribuído sob a licença MIT.

