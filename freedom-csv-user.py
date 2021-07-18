import requests
import csv
import os
from ez_address_parser import AddressParser

def format_name(name):
    # given a string of a name convert to nice name:
    # Input: Branden Walter
    # Output: brandenw

    name_list = name.lower().split(' ')
    firstname = name_list[0]
    
    if len(name_list) > 1:

        lastinitial = name_list[1][0]
        if lastinitial.isalpha():
            pass
        else:
            lastinitial = 'fc'
    else:
        lastinitial = 'fc'

    firstname = firstname.replace("'", '')
    result = str(firstname) + str(lastinitial)
    return result


def first_name_gen(name):
    # given a name list give only the first name string
    # Input: Branden Walter
    # Output: Branden

    name = name.split(' ')
    result = str(name[0])
    return result

def email_gen(name):
    # given a string of a username, return a valid dummy email:
    # Input: brandenw
    # Output: brandenw@noemail.ca

    email = str(name) + "@noemail.ca"
    return email 

def format_adress(address):
    # Impliment a Streetnumber, streetname etc. join to a string and append it to a list and return it.
    ap = AddressParser()

    results = []
    streetnum = ''
    city = ''
    postalcode = ''
    Province = ''

    result = ap.parse(address)
    for token, label in result:
        #print(token + label)
        if label == 'StreetNumber':
            streetnum = streetnum + token + ' '
        if label == 'StreetName':
            streetnum = streetnum + token + ' '
        if label == 'StreetType':
            streetnum = streetnum + token + ' '
        if label == 'Municipality':
            city = city + token + ' '
        if label == 'PostalCode':
            postalcode = postalcode + token + ' '
        if label == 'Province':
            Province = Province + token + ' '

    results.append(streetnum)
    results.append(city)
    results.append(postalcode)
    results.append(Province)

    return results
    
        
def main():

    # - Read in old csv 
    # - clean all data in every second row in file
    # - Write new clean data to a new csv file

    final_list = []
    
    with open("users-csv1.csv", 'r') as file_in:
        reader = csv.reader(file_in)
        first_header = next(reader)
        second_header = next(reader)
        count = 0
        counter = 0
        for row in reader:
            if count %2 == 0:
                new_row = [x.replace('America/Dawson_Creek', '') for x in row]
                username = format_name(new_row[0])
                print(new_row[0])
                first_name = first_name_gen(new_row[0])
                email = email_gen(username)
                address = format_adress(new_row[1])
                password = 'freedom_pass'
                final_list.append(username)
                final_list.append(first_name)
                final_list.append(email)
                final_list.append(password)
                final_list = final_list + address
                with open('csv-user-final.csv', 'a', newline='') as file_out:
                    writer = csv.writer(file_out)
                    writer.writerow(final_list)
                    final_list.clear()
                counter = counter +1
            else:
                pass
            count = count + 1
        
if __name__ == '__main__':
    main()