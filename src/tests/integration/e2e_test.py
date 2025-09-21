#!/usr/bin/env python3

from subprocess import Popen
from src.server import client


def test_server_client():
    server = Popen('../../../server/server.py')
    sum = client.get_sum(3, 4)
    assert (sum == 7)
