import nox


@nox.session(python=["3.9"])
def tests(session):
    session.install("-r", "requirements.txt")
    session.run("pytest", "-v", "--cov=csv_functions", "--cov-report=term-missing")
    session.run("coverage", "report", "-m", external=True)

# nox -s tests
