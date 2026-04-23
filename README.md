# 🚀 Automações em Python
Coleção de scripts de automação desenvolvidos para otimizar processos operacionais, marketing digital e produção de conteúdo em escala.

Este repositório reúne automações reais utilizadas no dia a dia, com foco em:
- Redução de tarefas manuais
- Ganho de produtividade
- Padronização de processos
- Escalabilidade (principalmente SEO e conteúdo)

---

## 📌 Sobre o Projeto
Este projeto centraliza diversas automações construídas em Python, utilizando principalmente:

- Controle de interface (RPA) com PyAutoGUI
- Scripts baseados em dados (JSON)
- Interfaces simples com Tkinter/CustomTkinter
- Integrações indiretas com sistemas web

As automações simulam ações humanas como cliques, digitação e navegação, permitindo automatizar sistemas que não possuem API.

---

## ⚙️ Automações Disponíveis

### 📄 auto_alterar_paginas_existentes
Automação para edição em massa de páginas no painel administrativo.

- Busca páginas por cidade
- Substitui HTML completo
- Injeta conteúdo dinâmico (cidade + blocos)
- Preenche SEO automaticamente (title, keywords, description)

👉 Uso principal: **SEO programático**

---

### 🌐 auto_criar_paginas_web
Criação automatizada de páginas internas com template dinâmico.

- Substituição de placeholders
- Inserção de dados personalizados
- Automação via navegador

---

### 🛒 auto_abrir_pedidos
Automação de abertura de pedidos em sistema interno.

- Navegação automática
- Preenchimento de campos
- Redução de tarefas repetitivas

---

### 📦 auto_cria_produtos
Automação para cadastro de produtos.

- Inserção de dados padronizados
- Agilidade no cadastro em massa

---

### 📧 auto_criar_campanhas_news
Automação para criação de campanhas (ex: SendPulse).

- Interface para gerenciar campanhas
- Definição de horários, tags e conteúdo

---

### 📱 auto_criar_stories
Automação para criação e agendamento de stories.

- Upload automático de mídia
- Definição de datas e horários
- Uso em Meta Business

---

### 🎬 auto_editar_video_capcut
Automação de edição de vídeos no CapCut.

- Ajustes de escala, posição e áudio
- Controle de velocidade
- Exportação automatizada

---

### 🧹 auto_deletar_arquivos
Script para limpeza de arquivos duplicados.

- Compara pastas
- Remove arquivos repetidos
- Suporte a múltiplos formatos

---

### 📁 auto_fechamento_de_arquivos
Automação para organização e fechamento de arquivos.

- Preparação para impressão
- Padronização de saída

---

### 🖱️ position_x_y
Ferramenta auxiliar para capturar coordenadas do mouse.

- Essencial para automações com PyAutoGUI

---

### 🔳 criar_qr_code
Gerador de QR Codes com interface.

- Personalização de cores
- Controle de tamanho e versão
- Exportação em PNG

---

### 🧩 interface_basica_para_auto
Interface simples para centralizar execuções.

- Botões para disparar automações
- Base para criação de painel interno

---

## 🧠 Como Funciona

A maioria das automações segue este fluxo:

1. Entrada de dados (manual ou JSON)
2. Execução de ações automatizadas (mouse/teclado ou navegador)
3. Inserção de conteúdo dinâmico
4. Salvamento e finalização

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.x

Instale as dependências:

```bash
pip install pyautogui pyperclip customtkinter qrcode

Certifique-se de instalar as dependências via pip antes de rodar os scripts.

Observações
Todos os scripts foram testados em Windows 1920x1080 (alguns podem precisar ajustes de coordenadas para outras resoluções).
Alguns scripts interagem diretamente com navegadores e sistemas internos, portanto use com cuidado e sempre teste com dados de teste.
