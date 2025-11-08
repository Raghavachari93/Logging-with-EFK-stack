FROM fluent/fluentd:v1.14-debian-1

USER root

# install elasticsearch plugin and other useful plugins
RUN gem install fluent-plugin-elasticsearch -v 5.0.5 --no-document || gem install fluent-plugin-elasticsearch --no-document

# copy config
COPY fluent.conf /fluentd/etc/fluent.conf

USER fluent

