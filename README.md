# flux-edge

Edge service (target: NVIDIA Jetson Orin Nano, TensorRT FP16) that turns camera / mmWave input into **anonymised zone metadata** for the AI DJ logic.

## Privacy by design
- Frames are processed in volatile memory and **discarded immediately**; nothing raw is stored or transmitted.
- Only aggregates leave the device, e.g. `{"zone":"A","density":0.85,"energy":0.6}`.
- Designed with biometric-privacy regimes (e.g. Saudi PDPL) in mind. **Get legal review before deploying**: whether aggregate-only processing falls outside a given law's scope is a legal question, not something this code can guarantee.

## Pipeline
camera/mmWave → density map (multi-column CNN / YOLO) → zone aggregation → OSC/MQTT → flux-host AI DJ controller
