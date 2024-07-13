# API center norte

## O que é?

Aplicação responsável por mapear os dados do cliente e indicar suas preferências, baseadas no caminho que fará pelo Shopping 

## Pré-requisitos

Python 3.x instalado

## Clone o repositório

git clone https://github.com/PGutoo/roadmap-center-norte.git

## Instale as bibliotecas necessárias

pip install -r requirements.txt

## Consumo

Para consumir a API acesse a url https://roadmap-center-norte-yrqz.vercel.app

| Rotas                       | Função                                                                                                               |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------|
| /login/{email}              | Identifica se o cliente existe na base de dados fornecida, caso exista retorna o nome do cliente com as preferências |
| /preferencias/{preferencia} | Retorna as lojas com base na preferência do cliente                                                                  |

cê encontre essa aplicação útil! Se você tiver alguma dúvida, fique à vontade para perguntar.