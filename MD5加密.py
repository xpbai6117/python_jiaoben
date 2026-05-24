# coding:utf-8
# @Author:xb
# @Time: 2024/3/21 16:14
# @File:MD5加密.py
import hashlib
def get_data(date,music_id):
        s = [
                "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt",
                "appid=1014",
                f"clienttime={date}",
                "clientver=20000",
                "dfid=1txQjF11nqGw2Bu4s31ACHIK",
                f"encode_album_audio_id={music_id}",
                "mid=d883995a1c69e128c82c30da1a653671",
                "platid=4",
                "srcappid=2919",
                "token=",
                "userid=0",
                "uuid=d883995a1c69e128c82c30da1a653671",
                "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
            ]
        string = ''.join(s)
        MD5 = hashlib.md5()
        MD5.update(string.encode('utf-8'))
        signature = MD5.hexdigest()
        return signature