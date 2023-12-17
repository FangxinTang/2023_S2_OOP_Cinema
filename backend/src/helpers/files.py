"""Module-specific non-business logic (e.g. utility functions)."""

import pathlib as pl
import uuid
from typing import TYPE_CHECKING

import boto3

from .. import constants as global_constants

if TYPE_CHECKING:
    from mypy_boto3_s3.client import S3Client
else:
    S3Client = object


LOCAL_ROOT = pl.Path().cwd() / "_LOCAL_STORAGE"


def _get_file_path(path: str | pl.Path) -> pl.Path:
    file_path = path

    if type(path) == str:
        file_path = pl.Path(path)
    return file_path  # type: pl.Path


def write_file(file: bytes, path: str | pl.Path, bucket: str = "noria-public") -> bool:
    """Writes a file to the server.

    Args:
        file (UploadFile): The file to write.
        file_path: The path to write the file to.

    Returns:
        success (bool): Whether the file was written successfully."""
    file_path = _get_file_path(path)

    if global_constants.ENVIRONMENT == "dev":
        # Write to local filesystem
        file_path = LOCAL_ROOT / pl.Path(path)
        try:
            file_path.parent.mkdir(parents=True, exist_ok=True)

            with open(file_path, "wb") as f:
                f.write(file)

            return True
        except IOError:  # TODO find correct errors. OSError is a placeholder.
            return False

    elif global_constants.ENVIRONMENT in ("stage", "prod"):
        # Write to S3
        client: S3Client = boto3.client("s3")
        try:
            client.upload_fileobj(
                Fileobj=file, Bucket=bucket, Key=path
            )  # TODO: async callbacks (websocket) for progress bar
            return True
        except:  # TODO find correct errors
            return False


def create_file(file: bytes, path: pl.Path) -> tuple[str, pl.Path]:
    """Create a file on the server and return the path to the file.

    Args:
        file (UploadFile): The file to create.
        path: The directory to write the file to. Will be appended to root path.
        id: Optional file id, otherwise one will be generated.

    Returns: (file_id, filepath):
        file_id (str): The file_id of the file.
        filepath (PosixPath): The path to the file.
    """
    file_path = _get_file_path(path)

    file_id = str(id) or str(
        uuid.uuid4()
    )  # TODO: #18 Assess need for file ids and implement if required
    write_file(file, file_path)

    return (file_id, file_path)


def check_file_exists(path: str | pl.Path, bucket: str = "noria-public") -> bool:
    """Checks if a file exists on the server.

    Args:
        path: The path to the file.
        bucket: The S3 bucket to check."""

    file_path = _get_file_path(path)

    if global_constants.ENVIRONMENT == "dev":
        # Check local filesystem
        return (LOCAL_ROOT / file_path).exists()
    elif global_constants.ENVIRONMENT in ("stage", "prod"):
        # Check S3
        client: S3Client = boto3.client("s3")
        try:
            client.head_object(Bucket=bucket, Key=str(file_path))
            return True
        except:  # TODO - narrow except
            return False


def get_file(path: str | pl.Path, bucket: str = "noria-public") -> bytes | None:
    """Finds the file on the server, using the file_id param.

    Args:
        file_id (str): The file_id to search for.

    Returns:
        filepath (PosixPath): The path to the file."""

    # TODO validate against user
    file_path = _get_file_path(path)

    if global_constants.ENVIRONMENT == "dev":
        # Read from local filesystem
        file_path = LOCAL_ROOT / file_path
        try:
            with open(file_path, "rb") as f:
                return f.read()
        except IOError:
            return None
    elif global_constants.ENVIRONMENT in ("stage", "prod"):
        # Read from S3
        client: S3Client = boto3.client("s3")
        try:
            response = client.get_object(Bucket=bucket, Key=str(file_path))
            return response["Body"].read()
        except Exception as e:  # TODO - narrow exception
            return None
