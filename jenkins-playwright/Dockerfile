FROM jenkins/jenkins:lts

USER root

# Install Python + system deps required by Playwright (Chromium)
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    wget \
    ca-certificates \
    libnss3 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libxss1 \
    libasound2 \
    libgbm1 \
    libdrm2 \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

# Make "python" available
RUN ln -s /usr/bin/python3 /usr/bin/python

USER jenkins
