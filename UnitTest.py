import unittest
import thumbnail
import json
import os
from PIL import Image


class Test(unittest.TestCase):

    def test_open_json(self):
        read = thumbnail.ReadJson()
        expected = open("C:\\Users\\Dan DCC\\PycharmProjects\\thumbnails\\unzipped\\manifest.json")

        actual = read.open_json("C:\\Users\\Dan DCC\\PycharmProjects\\thumbnails\\unzipped")
        expected = str(expected)
        actual = str(actual)

        self.assertEquals(expected, actual)

    def test_read_json(self):
        test_thumbnail = thumbnail.ReadJson()
        opened = open("C:\\Users\\Dan DCC\\PycharmProjects\\thumbnails\\unzipped\\manifest.json")
        expected = opened.read()
        opened.close()

        opened = open("C:\\Users\\Dan DCC\\PycharmProjects\\thumbnails\\unzipped\\manifest.json")
        actual = test_thumbnail.read_json(opened)
        opened.close()
        actual = str(actual)
        expected = str(expected)

        self.assertEqual(expected, actual)

    def test_decode_json(self):
        read = thumbnail.ReadJson()
        opened = open("C:\\Users\\Dan DCC\\PycharmProjects\\thumbnails\\unzipped\\manifest.json")
        raw = opened.read()
        expected = json.loads(raw)

        actual = read.decode_json(raw)

        self.assertDictEqual(expected, actual)

    def test_make_dir(self):
        read = thumbnail.ReadJson()
        temp_path = "C:\\Users\\Dan DCC\\PycharmProjects\\thumbnails\\new_folder"

        read.ensure_dir(temp_path)

        self.assertTrue(self, os.path.exists(temp_path))

    def test_dir_names(self):
        read = thumbnail.ReadJson()
        temp_path = "C:\\Users\\Dan DCC\\documents\\test\\crap\\UJHBG~`!@#$%^&()\\"

        read.ensure_dir(temp_path)

        self.assertTrue(self, os.path.exists(temp_path))

    def test_make_thumb(self):
        thumb_test = thumbnail.ReadJson()
        path = "C:\\Users\\Dan DCC\\Documents\\test\\"
        old_image = "daily_paint__671___panda_quickie_by_cryptid_creations-d802cri.jpg"

        actual = thumb_test.make_thumb(old_image, path)

        self.assertTrue(self, os.path.exists(actual))

    def test_unzipper(self):
        zip_test = thumbnail.ReadJson()
        path = "C:\\Users\\Dan DCC\\Documents\\test\\"
        dest = "GODMODE\\"
        zip = "GODMODE.zip"

        zip_test.unzip_file(path, dest, zip)

        self.assertTrue(self, os.path.exists(path + dest))

    def test_copy_makethumb(self):
        image_gen_test = thumbnail.ReadJson()
        path = "C:\\Users\\Dan DCC\\Documents\\test\\"
        dest = "destination\\"
        test_image = "procyon.jpg"
        test_thumb = "procyon_thumbnail.danIsCool.jpg"

        expct = path + dest + test_image
        expct2 = path + dest + test_thumb
        image_gen_test.copy_make_thumb(path + test_image, path + dest, test_image)

        self.assertTrue(self, os.path.exists(expct) and os.path.exists(expct2))



if __name__ == "__main__":
    unittest.main()