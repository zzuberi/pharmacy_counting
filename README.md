# Table of Contents
1. [Instructions](README.md#instructions)
2. [Dependencies](README.md#dependencies)
3. [Note](README.md#note)

# Instructions
This code can be executed by running run.sh. The input file should be placed in the ./input/ folder. run.sh needs to be edited to have the input file name and the desired output filename in the following format:

    python ./src/pharmacy-counting.py ./input/<input_file> ./output/<output_file>
      
By default the input file is "itcont.txt" and the output file is "top-cost-drug.txt." The output file will be generated in the ./output/ folder.

# Dependencies
The following dependencies are used and must be installed for this code to run:
  1. sys
  2. csv
  
# Note
The instructions did not specify if decimal format was required for the total_cost field. In order to pass the test, if the final total_cost value is an integer it will be printed as an integer wihtout decimal points. If the total_cost value is a decimal number it will be printed with two decimal points.
