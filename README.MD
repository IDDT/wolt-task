# wolt-task
Successful take home assignment for ML engineer position at Wolt. This project implements API that etimates delivery time in realtime given the necessary inputs in the form of a POST request.


### Endpoints
#### POST
Handle incoming JSON data to predict delivery duration.
Request: JSON with the following keys:
    - time_received (str): The timestamp of the order.
    - is_retail (bool): Whether the order is retail.
    - venue_id (str): Identifier of the venue.
Response: JSON response with the following keys:
    - result (int | None): Predicted delivery duration in minutes or None if not available.
    - error (None | str): An error message or None if no errors occurred.
```bash
curl http://127.0.0.1:8000/ -H 'Content-type: application/json' -d '{"venue_id": "8a61b8c", "time_received": "2017-01-25 03:16:07.938113", "is_retail": true}'
>> {"result": 21.162891387939453, "error": null}
```


### Running locally with Docker
```bash
docker build --tag wolt-task-test --target test . # run unit tests
docker-compose up # launch the whole stack
```


### Running on localhost
```bash
# Python version is specified in .python-version file. Used with pyenv.
python3 -m venv .venv && source .venv/bin/activate
pip3 install -U pip wheel && pip3 install -r requirements.txt
python3 -m unittest tests # run unit tests
REDIS_URI=redis://127.0.0.1:6379 uvicorn src:app --reload
```


### Configuration and environment variables.
Please see `src/config.py`.


### Architecture
```
├── Dockerfile
├── README.MD
├── docker-compose.yml
├── misc
│   ├── model_artifact.json    # model artifact bundled into the container
│   └── venue_preparation.csv  # venue_id to average preparation time mapping
├── requirements.txt
├── src
│   ├── __init__.py     # API start up code
│   ├── config.py       # centralized config
│   ├── database.py     # adapter for the database
│   ├── model.py        # adapter for the model
│   ├── routes          # API routes
│   │   ├── system.py   # system routes
│   │   └── v1.py       # application routes
│   └── types.py        # shared types
└── tests               # unit tests
```


### Areas for improvement
- Database has to be replaced with a real connection, which also needs to be async not to block the main thread.
- Caching requires a key strategy when the Redis cluster is shared across many services in the company.
- Use supervisord to launch N instances of the server per container for better resource utilization.
- Emit metrics for monitoring & alerts. Probably with something like statsd + Grafana.
- Cache expiration time should be brought up for discussion with involved parties.
- Implement graceful shutdown to close database and redis connections.
- Handle missing venue_id, probably with a default value.
