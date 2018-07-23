# profamaster

## How to start server

`make run`

## Create dev environment

`make init`

## Install virtualenv

`make install`

## Run tests

`make test`

## Documentation

### Create systemd service

1. Edit `/lib/systemd/system/profamaster.service`
2. Reload systemd using command: `systemctl daemon-reload`
3. Enable auto start using command: `systemctl enable profamaster`

```
[Unit]
Description=Profamaster web server

[Service]
Type=simple
ExecStart=pipenv run python start.py
WorkDir=PATH_TO_PROFAMASTER

[Install]
WantedBy=multi-user.target
```

### Error codes

- 101 : unknown error
- 102 : unknown action
