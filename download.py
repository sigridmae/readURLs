#!/usr/bin/env python3

import requests
import csv
import click


@click.command()
@click.option('-i', required=True)
def download(i):
    with open(i) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for lines in csv_reader:
            click.echo('HTML "' + lines[0] + '"')
            click.echo(requests.get(lines[1]).text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    download()

