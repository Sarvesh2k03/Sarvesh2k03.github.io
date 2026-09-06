# sarvesh2k03.github.io

Personal AI portfolio — live at **https://sarvesh2k03.github.io**

A single static page, no build step. Three shipped projects, each with a live demo,
public source, and the measured numbers behind it:

| Project | What it answers | Demo | Source |
|---|---|---|---|
| **Grounded** | Can a RAG system admit it doesn't know? | [demo](https://grounded-rag-nr9dmpzrh79njaamznujzv.streamlit.app/) | [repo](https://github.com/Sarvesh2k03/grounded-rag) |
| **Triage Desk** | What happens to the app when the model times out? | [demo](https://triage-desk-te0v.onrender.com/) | [repo](https://github.com/Sarvesh2k03/triage-desk) |
| **NYC 311 AI ETL** | Can an LLM sit inside a nightly pipeline without being a single point of failure? | [demo](https://nyc311-ai-etl.streamlit.app/) | [repo](https://github.com/Sarvesh2k03/nyc311-ai-etl) |

## Structure

```
index.html        the whole page — styles inline, no dependencies
assets/           portrait
```

Type is Archivo (display) and Instrument Sans / JetBrains Mono, loaded from Google Fonts.
Light and dark themes are both defined; the page follows the visitor's system setting.

## Editing

Open `index.html` and edit. There is no toolchain — a push to `main` publishes.
