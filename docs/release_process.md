## Manual Release Process

1. Build the production docker image locally (see [Docker](docs/docker.md))
2. Push the image to docker hub (see [Docker](docs/docker.md))
3. Log into [Azure Portal](portal.azure.com)
4. Locate the webhook url for the Web App in Deployment Center > Webhook URL
5. Hit that url with a post request, making sure to escape the dollar sign like below

```shell
curl -dH -X POST "https://\$<deployment_username>:<deployment_password>@<webapp_name>.scm.azurewebsites.net/docker/hook"
```