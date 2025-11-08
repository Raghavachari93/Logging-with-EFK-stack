# Project 40 — Logging with EFK stack (Elasticsearch / Fluentd / Kibana)

A local demo of centralized logging using the EFK stack:
- **Elasticsearch** (store & index logs)
- **Fluentd** (collect logs and forward to Elasticsearch)
- **Kibana** (visualize logs)
- A small Flask demo app that emits logs to stdout (collected via Fluentd)

> This setup is intended for **local development / learning**. For production use read the "Production notes" section below.

---

## Repo layout

