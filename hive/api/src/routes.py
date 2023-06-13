from flask import Blueprint, request, make_response, jsonify
from .connection_hive import remove_newline_and_comment, HiveServer, remove_caracter

execute_sql_blueprint = Blueprint(name="execute_sql", import_name=__name__)


@execute_sql_blueprint.route("", methods=["POST"])
def execute_sql():
    try:
        print("Chamada de API para executar o SQL")
        print("Dados de entrada: ")
        print(request.data)
        data = remove_newline_and_comment(request.data.decode("utf-8"))
        sql = remove_caracter(data)

        with HiveServer() as conn:
            conn.execute_command(sql)

        msg = {"code": 200, "status": "success", "message": "Comando executado com sucesso :)"}
        return make_response(jsonify(msg), 200)
    except Exception as e:
        msg = {"code": 500, "status": "error", "message": e.args[0]}
        return make_response(jsonify(msg), 500)


