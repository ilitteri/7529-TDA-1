# ¿Cómo ejecutar el programa?

## Para instalar las dependencias

```bash
pipenv install
```

## Para ejecutar el programa

```bash
pip3 src/main.py <ruta a un archivo>
```

## Para ejecutar los tests
```bash
pytest tests/test_depositos.py
```

## Para ejecutar el coverage
```bash
coverage run -m --source='src' pytest test/test_doorbell.py
```

## Para ejecutar el coverage y los tests al mismo tiempo y generar un reporte de coverage tanto web como .txt
```bash
coverage run -m --source='src' pytest test/test_doorbell.py && coverage report -m > coverage.txt && coverage html
```
