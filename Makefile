build:
	sudo docker build --tag=LogStreamer .
remove:
	sudo docker stop stream-server && sudo docker remove stream-server
run:
	sudo docker run --rm -it --name stream-server -p 8080:8080 LogStreamer
launch-client:
	sudo docker exec stream-server /bin/sh -c "python multi_client_streaming.py"
launch-client:
	sudo docker exec stream-server /bin/sh -c "python -m app.utils.log_maker 300"