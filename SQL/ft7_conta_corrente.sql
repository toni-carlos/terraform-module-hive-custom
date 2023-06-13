create database if not exists ft7;

drop table if exists ft7.conta_corrente;

create external table if not exists ft7.conta_corrente_001 (
    id int,
    ename string)
    PARTITIONED BY
        (`anomesdia` int COMMENT "Particao da tabela diaria")
    ROW FORMAT SERDE
        "org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe"
    STORED AS INPUTFORMAT
        "org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat"
    OUTPUTFORMAT
        "org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat"
    LOCATION 'hdfs://namenode:8020/user/hive/warehouse/ft7.db/conta_corrente_001';
