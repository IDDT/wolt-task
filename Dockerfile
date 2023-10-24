# syntax=docker/dockerfile:1.2


# build
FROM python:3.11.1-slim-bullseye AS build
WORKDIR /build
COPY requirements.txt .
RUN pip3 wheel --wheel-dir=/wheels -r requirements.txt


# test
FROM python:3.11.1-slim-bullseye AS test
WORKDIR /app
COPY . .
COPY --from=build /wheels /wheels
RUN pip3 install \
  --no-index \
  --no-cache-dir \
  --find-links=/wheels \
  -r requirements.txt
RUN ["python3", "-m", "unittest", "-v", "tests"]


# prod
FROM python:3.11.1-slim-bullseye AS prod
WORKDIR /app
COPY . .
COPY --from=build /wheels /wheels
RUN pip3 install \
  --no-index \
  --no-cache-dir \
  --find-links=/wheels \
  -r requirements.txt
EXPOSE 8000/tcp
CMD [ "uvicorn", \
  "--host", "0.0.0.0", \
  "--port", "8000" \
]
