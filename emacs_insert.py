import os
import pathlib
import datetime


def write_to_inbox(message: str) -> None:
    """
    write the message as a new heading to the org mode inbox (fleeting) file for later organization
    :param message: string message for new heading in inbox
    :return: None
    """
    # # define path to inbox.org (fleeting file_
    # org_home_fp_str = 'C:/Users/Daniel/home/emacs'
    #
    # org_home_fp = pathlib.Path(org_home_fp_str)
    # roam_fp = org_home_fp / 'roam'
    org_inbox_fn = 'inbox.org'

    # if using docker
    output_file = pathlib.Path("/app/data/" + org_inbox_fn)
    fp = output_file

    # get some dates for created property in emacs
    # Get the current date
    current_date = datetime.date.today()

    # Format the date as "yyyy-mm-dd"
    formatted_date = current_date.strftime("%Y-%m-%d")

    # Get the three-letter suffix of the day
    day_suffix = " " + current_date.strftime("%a")

    # define some constants - read from template someday? subject to change with template
    # changes in template will not be adjusted in this bit fo code
    message_prefix = '\n* '
    message_suffix = '\n:PROPERTIES:\n:CREATED: [' + formatted_date + day_suffix + ']\n:END:'

    with open(fp, 'a') as f:
        f.write(message_prefix + message + message_suffix)


def main():
    # test
    write_to_inbox('test')


if __name__ == '__main__':
    main()
