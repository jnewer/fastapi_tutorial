#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydantic import BaseModel, ValidationError, field_validator


class Person(BaseModel):
    username: str
    password: str

    # '*' 在这里是匹配任意字段
    @field_validator("username", "password")
    def split(
        cls,
        v,
    ):
        """如果传参是字符串，根据逗号切割成list"""
        if isinstance(v, str):
            return v.split(",")
        return v


if __name__ == "__main__":
    try:
        user = Person(username="xiao,zhong", password="123456")
    except ValidationError as e:
        print(e.errors())
        print(e.json())
    else:
        print(user.username, user.password)
