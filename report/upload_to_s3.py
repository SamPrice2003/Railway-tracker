"""Script which uploads a generated PDF report to the S3 bucket."""

from os import environ as ENV, _Environ

from dotenv import load_dotenv
from boto3 import client


def get_s3_client(config: _Environ) -> client:
    """Returns a live S3 client."""

    return client(
        "s3",
        aws_access_key_id=config["ACCESS_KEY_AWS"],
        aws_secret_access_key=config["SECRET_KEY_AWS"]
    )


def upload_to_s3(s3_client: client, filename: str, bucket_name: str, object_name: str) -> None:
    """Uploads a file to the S3 bucket."""

    s3_client.upload_file(filename, bucket_name, object_name)


if __name__ == "__main__":

    load_dotenv()
