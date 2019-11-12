from invoke import task, run

@task
def test(c):
    c.run("pytest -q tests/test_*.py")
    c.run("pytest --cov=./") 
