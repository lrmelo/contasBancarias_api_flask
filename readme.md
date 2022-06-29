# readme

## Segue a instalação das dependências

```bash
python3 -m pip install flask
python3 -m pip install requests
python3 -m pip install flask_api
```

## Segue os comandos para rodar os serviços

Em um terminal

```bash
FLASK_APP=contaService.py flask run
```

Em um segundo terminal

```bash
FLASK_APP=contaAcoes.py flask run --port8000
```

<aside>
💡 A documentação da API está na collection do postman, na aba Documentation de cada requisição.

</aside>