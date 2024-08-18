from . import Home


def views():
    @Home.route("/")
    def index():
        return "Hello World!"

    return Home
