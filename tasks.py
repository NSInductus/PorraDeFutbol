from invoke import task, run

@task
def test():
    run("pytest -q tests/test_*.py")
