# ==============================================================
# 🎯 Rastreamento de corpo em movimento balístico (VS Code)
# ==============================================================

import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import savgol_filter
import os

# Caminhos
video_path = "video.mp4"
output_dir = "resultados"
os.makedirs(output_dir, exist_ok=True)

# Abre o vídeo
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise RuntimeError("❌ Não foi possível abrir o vídeo.")

fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"🎞️ FPS: {fps:.2f} | Frames: {frame_count}")

# Lê o primeiro frame
ok, frame = cap.read()
if not ok:
    raise RuntimeError("❌ Erro ao ler o primeiro frame!")

# Mostra o primeiro frame e pede para selecionar a bolinha
print("🖱️ Selecione a bolinha metálica e pressione ENTER.")
bbox = cv2.selectROI("Selecione a bolinha", frame, False)
cv2.destroyAllWindows()

# Inicializa o rastreador CSRT
tracker = cv2.TrackerCSRT_create()
ok = tracker.init(frame, bbox)

positions = []
frames_idx = []
frame_id = 0

# Loop principal de rastreamento
while True:
    ok, frame = cap.read()
    if not ok:
        break

    ok, bbox = tracker.update(frame)
    if ok:
        x, y, w, h = bbox
        cx, cy = int(x + w/2), int(y + h/2)
        positions.append((cx, cy))
        frames_idx.append(frame_id)

        # Desenha o retângulo
        cv2.rectangle(frame, (int(x), int(y)), (int(x+w), int(y+h)), (0,255,0), 2)
        cv2.circle(frame, (cx, cy), 3, (0,0,255), -1)
        cv2.putText(frame, f"Frame {frame_id}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow("Rastreamento", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC para sair
        break

    frame_id += 1

cap.release()
cv2.destroyAllWindows()

print(f"✅ Rastreamento concluído. {len(positions)} pontos coletados.")

# --------------------------------------------------
# Processa as coordenadas e suaviza
# --------------------------------------------------
xs = np.array([p[0] for p in positions])
ys = np.array([p[1] for p in positions])
times = np.array(frames_idx) / fps

# Suavização (Savitzky–Golay)
janela = 9 if len(xs) >= 9 else (len(xs)//2*2+1)
xs_suave = savgol_filter(xs, janela, polyorder=2)
ys_suave = savgol_filter(ys, janela, polyorder=2)

# Distância e velocidade
dist = np.sqrt(np.diff(xs_suave, prepend=xs_suave[0])**2 + np.diff(ys_suave, prepend=ys_suave[0])**2)
dist_acum = np.cumsum(dist)
vel = np.gradient(dist_acum, times)

# --------------------------------------------------
# Gráficos
# --------------------------------------------------
plt.figure(figsize=(14,5))

plt.subplot(1,2,1)
plt.plot(xs_suave, ys_suave, '-o', color='deeppink', markersize=3)
plt.gca().invert_yaxis()
plt.title("Trajetória da bolinha (suavizada)")
plt.xlabel("x (pixels)")
plt.ylabel("y (pixels)")
plt.grid(True, alpha=0.3)

plt.subplot(1,2,2)
plt.plot(times, dist_acum, '-k', linewidth=2)
plt.title("Distância percorrida × Tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("Distância (pixels)")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "analise_trajetoria.png"), dpi=300)
plt.show()

# --------------------------------------------------
# Exporta CSV
# --------------------------------------------------
df = pd.DataFrame({
    "frame": frames_idx,
    "tempo (s)": times,
    "x (px)": xs_suave,
    "y (px)": ys_suave,
    "distancia acumulada (px)": dist_acum,
    "velocidade (px/s)": vel
})
csv_path = os.path.join(output_dir, "trajetoria_bolinha.csv")
df.to_csv(csv_path, index=False)

print(f"📁 Arquivos salvos em: {os.path.abspath(output_dir)}")
print(" - analise_trajetoria.png")
print(" - trajetoria_bolinha.csv")
