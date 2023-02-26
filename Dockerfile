FROM python:3.9.13-slim

COPY . .
RUN mkdir allure-report
ADD browsers.json ./allure-report