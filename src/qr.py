import sys
import qrcode


class QR():
    """QRコード作成"""
    def __init__(self, url, stem):
        """
        Args:
            url (str): QRコードを作成したいURL
            stem (str): 書き出し画像名の拡張子無し部分(ex. 'hoge.png'の'hoge')
        """
        self.url = url
        self.stem = stem

    def make_qrcode(self):
        """荒いQRコード
        pngで書き出す
        """
        img = qrcode.make(self.url)
        img.save(f'../img/{self.stem}.png')

    def make_qrcode2(self):
        """細かいQRコード
        *2.pngというファイル名で書き出す
        """
        qr = qrcode.QRCode(
            version=12,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(self.url)
        qr.make()
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f'../img/{self.stem}2.png')


def main(args):
    url = args[1]
    stem = args[2]
    qr = QR(url, stem)
    qr.make_qrcode()
    qr.make_qrcode2()


if __name__ == '__main__':
    """引数1: QRコードを作成したいURL
       引数2: QRコード画像名(書き出し画像名の拡張子無し部分)
    """
    main(sys.argv)
