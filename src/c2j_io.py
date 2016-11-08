import sys
import csv
import json
import codecs

def convert_to_json(input_filename, output_filename):
    """ reads csv from input_file and outputs json to output_file """

    with codecs.open(input_filename, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        try:
            json_data = []
            rows = []
            headers = next(readCSV)
            for row in readCSV:
                d = dict()
                for i, header in enumerate(headers):
                    d[header] = row[i]
                json_data.append(d)
        except (UnicodeDecodeError, UnicodeEncodeError):
            print >> sys.stderr, "CSV Format Error"
            pass        


    out_file = open(output_filename,"w")
    json.dump(json_data, out_file, indent=4)
    out_file.close()



if __name__ == "__main__":
    input_filename = raw_input('What is the name of your csv file?\n')
    output_filename = input_filename[:-4] + ".json" if input_filename.endswith('.csv') else input_filename + ".json"

    convert_to_json(input_filename, output_filename)
