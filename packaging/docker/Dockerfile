FROM node:20 AS prebuild

COPY decide /app/decide
COPY .git /app/.git
COPY package.json package-lock.json requirements.txt /app/
COPY packaging/docker/contents/prebuild.sh /prebuild.sh
WORKDIR /app

# Eliminar archivos no necesarios
RUN git clean -fxd

# Install dependencies
RUN chmod +x /prebuild.sh && /prebuild.sh

# Deploy built frontend to Django
FROM python:latest

# Set build arguments
ARG DJANGO_SUPERUSER_USERNAME=decide
ARG DJANGO_SUPERUSER_EMAIL=admin@decide.org
ARG DJANGO_SUPERUSER_PASSWORD=decide
# Set environment variables
ENV DJANGO_SUPERUSER_USERNAME=$DJANGO_SUPERUSER_USERNAME
ENV DJANGO_SUPERUSER_EMAIL=$DJANGO_SUPERUSER_EMAIL
ENV DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD
ENV DB_USE_SQLITE=1

COPY packaging/docker/contents /scripts
COPY --from=prebuild /app/ /app
RUN chmod +x /scripts/*.sh \
    && /scripts/postunpack.sh \
    && rm -rf .dockerenv /scripts/postunpack.sh

WORKDIR /app/decide

EXPOSE 80

ENTRYPOINT [ "/scripts/entrypoint.sh" ]
CMD [ "/scripts/run.sh" ]
LABEL org.opencontainers.image.source="https://github.com/us-ferferga/decide"
