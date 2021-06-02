FROM envoyproxy/envoy:v1.18-latest
RUN apt-get update && apt-get -q install -y \
    curl
COPY ./envoy.yaml /etc/envoy.yaml
RUN chmod go+r /etc/envoy.yaml
CMD ["/usr/local/bin/envoy", "-c", "/etc/envoy.yaml", "--service-cluster", "gateway"]
© 2021 GitHub, Inc.