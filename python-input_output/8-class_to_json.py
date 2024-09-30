#!/usr/bin/python3
import json


def class_to_json(obj):
    """return the dictionary description"""
    return obj.__dict__
