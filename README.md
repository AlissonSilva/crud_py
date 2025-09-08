1 - Adicionar a chave secreta 

python -c "import secrets; print(secrets.token_urlsafe(32))"

Isso irá gerar uma string aleatória, por exemplo:

'k2vQ9z2Qw3J6n8bX1p4rT7sV0yZ5uC6dE3fH9gL2mN8qR1tU'

Adicionar o código secreto gerado no .env em SECRET_KEY: k2vQ...

2 - Executar o arquivo requirements.txt

pip install -r requirements.txt

3 - Executar o projeto

 uvicorn main:app --reload
