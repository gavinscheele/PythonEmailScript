#!/usr/bin/python
import email_parser
import mysql_executer
import mysql_generator
import os
import sys
import getpass
import mysql.connector


# scrapes .edu emails out of each lines and saves them to the db. Logs errors to console.
def process_file(fn, hostname, username, password, db_name, table_name, column_name):
    input_file = open(fn, "r")
    readable_input = input_file.readlines()
    email_output_file = open("email_list_output.txt", "w")
    line_number = 0

    for line in readable_input:
        try:
            email_output_file.write(email_parser.text_parser(line) + "\n")
        except ValueError as e:
            base_filename = fn.split("/")
            base_filename = base_filename[1]
            print("----------")
            print("ERROR in file \"" + base_filename + "\"")
            print("Email address not found on line: " + str(line_number))
            print(line.rstrip("\n"))
            print("----------")

        line_number += 1

    input_file.close()
    email_output_file.close()
    try:
        mysql_statement = mysql_generator.generate_mysql(fn, table_name, column_name)
    except EOFError as e:
        print(e)
    else:
        try:
            mysql_executer.execute_query(mysql_statement, hostname, username, password, db_name)
        except mysql.connector.Error as e:
            print("Something went wrong: {}".format(e))
            print("Check your credentials.")
            clean_up()
            sys.exit()

    # remove intermediate output file
    if os.path.isfile("email_list_output.txt"):
        os.remove("email_list_output.txt")


# creates email output and error files for runtime use
def create_output_files():
    intermediate_output_fn = "email_list_output.txt"

    if not os.path.isfile(intermediate_output_fn):
        open(intermediate_output_fn, 'a').close()


def clean_up():
    intermediate_output_fn = "email_list_output.txt"

    if os.path.isfile(intermediate_output_fn):
        os.remove(intermediate_output_fn)


# driver function
def main():
    arguments = sys.argv[1:]
    file_input_directory = "place_input_files_here"

    print("Please enter db connection credentials")
    hostname = raw_input("hostname: ")
    username = raw_input("username: ")
    password = getpass.getpass("password: ")
    db_name = raw_input("database name: ")
    table_name = raw_input("table name: ")
    column_name = raw_input("column name: ")
    # create files in directory for intermediate output and to list errors
    create_output_files()

    num_files_processed = 0
    # for each file in the place_input_files_here directory, parse out emails and add them to the db
    for fn in os.listdir(file_input_directory):

        if os.path.exists(os.path.join(file_input_directory, fn)):
            num_files_processed += 1
            process_file(file_input_directory + "/" + fn, hostname, username, password, db_name, table_name, column_name)

    print(str(num_files_processed) + " files processed")


main()


