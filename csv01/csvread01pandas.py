#!/usr/bin/python3
import pandas

def main():

    superdf = pandas.read_csv("superbirthday.csv")

    print(f"Column names are {', '.join(superdf)}")

    orient = 'records' prevents to_dict() from using the index value
    print(superdf.to_dict(orient='records'))

    for row in superdf.to_dict(orient='records'):
        print(f"\t{row['name']} aka {row['heroname']}, was born in {row['birthday month']}.")

    print(f"Total lines processed {superdf.shape[0]}")

if __name__ == "__main__":
    main()

