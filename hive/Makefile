clean_all:
	@docker-compose down --rmi all

create_container:
	@docker-compose up -d

build_image_api:
	@docker build -t flask-api-hive-server:latest ./api/.