# LogStreamer

#### Real-Time Server-Sent Events based log streaming server with multi-client support.

## Structure

```
├── app
│   ├── core
│   │   ├── event_generator.py # Generate server-sent events.
│   │   └── log_reader.py # Read log file and yield new lines.
│   ├── data # test data
│   │   ├── logs.log # Log file being streamed.
│   │   └── seed.log # seed for log generation.
│   ├── handlers # Handlers for log streaming API
│   │   └── log_handlers.py # send log update server events.
│   ├── utils
│   │   └── log_maker.py # Generate random logs.
│   ├── config.py # config for app (server, log, etc.)
│   └── main.py # server / entrypoint to app
├── client.sh # optional curl based streaming client
├── Dockerfile # dockerfile (duh)
├── Makefile # installation and run targets.
└── multi_client_streaming.py // streaming client
```

### API

| Route       | HTTP  | Description      | Headers                           |
|-------------|-------|------------------|-----------------------------------|
| **/stream** | `GET` | Start log stream | `Content-Type: text/event-stream` |

## Installation

1. `cd` into LogStreamer directory

   ```shell
   $ cd LogStreamer
   ```

2. Build the docker image (will need superuser privileges)

   ```shell
   $ make build # check image info by running `sudo docker images`
   ```
3. Start the streaming server
   ```shell
   $ make run # check container info by running `sudo docker ps`
   ```

Streaming server should start listening on `localhost:8080`

### How to start the Streaming Client

In a new terminal window

1. Start a client
   ```shell
   $ make launch-client
   ```

#### Nothing's Happening!

1. Start the log generator (In a new terminal window)
   ```shell
   $ make launch-logger # keep looking at the client window
   ```

#### Recap:

- [x] Launched a streaming server.
- [x] Launched a multithreaded streaming client (to simulate multiple clients).
- [x] Launched a random log generator.
- [x] Observed it in action.

#### Stop Server

1. Stop Logger by pressing `Ctrl + c` or Mac: `Cmd + c`
2. Stop Client by pressing `Ctrl + c` or Mac: `Cmd + c`
3. In an idle terminal window, run
    ```shell
    # note: this will stop AND remove the container
    $ make stop 
    ```