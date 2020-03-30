"""명령행 인터페이스."""
import json

import click
import botocore

from featr.version import VERSION
from featr.util import set_log_verbosity, iter_profiles
from featr.build import start
# from featr.profile import check_profile, show_plan


@click.group()
@click.option('-v', '--verbose', count=True, help="Increase message verbosity.")
@click.pass_context
def main(ctx, verbose):
    ctx.ensure_object(dict)
    set_log_verbosity(verbose)


@main.command('profiles', help='List all profiles.')
def profiles():
    """모든 프로파일을 리스팅."""
    for prof in iter_profiles():
        print(prof)


@main.command(help="Run feature building")
@click.argument('PROFILE')
@click.option('-p', '--param', multiple=True,
              help="Override profile by parameter.")
def run(profile, param):
    start(profile, param)


# @main.command(help="Create cluster.")
# @click.argument('PROFILE')
# @click.option('-c', '--cluster', "name", help="Cluster name (Default: "
#               "Profile name).")
# @click.option('-p', '--param', multiple=True,
#               help="Override profile by parameter.")
# @click.option('-n', '--notebook', 'open_nb', is_flag=True, help="Open remote "
#               "notebook when cluster is ready.")
# @click.option('-d', '--dashboard', 'open_db', is_flag=True, help="Open remote "
#               "dashboard when cluster is ready.")
# def create(profile, name, param, open_nb, open_db):
#     """클러스터 생성."""
#     check_profile(profile)
#     pobj, clinfo = create_cluster(profile, name, param)
#     remote_nb = 'notebook' in clinfo
#     if name is None:
#         name = clinfo['name']
#     if remote_nb:
#         start_notebook(pobj, clinfo)
#     if 'type' in clinfo:
#         start_cluster(clinfo)
#     save_cluster_info(name, clinfo)
#     show_cluster(name)

#     if open_nb:
#         if remote_nb:
#             open_notebook(name)
#         else:
#             print("There is no remote notebook in the cluster.")

#     if open_db:
#         open_dashboard(name, False)


@main.command(help='Show featr version.')
def version():
    """버전을 출력."""
    print(VERSION)


if __name__ == '__main__':
    main()
