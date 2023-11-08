# import sys
# import os
# sys.path.append(f'{os.getcwd()}/truss_saver')

from .truss_saver import truss
from .truss_saver.truss.docker import Docker
from .truss_saver.truss import cli


def save_model(model, model_name, python_dependencies=None, system_dependencies=None):
    tr = truss.create(model, model_name)
    from pprint import pprint as pp
    return pp({'config': tr.__dict__['_spec'].__dict__['_config'].__dict__})

def run_model_server(model_path, port=8080):
    container = cli.run_image(model_path, port=port)
    return container

def stop_model_server(container_id):
    Docker.client().stop(containers=container_id)


def active_model_server():
    Docker.client().containers.list()