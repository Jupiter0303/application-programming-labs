from parsing import parsing_arguments
from openfile import open_file
from countname import count_copy_name


def main():
    arguments = parsing_arguments()
    try:
        text = open_file(arguments.filename)
        print(count_copy_name(text,arguments.name))
    except Exception as e:
        print(f"Error: {e} ")


if __name__ == "__main__":
    main()