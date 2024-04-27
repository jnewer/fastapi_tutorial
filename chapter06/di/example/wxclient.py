#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Optional


@dataclass
class WxClient:
    access_key_id: str
    secret_access_key: str
    service_name: Optional[str] = None
