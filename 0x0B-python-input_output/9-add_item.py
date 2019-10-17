#!/usr/bin/python3
"""
This module contains the script for task 9
"""
if __name__ == "__main__":
    import sys
    import os

    save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
    load_from_json_file = __import__(
        "8-load_from_json_file").load_from_json_file

    if os.path.exists("add_item.json"):
        args = load_from_json_file("add_item.json")
    else:
        args = []
    args += sys.argv[1:]
    save_to_json_file(args, "add_item.json")
