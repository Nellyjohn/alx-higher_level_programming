#!/usr/bin/python3
def raise_exception():
    try:
        raise Exception("Exception raised")
    except Exception:
        print("Exception raised")
