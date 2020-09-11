import json
import csv

DEFAULT_READ = "small_data.json"
DEFAULT_WRITE = "small_datas.csv"


def convert_file(read, write):
    try:
        file_read = open(read, "r")
        file_write = open(write, "w")
        file_read.seek(0)
        info = []
        lines = json.load(file_read)
        write = csv.writer(file_write, delimiter=";")
        for line in lines:
            info = [line["stationId"], line["name"]]
            write.writerow(info)

        print("Conversion succeeded.")
        file_write.close()
        file_read.close()
    except (OSError, csv.Error, json.JSONDecodeError):
        print("There was an error in handling the file.")


def main():
    read = input("Enter the name of the input file: ")
    if read == "":
        read = DEFAULT_READ

    write = input("Enter the name of the output file: ")
    if write == "":
        write = DEFAULT_WRITE
    print()

    convert_file(read, write)


main()