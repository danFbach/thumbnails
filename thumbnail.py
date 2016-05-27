import shutil
from PIL import Image
import zipfile
import json
import re
import os


class ReadJson(object):

    @staticmethod
    def ensure_dir(f):
        if not os.path.exists(f):
            os.makedirs(f)
            os.chmod(f, 0o777)

    @staticmethod
    def make_thumb(old_image, path):
        size_100 = (100, 100)
        image1 = Image.open(path + old_image)
        fn, fext = os.path.splitext(old_image)
        image1.thumbnail(size_100)
        image1.save(path + "\\{}_thumbnail.danIsCool{}".format(fn, fext))
        return path + "\\{}_thumbnail.danIsCool{}" .format(fn, fext)

    @staticmethod
    def open_json(path):
        return open(path + "\\manifest.json", "r")

    @staticmethod
    def read_json(raw):
        return raw.read()

    @staticmethod
    def decode_json(data):
        return json.loads(data)

    @staticmethod
    def get_next(path, old_theme, a_dict):
            ReadJson.ensure_dir(path + "\\" + old_theme)
            return a_dict[old_theme]

    @staticmethod
    def create_folders(path, destination, themes):
        for theme in themes:
            ReadJson.step_up(theme, path, themes)
        shutil.make_archive(destination, 'zip', path)
        print("Operation Complete.")

    @staticmethod
    def step_up(next_theme, path, themes):
        a_theme = ReadJson.get_next(path, next_theme, themes)
        for image in a_theme:
            ReadJson.next_step(next_theme, image, path, a_theme)

    @staticmethod
    def next_step(this_theme, image, path, a_dict):
        m = re.search('([\s\w\W]+\.(?:jpg|jpeg))', image)
        if m is None:
            ReadJson.step_up(image, path + "\\" + this_theme, a_dict)
        else:
            ReadJson.copy_make_thumb(the_path + "\\" + image, path + "\\" + this_theme + "\\", image)

    @staticmethod
    def copy_make_thumb(path1, path2, image):
            shutil.copyfile(path1, path2 + image)
            ReadJson.make_thumb(image, path2)

    @staticmethod
    def get_zip_location(zip_path):
        intended_path = input("Enter .zip file to extract: ")
        if os.path.exists(zip_path + "\\" + intended_path):
            return intended_path
        else:
            print("There is no .zip folder at that location.")
            return ReadJson.get_zip_location(zip_path)

    @staticmethod
    def get_destination():
        return input("Enter destination folder(C:/Users/.../folder/'new folder'): ")

    @staticmethod
    def unzip_file(path, destination, the_zip):
        ex = zipfile.ZipFile(path + "\\" + the_zip)
        full_path = path + "\\" + destination + "\\"
        ex.extractall(full_path)
        return destination

"""short_path = os.getcwd()
zip_location = ReadJson.get_zip_location(short_path)
dest = ReadJson.get_destination()
the_destination = ReadJson.unzip_file(short_path, dest, zip_location)
the_path = short_path + "\\" + the_destination
raw_json = ReadJson.open_json(the_path)
json_data = ReadJson.read_json(raw_json)
manifest_dict = ReadJson.decode_json(json_data)
main_theme = manifest_dict['directory_structure']['image_themes']
ReadJson.create_folders(the_path, the_destination, main_theme)"""