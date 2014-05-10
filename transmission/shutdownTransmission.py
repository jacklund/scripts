#! /usr/bin/env python

import subprocess

import transmissionrpc
from transmissionrpc.error import TransmissionError


def main():
    all_done = True
    try:
        tc = transmissionrpc.Client('localhost', port=9091)
        for torrent in tc.get_torrents():
            if torrent.status == 'downloading':
                all_done = False
                break
        if all_done:
            subprocess.call(['osascript', '-e',
                             'tell application "Transmission" to quit'])
    except TransmissionError:
        pass

if __name__ == "__main__":
    main()
