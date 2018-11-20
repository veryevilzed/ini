#!/usr/bin/env python
# coding: utf-8

import click
import os
import sys
import configparser as cp


@click.command()
@click.option('-f', '--file', type=click.Path(exists=True), default=lambda: os.environ.get('INI_CONFIG', None), envvar="INI_CONFIG", help='path to .ini file')
@click.option('-d', '--default', type=click.Path(exists=True), default=lambda: os.environ.get('INI_CONFIG_DEFAULT', None), envvar="INI_CONFIG_DEFAULT", help='path to default .ini file')
@click.argument('section')
@click.argument('param')
def get(file, default, section, param):
    if not file and not default:
        print("file and default is empty")
        sys.exit(5)
    list = []
    if file:
        list += [file]
    if default:
        list += [default]

    config = cp.ConfigParser()
    config.read(list)
    print(config.get("section", "value1"))
    print(config.get("section", "value2"))


if __name__ == '__main__':
    get()