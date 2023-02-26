FROM python:3.9.13-slim

RUN mkdir allure-report
ADD browsers.json .
ADD browsers.json ./allure-report