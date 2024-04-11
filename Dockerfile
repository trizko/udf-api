FROM python:3.10-alpine

RUN adduser -D user
USER user

COPY --chown=user:user . /home/user/app

WORKDIR /home/user/app

RUN pip install --user -r requirements.txt

CMD ["python", "main.py"]