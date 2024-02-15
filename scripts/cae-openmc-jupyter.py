#! /bin/env python
from argparse import ArgumentParser
from subprocess import run

parser = ArgumentParser(description='Run OpenMC Jupyter Notebook')
parser.add_argument('username', metavar='USERNAME', type=str,
                    help='CAE username')
parser.add_argument('-c', '--cae-machine', metavar='CAE_MACHINE_NAME', type=str,
                    help='CAE machine name', default='best-tux.cae.wisc.edu')
parser.add_argument('-d', '--working-directory', metavar='WORKING_DIRECTORY', type=str,
                    help='working directory for the jupyter notebook', default='.')
parser.add_argument('-p','--port', metavar='PORT', type=int,
                    help='port for the jupyter notebook', default=8888)

args = parser.parse_args()

cmd_template = 'ssh -t -L {}:localhost:{} {}@{} "/cae/apps/bin/cae-openmc \'jupyter-notebook --notebook-dir={} --no-browser --port={}\'"'

cmd = cmd_template.format(args.port,
                          args.port,
                          args.username,
                          args.cae_machine,
                          args.working_directory,
                          args.port)

print(f'Running command: {cmd}')

run(cmd, shell=True)
