# fluentd/Dockerfile
# Use a recent fluent/fluentd image that ships with Ruby 3.x so modern gem deps install cleanly.
# If this exact tag isn't available in your registry, replace it with another recent fluent/fluentd tag.
FROM fluent/fluentd:v1.18-debian-1

# Run plugin installs and any needed build tools as root
USER root

# Install small set of build tools for native extensions and cleanup apt lists
RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential ca-certificates curl \
  && rm -rf /var/lib/apt/lists/*

# Optional: set GEM options to speed installs and avoid generating documentation
ENV GEM_HOME=/usr/local/bundle \
    GEM_PATH=/usr/local/bundle \
    BUNDLE_PATH=/usr/local/bundle \
    LANG=C.UTF-8 \
    FLUENTD_OPT=""

# Install Elasticsearch plugin (and any other plugins you want).
# You can pin a specific version (e.g. -v 5.3.0) if desired; leaving unpinned installs the latest compatible one.
RUN gem install fluent-plugin-elasticsearch --no-document

# (Optional) Install other useful plugins (uncomment if you want them)
# RUN gem install fluent-plugin-remote_syslog --no-document
# RUN gem install fluent-plugin-rewrite-tag-filter --no-document

# Copy the fluentd config into the image
COPY fluent.conf /fluentd/etc/fluent.conf

# Expose fluentd forward input port(s)
EXPOSE 24224 24224/udp

# Drop back to the fluent user (the official image uses user 'fluent')
USER fluent

# Use the image's default ENTRYPOINT/CMD that starts fluentd.
# (If you need to pass options, use the FLUENTD_OPT env var or override via docker run / compose.)

