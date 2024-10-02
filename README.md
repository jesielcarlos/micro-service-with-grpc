# Microsserviços com gRPC e Python

Este repositório é dedicado ao estudo do desenvolvimento de microsserviços utilizando Python e gRPC. O objetivo é implementar serviços altamente escaláveis e de fácil manutenção.

## Índice

- [Visão Geral](#visão-geral)
- [Tecnologias](#tecnologias)
- [Arquitetura](#arquitetura)
- [Instalação](#instalação)

## Visão Geral

Este projeto demonstra como construir microsserviços com gRPC em Python. O foco está em criar APIs de alta performance, modularizadas utilizando os princípios de arquitetura de microsserviços. Os conceitos principais incluem a comunicação entre serviços via gRPC e a adesão aos princípios SOLID, DDD e Clean Architecture, para garantir a escalabilidade e a manutenção do código.

## Tecnologias

- **Python 3.x**: Linguagem de programação utilizada para implementar os serviços.
- **gRPC**: Framework de RPC de alta performance utilizado para a comunicação entre os microsserviços.
- **Protocol Buffers**: Formato de serialização para a comunicação via gRPC.
- **Docker**: Para a conteinerização dos serviços e facilitar a implantação.
- **Kubernetes**: (Opcional) Orquestração para escalar e gerenciar os microsserviços.

## Arquitetura

O projeto está estruturado seguindo os princípios da Clean Architecture:

- **Server**: Cria o servidor grpc com os métodos disponíveis.
- **Client**: Executa as requisições ao servidor grpc.

### Comunicação entre os Serviços

- **gRPC**: Os serviços se comunicam entre si utilizando gRPC. Protocol Buffers (protobuf) são usados para definir as mensagens e as interfaces de serviço.

## Instalação

Para configurar o projeto localmente, siga os passos abaixo:

1. Clone o repositório:

   ```bash
   git clone https://github.com/jesielcarlos/micro-service-with-grpc.git
   cd microsservicos-grpc-python
