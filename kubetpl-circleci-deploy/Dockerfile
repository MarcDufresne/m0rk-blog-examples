FROM debian:stable-slim

ARG KUBECTL_VERSION=v1.11.2
ARG KUBETPL_VERSION=0.7.1

RUN apt update \
    && apt -y --no-install-recommends install \
        ca-certificates \
        curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$KUBECTL_VERSION/bin/linux/amd64/kubectl \
    && chmod +x kubectl \
    && mv kubectl /usr/local/bin/

RUN curl -o kubetpl \
        https://github.com/shyiko/kubetpl/releases/download/$KUBETPL_VERSION/kubetpl-$KUBETPL_VERSION-linux-amd64 \
    && chmod +x kubetpl \
    && mv kubetpl /usr/local/bin/
