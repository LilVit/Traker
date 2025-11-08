# ============================================================

# &nbsp;                RASTREADOR DE MOVIMENTO 

# ============================================================

# 

# Projeto em Python para rastrear o movimento de um corpo (ex: bolinha metálica)

# em um vídeo experimental de lançamento balístico. 

# O código usa o algoritmo CSRT do OpenCV para seguir o objeto 

# e gera gráficos de trajetória, distância e velocidade, além de exportar

# os dados para planilha (CSV).

# 

# ------------------------------------------------------------

# 📁 ESTRUTURA DO PROJETO

# ------------------------------------------------------------

# 

# traker/

# │

# ├── video.mp4                    → vídeo do experimento

# ├── tracker\_ballistic.py         → código principal

# ├── requirements.txt             → dependências necessárias

# ├── resultados/                  → gráficos e CSV gerados automaticamente

# └── README.txt                   → este arquivo de instruções

# 

# ------------------------------------------------------------

# ⚙️ INSTALAÇÃO

# ------------------------------------------------------------

# 

# 1\. Verifique se o Python 3.8 ou superior está instalado.

# &nbsp;  Comando para checar:

# &nbsp;      python --version

# 

# 2\. Instale todas as dependências do projeto executando:

# &nbsp;      pip install -r requirements.txt

# 

# &nbsp;  Este comando instalará:

# &nbsp;      • opencv-contrib-python  (biblioteca principal de visão computacional)

# &nbsp;      • matplotlib              (plotagem de gráficos)

# &nbsp;      • pandas                  (exportação de dados)

# &nbsp;      • scipy                   (suavização dos dados)

# 

# ------------------------------------------------------------

# ▶️ COMO USAR

# ------------------------------------------------------------

# 

# 1\. Coloque o vídeo (ex: video.mp4) dentro da pasta "traker/". (OBS: A pasta deve ser exatamente esse nome) 

# 

# 2\. Execute o script principal no terminal:

# &nbsp;      python tracker\_ballistic.py

# 

# 3\. Quando o vídeo abrir:

# &nbsp;      • Selecione a bolinha metálica com o mouse (arraste um retângulo)

# &nbsp;      • Pressione ENTER para iniciar o rastreamento

# &nbsp;      • O rastreamento será mostrado em tempo real

# 

# 4\. Pressione ESC a qualquer momento para encerrar.

# 

# ------------------------------------------------------------

# 📊 SAÍDAS GERADAS

# ------------------------------------------------------------

# 

# Após o término do rastreamento, os arquivos serão salvos na pasta:

# &nbsp;   traker/resultados/

# 

# Arquivos gerados:

# &nbsp;   • analise\_trajetoria.png  → gráfico da trajetória e distância × tempo

# &nbsp;   • trajetoria\_bolinha.csv  → dados (frame, tempo, x, y, distância, velocidade)

# 

# ------------------------------------------------------------

# ⚠️ POSSÍVEIS ERROS E SOLUÇÕES

# ------------------------------------------------------------

# 

# • ERRO: AttributeError: module 'cv2' has no attribute 'TrackerCSRT\_create'

# &nbsp; SOLUÇÃO:

# &nbsp;      pip uninstall opencv-python -y

# &nbsp;      pip install opencv-contrib-python

# 

# • ERRO: "Não foi possível abrir o vídeo."

# &nbsp; SOLUÇÃO:

# &nbsp;      Verifique se o nome do arquivo é exatamente "video.mp4" 

# &nbsp;      e se ele está na mesma pasta que o script principal.

# 

# ------------------------------------------------------------

# 💡 DICA EXTRA

# ------------------------------------------------------------

# 

# Se quiser gerar gráficos com unidades físicas (m/s e m), 

# adicione uma calibração no código indicando a escala:

# &nbsp;  Exemplo: "100 pixels equivalem a 0,10 metros"

# 

# Assim, o programa converterá automaticamente as distâncias 

# para metros e calculará velocidades e aceleração realistas.

# 

# ------------------------------------------------------------

# 📘 AUTOR E LICENÇA

# ------------------------------------------------------------

# 

# Autor: Vitor Eduardo

# Data: Novembro de 2025 (Ultima atualização) 

# Licença: Uso livre para fins educacionais e científicos

# ============================================================



