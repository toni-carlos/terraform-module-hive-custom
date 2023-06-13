from typing import List
import re
from pyhive import hive
import os


def remove_caracter(data: str) -> str:
    """Remove caracteres do payload

    :param data: dados do payload
    :return: sql passado no payload
    """

    data = data.replace("'", '\"')
    remove_initial_character = re.sub(r'^(\s)*(\{)(\s)(\"sql\"\:)(\s)*(\")', "", data)  # remove { "sql": "
    remove_final_character = re.sub(r'((\s)*(\")(\s)*(\}))$', "", remove_initial_character)  # remove " }
    return remove_final_character


def remove_newline_and_comment(query: str) -> str:
    """Remove caracter de nova linha e comentários

    :param query: sql  do tipo create, drop e alter
    :return: comandos sql concatenados na mesma linha
    """

    print(f"Removendo caracteres de nova linha e comentários!!: {query}")

    lines = []
    for line in query.splitlines():
        if line and not line.startswith("--"):
            lines.append(" " + line.strip())

    sql = "".join(lines)
    return sql


def split_command(query: str) -> List[str]:
    """ Substituir o caracter " por ' e separa os comandos sql

    :param query: query sql
    :return: lista de comandos sql
    """
    query = query.replace('"\\;"', "'\\;'")
    return [command.strip() for command in re.split(r";(?=(?:[^\']*\'[^\']*\')*[^\']*$)", query) if command]


class HiveServer:

    def __init__(self):
        self.conn = None
        self.user = os.getenv("USER_HIVE")
        self.password = os.getenv("PWD_HIVE")
        self.host = os.getenv("HOST_HIVESERVER")
        self.port = os.getenv("PORT_HIVESERVER")

    def __enter__(self):
        self.init_connection()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def init_connection(self):
        print("Iniciando conexão com o HiveServe")

        try:
            self.conn = hive.Connection(host=self.host, port=int(self.port), username=self.user, password=self.password, auth='CUSTOM')
            print("Conexão criada com sucesso :)")
        except Exception as e:
            msg = f"Erro ao criar a conexao com o Hive Server :( . {e}"
            print(msg)
            raise Exception(msg)

    def execute_command(self, query):
        try:
            with self.conn.cursor() as cur:
                for command in split_command(query):
                    cur.execute(command)
            print("Comandos executados com sucesso :)")
        except Exception as e:
            msg = f"Erro ao executar a query no HiveServer :( . {e}"
            print(msg)
            raise Exception(msg)
