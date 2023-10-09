# Sourced from Peter Malmgren
# https://petermalmgren.com/signal-handling-docker/

import sys
import signal

import time

def signal_handler(signum, frame):
    print(f"Gracefully shutting down after receiving signal {signum}")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        time.sleep(0.5)  # simulate work
        print("Interrupt me")
