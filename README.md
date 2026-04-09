Automação de Tarefas Diversas

Este repositório reúne scripts de automação para marketing digital, criação de conteúdo, edição de vídeos, geração de QR Codes, gerenciamento de arquivos e interfaces básicas de controle.

Scripts Incluídos
1. Disparo de Campanhas SendPulse
Automatiza o envio de campanhas de e-mail pelo SendPulse.
Permite adicionar múltiplas campanhas com assunto, complemento, tags, ID da página e horário.
Interface gráfica em Tkinter para gerenciar campanhas.
2. Criação de Páginas Internas
Automação para criar páginas no sistema interno expanssiva.com.br.
Substitui placeholders em templates (codigo.txt) com dados de cidade, título, keywords e descrição.
Controla navegador e cliques via PyAutoGUI.
3. Agendamento de Stories Meta (Facebook)
Automatiza a criação e programação de stories no Meta Business.
Seleção de arquivos de pastas específicas, preenchimento de datas e horários.
Validação de erros de upload de vídeos.
4. Limpeza de Arquivos Duplicados
Script que deleta arquivos de uma pasta caso já existam em outra.
Suporta múltiplas extensões de mídia e confirma antes de deletar.
5. Edição de Vídeos no CapCut
Automatiza ajustes de escala, posição, áudio, velocidade e exportação de vídeos no CapCut.
Controla cliques e atalhos via PyAutoGUI.
6. Fechamento de Receituários
Interface em CustomTkinter para gerar receituários em formatos 15x21 ou 14x20.
Automatiza fechamento e organização dos arquivos para impressão.
7. Gerador de QR Code
Interface Tkinter para gerar QR Codes personalizados.
Permite definir cores, tamanho, borda, versão e salvar em PNG.
8. Painel Básico de Controle
Interface simples em CustomTkinter para iniciar automações diversas.
Botões personalizáveis para executar funções definidas pelo usuário.
9. Captura de Coordenadas do Mouse
Script simples para identificar coordenadas x, y do mouse.
Útil para planejar cliques em automações PyAutoGUI.
Dependências
pyautogui
pyperclip
tkinter (ou customtkinter)
qrcode
shutil
os
time
datetime
random

Certifique-se de instalar as dependências via pip antes de rodar os scripts.

Observações
Todos os scripts foram testados em Windows 1920x1080 (alguns podem precisar ajustes de coordenadas para outras resoluções).
Alguns scripts interagem diretamente com navegadores e sistemas internos, portanto use com cuidado e sempre teste com dados de teste.
