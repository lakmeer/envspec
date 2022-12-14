# EnvSpec

## How to EnvSpec

#### 1. Write your environment requirements in `.envspec` and commit it
``` sh
# Non-sensitive values can be stored in version control
APP_NAME=EnvSpec Demo
NOT_A_SECRET="I don't care if this gets leaked"

# Blank keys will capture values from the environment
ENVIRONMENT=
SECRET_API_KEY=
```

#### 2. Fill in sensitive values in your CI pipeline config
![Example of CI config screen](https://github.com/lakmeer/envspec/blob/master/docs/ci-config.png?raw=true)

#### 3. Run `make-env` in your pipeline
If any variables were not found, you will see clear, concise errors in your logs.

#### 4. Deploy the generated `.env` file
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
  - No installer
  - Runs anywhere


## Details

### Options

#### `-s`, `--spec` - default `.envspec`

- Choose a different specfile; eg: you may want to keep it out of project root

#### `-o`, `--outfile` - default `.env`

- Choose a different name or location for the output dotenv file

#### `-v`, `--verbosity` - default `1`

- 0: Minimal - Only show me errors
- 1: Default - shows confirmation for each required variable
- 2: Copious - tell me every little thing

#### `-n`, `--no-colors`

- Disable ANSI formatting in stdout


### Notes on default behaviours

#### Overwriting

- Environment-provided values will overwrite spec-provided values.
  - eg: If the spec contains `ENV=dev`, but the pipeline defines `ENV` as `staging`, the output
    `.env` will contain `ENV="staging"`
- Any existing `.env` file in the working dir is backed up to `.env.bak`
- Any existing `.env.bak` is out of luck.

#### Formatting

- Output values are always double-quoted
- Comments and blank lines are preserved
- Extraneous whitespace is removed: `KEY = value` will become `KEY="value"`

#### Errors

- EnvSpec will halt in the following cases:
  - If the `.envspec` file is missing
  - If a required variable is not found in the environment
  - If a line doesn't contain a `=`, but is also not a comment
- Keys with explicit blank values, like `INTENTIONALLY_BLANK=""`, will not cause an error if not
  found in the environment.
- If EnvSpec stops due to an error, the WIP envfile will be deleted.

## Todo

- Verbose output flag
- Flags to disable automatic formatting and quoting
- More unit tests
  - Missing key `=value` should throw
  - Flag options
    - Help text terminates with 0
    - Colors
    - Output levels
    - Loading alternate specfiles
    - Writing alternate envfiles
- Do string processing without `sed`

If you would like to help with any of the above items, please send a pull request.

## Contributing

Please send pull requests to add new unit tests or request optional features.
This project's goals include having as few feature flags as possible, so it better be a good idea.


## License

This software is published under the [Unlicense](http://unlicense.org). No rights reserved, but no
warranty either. See [LICENSE](https://raw.githubusercontent.com/lakmeer/envspec/master/LICENSE) for
terms.

