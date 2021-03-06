#!/usr/bin/env python
# coding: utf-8

import click
import os
import sys
import configparser as cp


@click.command()
@click.option('-f', '--file', default=lambda: os.environ.get('INI_CONFIG', None), envvar="INI_CONFIG", help='path to .ini file')
@click.option('-d', '--default', type=click.Path(exists=True), default=lambda: os.environ.get('INI_CONFIG_DEFAULT', None), envvar="INI_CONFIG_DEFAULT", help='path to default .ini file')
@click.option('-e', '--error', default=False, is_flag=True)
@click.argument('section', required=True)
@click.argument('param', required=True)
def get(file, default, error, section, param):
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
    if not config.has_option(section, param):
        if error:
            print("section or param not found")
            sys.exit(5)
        else:
            sys.exit()
    print(config.get(section, param))


if __name__ == '__main__':
    get()