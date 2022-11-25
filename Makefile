build:
	sudo docker build --tag=log-streamer .
run:
	sudo docker run --rm -it --name stream-server -p 8080:8080 log-streamer
launch-client:
	sudo docker exec -it stream-server bash -c "python multi_client_streaming.py"
launch-logger:
	sudo docker exec -it stream-server bash -c "python -m app.utils.log_maker 300"
stop:
	sudo docker stop stream-server