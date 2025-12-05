from subprocess import run, PIPE


def test_help_output():
    result = run(["python", "-m", "weatherwise", "-h"], stdout=PIPE, text=True)
    assert "WeatherWise" in result.stdout
