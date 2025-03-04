
from download import download_images
from iterator import  Iterator
from createannotation import create_annotation
from parsing import parsing_arguments



def main():
    arguments = parsing_arguments()
    try:
        download_images(arguments.keyword, arguments.save_path)
        create_annotation(arguments.annotation, arguments.save_path)
        iterator = Iterator(arguments.annotation)
        for abs_path, rel_path in iterator:
            print(f"Image: Absulate Path {abs_path}, Relative Path: {rel_path}")
    except Exception as e:
        print(f"Error: {e} ")


if __name__ == "__main__":
    main()