#!/usr/bin/env python3

import json
import sys
import yaml

def main() -> int:
    packages_to_filter = []
    with open('manifest.yaml', 'r', encoding='utf-8') as file:
        y = yaml.safe_load_all(file)
        for d in y:
            for r in d['repo-packages']:
                packages_to_filter = r['packages']
    # print(packages_to_filter)

    for arch in ['x86_64', 'aarch64']:
        with open(f'fedora-coreos-config/manifest-lock.{arch}.json', 'r', encoding='utf-8') as file:
            j = json.load(file)
            for p in j['packages'].copy():
                if j['packages'][p]['metadata']['sourcerpm'] in packages_to_filter:
                    j['packages'].pop(p, None)

        with open(f'manifest-lock.{arch}.json', 'w', encoding='utf-8') as file:
            json.dump(j, file, ensure_ascii=False, indent=2)
            file.write("\n")

    return 0

if __name__ == '__main__':
    sys.exit(main())
