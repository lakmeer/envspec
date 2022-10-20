# A reasonable example envfile with typical features
#
# We will test this by simulating the staging deployment pipeline.
# We expect to fill in blanks, and also:
#  - overwrite the default url with the staging url

# Basic stuff
ENVIRONMENT=
APP_NAME=Next Big Thing
APP_URL=https://nextbigthing.io
ADMIN_PATH=admin

# Database Configuration
DB_SERVER=localhost
DB_DATABASE="nbt"
DB_PORT=3306
DB_USER=staging_user
DB_PASS=

# AWS stuff
AWS_KEY="AKIAIOSFODNN7EXAMPLE"
AWS_SECRET=

