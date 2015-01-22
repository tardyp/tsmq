#!/bin/env python
# -*- coding: utf-8 -*-

import glob
import json

from yamltypes import yaml
from yamltypes import YamlConfig
from flask import render_template
from flask import Flask

application = app = Flask(__name__, static_url_path='', template_folder='static')

"""I load the spec, and serve it to the js ui
"""
messages = dict(YamlConfig("spec/messages.yaml", yamltypes_dirs=["spec/types"]))
types = {}
for fn in glob.glob("spec/types/*.type.yaml"):
    with open(fn) as y:
        types.update(yaml.load(y))


@application.route('/')
def root():
    return render_template('index.html', messages=json.dumps(messages), types=json.dumps(types))


if __name__ == '__main__':
    app.run(debug=True)
