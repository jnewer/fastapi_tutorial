"""Containers module."""

import logging.config
import sqlite3

from dependency_injector import containers, providers

from .wxclient import WxClient
from example import services


class Container(containers.DeclarativeContainer):

    config = providers.Configuration(ini_files=["config.ini"])

    logging = providers.Resource(
        logging.config.fileConfig,
        fname="logging.ini",
    )

    # Gateways

    database_client = providers.Singleton(
        sqlite3.connect,
        config.database.dsn,
    )

    wx_client = providers.Singleton(
        WxClient,
        service_name="wx_client",
        aws_access_key_id=config.aws.access_key_id,
        aws_secret_access_key=config.aws.secret_access_key,
    )

    # Services

    user_service = providers.Factory(
        services.UserService,
        db=database_client,
    )

    auth_service = providers.Factory(
        services.AuthService,
        db=database_client,
        token_ttl=config.auth.token_ttl.as_int(),
    )

    photo_service = providers.Factory(
        services.PhotoService,
        db=database_client,
        wxc=wx_client,
    )
