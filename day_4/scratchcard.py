import pandas as pd

def main():
    df = pd.read_table("input.txt", header=None, )
    df.info()

main()