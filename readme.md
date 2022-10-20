# EnvSpec

## How to EnvSpec

### 1. Write your environment requirements in `.envspec` and commit it
``` sh
# Non-sensitive values can be stored in version control
APP_NAME=EnvSpec Demo
NOT_A_SECRET="I don't care if this gets leaked"

# Blank keys will capture values from the environment
ENVIRONMENT=
SECRET_API_KEY=
```

### 2. Fill in sensitive values in your CI pipeline config
![Example of CI config screen](https://github.com/lakmeer/envspec/blob/master/docs/ci-config.png?raw=true)

### 3. Run `make-env` in your pipeline
If any variables were not found, you will see clear, concise errors in your logs.

### 4. Deploy the generated `.env` file
``` sh
# Non-sensitive values can be stored in version control
APP_NAME="EnvSpec Demo"
NOT_A_SECRET="I don't care if this gets leaked"

# Blank keys will capture values from the environment
ENVIRONMENT="staging"
SECRET_API_KEY="2d803bd451c77c3c130a4dda46cf0b22"
```


## Basic AF

- No new syntax
  - You already know how it works
  - Comments and breaks will be preserved
  - Automatically quotes values and regularizes formatting
- It's a single bash script
  - Commit it to your repo
  - Runs anywhere
  - No installer
  - No external dependancies


## Contributing

Please send pull requests to add new unit tests or request optional features.
This project's goals include having as few feature flags as possible, so it better be a good idea.


## License

This software is published under the [Unlicense](http://unlicense.org). No rights reserved, but no
warranty either. See [LICENSE](https://githubusercontent.com/lakmeer/envspec/master/LICENSE) for
terms.

