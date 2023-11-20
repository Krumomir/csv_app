import nox


@nox.session(python=["3.9"])
def tests(session):
    # Install dependencies
    session.install("-r", "requirements.txt")

    # Run tests with cProfile
    session.run(
        "python",
        "-m",
        "cProfile",
        "-o",
        "test_profile.prof",  # Output file for cProfile results
        "-m",
        "pytest",
        "test_csv.py",  # Replace with the actual test file
        "-v",
        "--cov=csv_functions",
        "--cov-report=term-missing",
        external=True,
    )

    # Display cProfile statistics
    session.run("python", "-m", "pstats", "test_profile.prof")

    # Generate a call graph using gprof2dot and Graphviz (optional)
    session.install("gprof2dot", "graphviz")
    session.run("gprof2dot", "-f", "pstats", "test_profile.prof", "-o", "call_graph.dot", external=True)
    session.run("dot", "-Tpng", "-o", "call_graph.png", "call_graph.dot", external=True)


@nox.session
def benchmarks(session):
    session.install("-r", "requirements.txt", "pytest", "pytest-benchmark")
    session.run("pytest", "--benchmark-only", "test_csv.py")
