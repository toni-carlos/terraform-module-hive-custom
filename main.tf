module "tbl_conta_corrente"{
    source = "./modules/hive"
    path_file = var.sql_tabela_ft7_conta_corrente
}

module "tbl_conta_poupanca"{
    source = "./modules/hive"
    path_file = var.sql_tabela_ft7_conta_poupanca
}

module "tbl_ga8_usuario"{
    source = "./modules/hive"
    path_file = var.sql_tabela_ga8_usuario
}