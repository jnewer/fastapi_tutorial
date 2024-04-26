#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Union, Optional, List

from pydantic import BaseModel, field_validator


def share_logic_auth(name: str) -> str:
    if name == "xiaozhong":
        return "通过"
    return "不通过"


class Base(BaseModel):
    name: str
    # 定义校验器
    _validator_name = field_validator("name")(share_logic_auth)


class Yuser(Base):
    pass


class Xuser(Base):
    pass


yuser = Yuser(name='xiaozhong')
print("xiaozhong:名字",yuser.name)
xuser = Xuser(name='_xiao')
print("_xiao:名字",xuser.name)

