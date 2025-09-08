python -c "import secrets; print(secrets.token_urlsafe(32))"

Isso irá gerar uma string aleatória, por exemplo:

'k2vQ9z2Qw3J6n8bX1p4rT7sV0yZ5uC6dE3fH9gL2mN8qR1tU'

Adicionar o código secreto gerado no .env em SECRET_KEY: k2vQ...

 uvicorn main:app --reload
