# ============================================================
# 🧠 Análise de Velocidade Real (com calibração em metros)
# ============================================================
# Autor: Vitor Eduardo
# Data: 2025
#
# Este script lê o arquivo CSV gerado pelo rastreamento do movimento
# e converte as medidas de pixels para metros com base em uma calibração
# fornecida pelo usuário.
#
# Saídas:
#  - Gráfico da velocidade real (m/s) ao longo do tempo
#  - CSV atualizado com colunas em metros
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import os

# ------------------------------------------------------------
# 📂 Lendo o arquivo de trajetória
# ------------------------------------------------------------
print("📂 Lendo dados de trajetória...")

csv_path = os.path.join("resultados", "trajetoria_bolinha.csv")

if not os.path.exists(csv_path):
    raise FileNotFoundError("❌ O arquivo resultados/trajetoria_bolinha.csv não foi encontrado.")

df = pd.read_csv(csv_path)

# Conferindo colunas
colunas_esperadas = ["frame", "tempo (s)", "x (px)", "y (px)", "distancia acumulada (px)", "velocidade (px/s)"]
if not all(col in df.columns for col in colunas_esperadas):
    raise ValueError(f"❌ O CSV não contém as colunas esperadas: {colunas_esperadas}")

print("✅ Dados carregados com sucesso!")
print(df.head(), "\n")

# ------------------------------------------------------------
# 📏 Calibração de escala (pixels → metros)
# ------------------------------------------------------------
print("⚙️  Calibração da escala (necessária para converter px → m)")
print("👉 Informe um trecho conhecido no vídeo.")
print("   Exemplo: se uma régua de 0.20 m ocupa 150 pixels,")
print("   então você digita: 150  e depois  0.20\n")

px_medidos = float(input("Quantos pixels medem o comprimento conhecido? "))
comprimento_real_m = float(input("Qual o comprimento real (em metros)? "))

metro_por_pixel = comprimento_real_m / px_medidos
print(f"\n📏 1 pixel = {metro_por_pixel:.6f} metros")

# ------------------------------------------------------------
# 🧮 Conversão das colunas para unidades físicas
# ------------------------------------------------------------
df["x (m)"] = df["x (px)"] * metro_por_pixel
df["y (m)"] = df["y (px)"] * metro_por_pixel
df["distancia acumulada (m)"] = df["distancia acumulada (px)"] * metro_por_pixel
df["velocidade (m/s)"] = df["velocidade (px/s)"] * metro_por_pixel

# ------------------------------------------------------------
# 📊 Gráfico da velocidade real
# ------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.plot(df["tempo (s)"], df["velocidade (m/s)"], color="red", lw=2, label="Velocidade (m/s)")
plt.title("Velocidade Real do Corpo em Movimento")
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (m/s)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()

# Salvar gráfico
output_graph = os.path.join("resultados", "grafico_velocidade_m_s.png")
plt.savefig(output_graph, dpi=300)
plt.show()

print(f"\n✅ Gráfico salvo em: {output_graph}")

# ------------------------------------------------------------
# 💾 Salvando novo CSV com unidades físicas
# ------------------------------------------------------------
output_csv = os.path.join("resultados", "trajetoria_real.csv")
df.to_csv(output_csv, index=False)
print(f"✅ Novo CSV salvo em: {output_csv}")
print("\n✅ Análise concluída com sucesso!")
