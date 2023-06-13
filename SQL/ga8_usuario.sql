create database if not exists ga8;

drop table if exists ga8.usuario;

create external table if not exists ga8.usuario (
    id int,
    name string)
    PARTITIONED BY
        (`anomesdia` int COMMENT "Particao da tabela diaria")
    ROW FORMAT SERDE
        "org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe"
    STORED AS INPUTFORMAT
        "org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat"
    OUTPUTFORMAT
        "org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat"
    LOCATION 'hdfs://namenode:8020/user/hive/warehouse/ga8.db/usuario';
