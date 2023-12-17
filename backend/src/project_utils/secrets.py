""" NOTE - This is a copy of the secrets.py file from the noria project. 
In production, we'll utilise the noria_utils package from CodeArtifact. 
This is a temporary solution."""

import json
import os
import pathlib as pl
import warnings
from typing import Literal

# import aws_secretsmanager_caching
# from mypy_boto3_secretsmanager.client import SecretsManagerClient


def get_secret(
    key: str,
    environment: Literal["dev", "stage", "prod"] = None,
    creds_file: pl.Path = pl.Path(__file__).parent / "secrets.json",
    region_name: str = None,
) -> dict:
    """Retrieves a secret by key, depending on the current environment.

    If the environment is "dev", then the secret is retrieved from a local file.
    This file must be JSON.

    By default, the environment variable ENVIRONMENT is used.
    If this is not set, then the environment is assumed to be "dev".

    If environment is set, then the environment variable is ignored.
    """

    if region_name is None:
        region_name = os.getenv("AWS_DEFAULT_REGION", None)
        if region_name is None:
            warnings.warn(
                "AWS Region not set. Defaulting to 'ap-southeast-2'.", UserWarning
            )
            region_name = "ap-southeast-2"

    # Instantiate a Secrets Manager client with cache
    # secret_manager: SecretsManagerClient = boto3.client(
    #     "secretsmanager", region_name=region_name
    # )
    # cache_config = aws_secretsmanager_caching.SecretCacheConfig()
    # cache = aws_secretsmanager_caching.SecretCache(
    #     config=cache_config, client=secret_manager
    # )

    if environment is None:
        environment = os.getenv("ENVIRONMENT", None)  # type: ignore
        # we handle alt cases below.
        if environment is None:
            warnings.warn("Environment not set. Defaulting to 'dev'.", UserWarning)
            environment = "dev"

    assert environment in ["dev", "stage", "prod"]

    if environment:  # == "dev":
        assert creds_file is not None
        # Fetch from credentials.json
        with open(creds_file, "r") as f:
            secrets: dict = json.load(f)
        return secrets.get(key, None)

    # elif environment == "stage" or environment == "prod":
    #     # Fetch from AWS Secrets Manager
    #     try:
    #         secret = cache.get_secret_string(key)
    #         if secret:
    #             logging.info(f"Retrieved secret {key} from cache.")

    #             return json.loads(secret)
    #     except Exception as e:
    #         print(e)
