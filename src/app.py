from configs.cadastro import Cadastro


def app():
    teste = Cadastro()
    teste.cadastrarMeta(2,200)
    teste.cadastrarConsumo(400)


if __name__ == "__main__":
    app()