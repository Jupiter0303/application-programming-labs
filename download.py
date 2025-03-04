import os


from icrawler.builtin import GoogleImageCrawler


def download_images(keyword:str, path:str)->None:
    """
    Поиск картинок по ключевому слову и их сохранение
    :param keyword: ключевое слово для поиска
    :param path: директория для сохранения найденных картинок
    :return: ничего не возвращает
    """
    if not os.path.exists(path):
        os.makedirs(path)

    google_crawler = GoogleImageCrawler(storage={'root_dir':path})
    google_crawler.crawl(keyword=keyword,max_num= 10)




