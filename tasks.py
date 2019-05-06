from invoke import task
import threading


@task
def fix(c, docs=False):
    c.run("autopep8 -ivr *.py")
    c.run("autopep8 -ivr web_gpio_tester/*.py")


@task
def lint(c, docs=False):
    c.run("flake8 --show-source web_gpio_tester/*.py")


@task
def build(c, docs=False):
    with c.cd("web_gpio_tester/views"):
        c.run("yarn build")


@task
def start(c, docs=False):
    def python_start():
        c.run("python web_gpio_tester/main.py", hide=True)

    def npm_start():
        with c.cd("web_gpio_tester/views"):
            c.run("yarn start", hide=True)
    thread_1 = threading.Thread(target=python_start)
    thread_2 = threading.Thread(target=npm_start)
    print("Starting the server... Enjoy!")
    thread_1.start()
    thread_2.start()
