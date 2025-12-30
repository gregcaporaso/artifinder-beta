#!/usr/bin/env python

import warnings
from pathlib import Path

import typer

from qiime2.sdk.result import Result
from qiime2.core.archive.provenance_lib import ProvDAG

from artifinder import __version__ as artifinder_version


warnings.filterwarnings('ignore')
app = typer.Typer()


@app.command()
def find(search_dir: str,
         target_result_fp: str,
         verbose: bool = True,
         include_targets: bool = False,
         include_results_not_found: bool = False):
    """
    Find and identify rachis `Results` used in generating the target `Result`.
    """
    target_result_fp = Path(target_result_fp)
    search_dir = Path(search_dir)

    if not search_dir.exists():
        raise FileNotFoundError("Search directory does not exist: "
                                f"{search_dir}")

    if not target_result_fp.exists():
        raise FileNotFoundError("Target Result file path does not exist: "
                                f"{target_result_fp}")


    # Store target information in a dict, which will easily allow for
    # supporting multiple input targets some day.
    target_uuids = {}
    target = Result.peek(target_result_fp)
    target_uuids[target.uuid] = (target.type, target_result_fp.absolute())
    print('Target Result(s):')
    for target_uuid, (type, path) in target_uuids.items():
        print(f' * {target_uuid}')
        print(f'  * {type}')
        print(f'  * {path}')
        print('')

    if verbose:
        print("Parsing target's provenance...")
    prov_dag = ProvDAG(target_result_fp, verbose=verbose)

    if verbose:
        print("Scanning search path for .qza and .qzv files...")
    fps = list(search_dir.glob('**/*.qz[av]'))

    if verbose:
        print(f"Found {len(fps)} Results in search directory. "
              "Will now cross-reference those against the target's "
              "provenance.")

    observed_uuids = {
        Result.peek(fp).uuid: fp.absolute() for fp in fps}

    found_uuids = {}
    unfound_uuids = {}

    for n in prov_dag.collapsed_view:
        node_data = prov_dag.get_node_data(n)
        node_type = node_data.type
        if n in observed_uuids:
            found_uuids[n] = (node_type, observed_uuids[n])
        else:
            unfound_uuids[n] = node_type

    print('Results found:')
    for uuid, (type, path) in found_uuids.items():
        if uuid in target_uuids and not include_targets:
            continue
        print(f' * {uuid}')
        print(f'  * {type}')
        print(f'  * {path}')
        print('')

    if include_results_not_found:
        print('\nResults not found:')
        for uuid, type in unfound_uuids.items():
            print(f' * {uuid}')
            print(f'  * {type}')
            print('')

    print('')
    print('---')
    print(f'Run with `artifinder` version: {artifinder_version}')
