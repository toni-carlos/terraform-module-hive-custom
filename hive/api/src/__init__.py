# import json
#from connection_hive import remove_newline_and_comment
# data = b'{"sql": drop table if exists ft7.employee2;\n\ncreate external table if not exists ft7.employee2 (\n    eid int,\n    ename string,\n    age int,\n    jobtype string,\n    storeid int,\n    storelocation string,\n    salary bigint,\n    yrsofexp int)\n    PARTITIONED BY\n        (`anomesdia` int COMMENT "Particao da tabela diaria")\n    ROW FORMAT SERDE\n        "org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe"\n    STORED AS INPUTFORMAT\n        "org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat"\n    OUTPUTFORMAT\n        "org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat";}'
# data_decode = data.decode("utf-8").replace("'", '\"')
#
# remove_newline_and_comment(data_decode)
# import re
# import json
# data =b'{ \'sql\': \'drop table if exists ft7.conta_poupanca_0233;\n\ncreate external table if not exists ft7.conta_poupanca_0233 (\n    id int,\n    data_inicio string,\n    data_fim string)\n    PARTITIONED BY\n        (`anomesdia` int COMMENT "Particao da tabela diariaa")\n    ROW FORMAT SERDE\n        "org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe"\n    STORED AS INPUTFORMAT\n        "org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat"\n    OUTPUTFORMAT\n        "org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat"\n    LOCATION \'hdfs://namenode:8020/user/hive/warehouse/ft7.db/conta_poupanca_0233\';\' }'
# d_p = remove_newline_and_comment(data.decode("utf-8"))
# remove_initial_character = re.sub(r'^(\s)*(\{)(\s)(\"sql\"\:)(\s)*(\")', "", d_p.replace("'", '\"').strip())
# remove_final_character = re.sub(r'((\s)*(\")(\s)*(\}))$', "", remove_initial_character)
#
# print(sql)