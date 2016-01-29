#!/usr/bin/python

import argparse


def update_entry(name, addr=None, file='/etc/avahi/hosts'):

    with open(file, 'r+') as fp:
        lines = [x for x in fp.readlines() if not name + '\n' in x]

        if addr:
            lines.append("{0} {1}\n".format(addr, name))

        fp.seek(0)
        for line in lines:
            fp.write(line)


def rm_entry(name, file='/etc/avahi/hosts'):
    update_entry(name, None, file)


def parse_args():
    prog = 'mdns'
    parser = argparse.ArgumentParser(
        prog=prog,
        description="Add an mdns (Zeroconf) entry for a .local address",
        epilog="After entry, the host can be accessed by e.g. "
               "'ping <host>.local'",
    )

    parser.add_argument(
        'host',
        help="host name (e.g. \"comitup.local\")",
    )

    parser.add_argument(
        'address',
        help="IP address",
    )

    args = parser.parse_args()

    return args


def main():
    args = parse_args()

    host = args.host
    if '.local' not in host:
        host += ".local"

    update_entry(args.host, args.address)


if __name__ == '__main__':
    main()