# This spec is a sanitized version of a real envfile from a Craft CMS project.
# We will simulate deployment to the staging environment

# The environment Craft is currently running in (dev, staging, production, etc.)
ENVIRONMENT=

# The application ID used to to uniquely store session and cache data, mutex locks, and more
APP_ID="CraftCMS--fa70bc7a-0bdc-4eca-911b-6a19cf513ff8"

# The secure key Craft will use for hashing and encrypting data
SECURITY_KEY=

# Database Configuration
DB_DRIVER=mysql
DB_SERVER=mysql57
DB_PORT=3306
DB_DATABASE=awesome
DB_USER=awesome
DB_PASSWORD=
DB_SCHEMA=""

# System Basics
CP_TRIGGER=admin
SYSTEM_NAME="Awesome Application"
DEFAULT_SITE_URL="https://awesome.mystudio.io"

# Email settings
SYSTEM_EMAIL_ADDR="test@mystudio.io"
REPLY_TO_ADDR="noreply@mystudio.io"
SENDER_NAME="Awesome Application"
SMTP_HOST="smtp.postmarkapp.com"
SMTP_PORT="587"
SMTP_USERNAME=
SMTP_PASSWORD=

# DO Spaces
SPACES_API_KEY="505881NQ2X5CZX529Y6J"
SPACES_SECRET=
SPACES_ENDPOINT="https://sgp1.digitaloceanspaces.com"
SPACES_BASE_URL="https://awesome.sgp1.digitaloceanspaces.com/"
SPACES_REGION="sgp1"
SPACES_BUCKET="awesome"

# Recaptcha
RECAPTCHA_KEY=

# Stripe
STRIPE_KEY="pk_test_bxJuE0fpBxauHmThIvNnWtDt"
STRIPE_SECRET_KEY=
