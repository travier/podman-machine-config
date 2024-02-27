# Podman Machine OS Config

WIP

## Steps for fedora-coreos-config Git submodule update

To be automated via a GitHub Action:
- Bump submodule
- Create / delete symlinks to manifest-lock.overrides.arch.yaml files
- Run process-manifest-lock.py to update filtered lock-files

## TODO

- Add manifest-lock.overrides.arch.yaml support to process-manifest-lock.py
