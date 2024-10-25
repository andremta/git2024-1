FROM python:3.11-alpine
LABEL description="Webcounter"

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG REDIS_URL='localhost'
ENV REDIS_URL=${REDIS_URL}

ARG CI_COMMIT_SHORT_SHA='develop'
ENV CI_COMMIT_SHORT_SHA=${CI_COMMIT_SHORT_SHA}

EXPOSE 5000

RUN adduser -D user
USER user
WORKDIR /home/user
ENV PATH="/home/user/.local/bin:${PATH}"

COPY --chown=user:user requirements.txt requirements.txt
RUN pip install --user -r requirements.txt
COPY --chown=user:user . .

CMD ["python", "-m", "webcounter"]
