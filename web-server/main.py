import store
from fastapi import FastAPI

def run():
    store.get_categories()


if __name__ == '__main__':
    run()