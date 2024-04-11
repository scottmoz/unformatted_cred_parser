import csv
from pprint import pprint
from pathlib import Path


def main():
    known_creds_file_path = Path("/local_file_known_creds.csv")
    new_file_path = Path("/new_file.txt")

    new_creds_lines_list = list()
    # Open new file and search line by line
    with open(new_file_path, 'r') as new_file_f:
        # Iterate over each line in the new file
        new_creds_lines_list_tmp = new_file_f.readlines()
        # Copy the data out of the object into memory
        # The file doesn't need to be open to conduct operations
        for line in new_creds_lines_list_tmp:
            # Remove /n
            line = line.rstrip()
            new_creds_lines_list.append(line)

    known_creds_list_dict = list()
    with open(known_creds_file_path, 'r') as reset_creds_file_f:
        known_creds_list_dict_tmp = csv.DictReader(reset_creds_file_f)
        # Copy the data out of the object into memory
        # The file doesn't need to be open to conduct operations
        for line in known_creds_list_dict_tmp:
            known_creds_list_dict.append(line)

    known_email_new_passwd_list = list()
    known_email_known_passwd_list = list()
    ukwn_email_list = list()
    for known_cred_dict in known_creds_list_dict:
        for new_cred_line in new_creds_lines_list:
            if known_cred_dict["Email"] in new_cred_line and known_cred_dict["Password"] not in new_cred_line:
                # Email matches but password doesn't
                if new_cred_line not in known_email_new_passwd_list:
                    known_email_new_passwd_list.append(new_cred_line)
            elif known_cred_dict["Email"] in new_cred_line and known_cred_dict["Password"] in new_cred_line:
                # Email and password match
                if new_cred_line not in known_email_known_passwd_list:
                    known_email_known_passwd_list.append(new_cred_line)
            else:
                # Unknown email and unknown password
                if new_cred_line not in ukwn_email_list:
                    ukwn_email_list.append(new_cred_line)

    print("Known email & New Password")
    print(known_email_new_passwd_list)
    # print("Known email & Known Password")
    # print(known_email_known_passwd_list)
    print("Totally new creds")
    for line in ukwn_email_list:
        print(line)
      

if __name__ == "__main__":
    main()
