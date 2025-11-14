<h1 align="center"> Traker — Análise Automatizada de Movimento</h1>

<p align="center">
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/python-3.10+-yellow?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/opencv-4.x-red?style=for-the-badge&logo=opencv">
</p>

---

<p align="center">
<img src="https://github.com/LilVit/Traker/blob/main/resultados/analise_trajetoria.png?raw=true" width="1000"> </div>
</p>

<p align="center"><i>Exemplo ilustrativo do rastreamento automático de um objeto.</i></p>

---

##  Sobre o Projeto

O **Traker** é uma ferramenta criada para **automatizar a extração de dados de movimento** a partir de vídeos.  
Ele identifica um objeto, acompanha sua trajetória e gera informações como:

- posição (x, y)  
- velocidade  
- aceleração  
- distância percorrida  

Tudo é exportado em **CSV**, junto com gráficos automáticos para análise visual.

---

##  Funcionalidades

-  Rastreamento automático em qualquer vídeo  
-  Geração de CSV com todos os dados  
-  Análises de velocidade, aceleração e trajetória  
-  Gráficos automáticos  
-  Conversão opcional de **pixels para metros**  
-  Processo rápido, padronizado e reproduzível  

---

##  Tecnologias Utilizadas

- **Python 3.10+**  
- **OpenCV**  
- **Pandas**  
- **NumPy**  
- **Matplotlib**

---

## 📁 Estrutura do Projeto

```bash
Traker/
│
├── tracker.py # Rastreamento e coleta dos dados
├── analise_velocidade.py # Análises complementares
├── resultados/ # Onde os CSVs e gráficos são salvos
│ └── dados.csv
├── video.mp4 # Seu vídeo a ser analisado
└── README.md
```

---

##  Requisitos

| Biblioteca   | Versão Recomendada |
|--------------|--------------------|
| Python       | 3.10+              |
| OpenCV       | 4.8+               |
| NumPy        | 1.26+              |
| Pandas       | 2.1+               |
| Matplotlib   | 3.8+               |

---

##  Instalação

###  Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/Traker.git
cd Traker

opencv-python
pandas
numpy
matplotlib
```

Instale as dependências

Crie um arquivo requirements.txt com:

```
opencv-python
pandas
numpy
matplotlib
```
e instale:

```
python tracker.py
```

Coloque o vídeo dentro da pasta do projeto e ajuste o nome do arquivo no script, caso necessário.

Execute:
```
python tracker.py
```

Contexto:

O Traker foi desenvolvido para simplificar análises experimentais de Física, reduzindo erros manuais e permitindo estudos mais profundos sobre movimento, velocidade e dinâmica.

Contribuições:

Contribuições são bem-vindas!
Abra uma issue ou envie um pull request.

<p align="center"> <b>Desenvolvido com ❤ por Vitor Eduardo</b> </p> 
