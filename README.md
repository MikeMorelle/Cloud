# Cloud Roadmap – Edge AI & Raspberry Pi Cluster
_____________________________________________________________________
# Ungefährer Zeitplan:
1. Grundlagen & Setup (Woche 1-3)
2. Cluster & PXE Boot (Woche 4-6)
3. HPC & MPI (Woche 7-9)
4. AI Training & Backend (Woche 10-11)
5. Frontened & Integration (Woche 12-13)
6. Testing, Doku & Demo (Woche 14)
______________________________________________________________________
# Milestone 1: Sensor Nodes & Object Detection Setup 

Ziel: Funktionsfähige Edge-Knoten mit Kamera & AI-Inferenz

Aufgaben:
- Setup von Raspberry Pi 5 + Kamera (AI Camera / Kamera + AI HAT+)
- Installation OS (Raspberry Pi OS oder Ubuntu)
- Deployment von Objekterkennung (YOLO / TensorFlow)
- PXE-Boot für Raspberry Pi 3 Worker über Master (Pi 4/5)

Verantwortlich:
Algis
Michael

# Milestone 2: Performance Benchmark (HPL)

Ziel: Messung der Clusterleistung in GFLOPS

Aufgaben:
- Installation & Konfiguration von High Performance LINPACK
- Benchmarking einzelner Nodes vs. Cluster

Verantwortlich:
Chris

# Milestone 3: MPI Cluster Setup & Skalierung

Ziel: Aufbau eines verteilten Clusters

Aufgaben:
- Installation von MPI
- Master-Worker Architektur (Pi 5 → Pi 3)
- Skalierungstests + Analyse
- Demonstration von Amdahl & Gustafson (MPI)

Verantwortlich:
Algis

# Milestone 4: Amdahl & Gustafson (Non-MPI)

Ziel: Vergleich paralleler Skalierung ohne MPI

Aufgaben:
- Nutzung eines Task-Distributors
- Analyse von Speedup & Effizienz

Verantwortlich:
Algis

# Milestone 5: Monitoring & Observability

Ziel: Systemüberwachung aller Nodes

Aufgaben:
- Setup von Prometheus + Grafana oder CheckMK
- Metriken: CPU, RAM, Temperatur, Netzwerk

Verantwortlich:
Hichan, Ibrahim, Deniz, Mohammed

# Milestone 6: Datensammlung & Modelltraining

Ziel: Eigenes Object Detection Modell

Aufgaben:
- Datensammlung (Kamera / Cloud wie Roboflow)
- Labeling & Training (YOLOv8 / TensorFlowLite)

Verantwortlich:
Michael 

# Milestone 7: Backend & Storage Cluster

Ziel: Skalierbares Backend-System

Aufgaben:
- Deployment via Docker + k3s
- Storage: Ceph / MinIO / SeaweedFS
- API (REST / MQTT)

Verantwortlich:
Algis, Hichan, Ibrahim, Mohammed

# Milestone 8: Frontend Entwicklung

Ziel: Visualisierung & Dashboard

Aufgaben:
- UI mit React oder Vue.js
- Anzeige von Logs, Events, Bildern

Verantwortlich:
Algis, Ibrahim, Chris, Mohammed

# Milestone 9: Telegram Bot Integration

Ziel: Echtzeit-Benachrichtigungen

Aufgaben:
- Bot-Setup über Telegram
- Alerts für System & Detection Events

Verantwortlich:
Hichan, Chris, Mohammed
