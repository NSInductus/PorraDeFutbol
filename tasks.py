from invoke import task, run
@task
def install(c):
    print("Instalando paquetes...")
    c.run("pip install -r requirements.txt")
    print("Instalación finalizada.")


@task
def test(c):
    print("Ejecutando tests...")
    c.run("pytest -q tests/test_*.py")
    print("Ejecución de tests finalizada.")

@task
def coverage(c):
    print("Test de cobertura...")
    c.run("pytest --cov=Mercado --cov=Portfolio tests/")
    print("Test de cobertura finalizado.")
