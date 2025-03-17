FROM ubuntu:latest

WORKDIR /app

COPY scripts/ ./scripts
COPY data/ ./data

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update \
    && apt-get install -y python3 \
    && apt install -y curl \
    && apt install -y texlive

COPY --link --from=ghcr.io/astral-sh/uv:0.4 /uv /usr/local/bin/uv

RUN mkdir ./artifacts
RUN cd scripts \
    && uv sync \
    && uv run main.py

RUN cd artifacts && pdflatex document.tex

