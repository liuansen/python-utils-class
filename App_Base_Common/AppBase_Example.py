# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals

import sys

from AppBase import AppBase, try_except


class Example(AppBase):
    app_name = 'for example'

    def __init__(self):
        super(Example, self).__init__()

    def add_arguments(self, parser):
        parser.add_argument(
            "-example",
            "--example",
            dest="example",
            help="example",
            type=int
        )

    @try_except("for_example")
    def handle(self, options):
        example = options.get('example')
        print example


if __name__ == '__main__':
    op = Example()
    op.run(sys.argv)
    # cmd: python AppBase_Example -example 1
