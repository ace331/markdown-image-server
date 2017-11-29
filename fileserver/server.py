import os
import random
import string
import json
import time
import logging

import tornado.ioloop
import tornado.web

file_root = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'files')

class PingHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps({
            "Pong": int(time.time()),
        }))


class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        ret = {'result': 'ok'}
        file_metas = self.request.files.get('file', None)

        if not file_metas:
            ret['result'] = 'invalid args'
            return ret
        else:
            for meta in file_metas:
                dirname = time.strftime('%Y%m', time.localtime(time.time()))
                upload_path = os.path.join(file_root, dirname)
                if not os.path.exists(upload_path):
                    os.makedirs(upload_path)
                ext = (meta['filename'] or "").split('.')[-1]
                filename = "{}_{}".format(int(time.time() * 1000), ''.join(random.sample(string.ascii_uppercase + string.digits, 8)))
                if ext:
                    filename = ".".join([filename, ext])

                file_path = os.path.join(upload_path, filename)
                with open(file_path, 'wb') as upload_file:
                    upload_file.write(meta['body'])
                url = "http://localhost:8080/static/{}/{}".format(dirname, filename)
                ret["url"] = url
                ret["markdown"] = "![]({})".format(url)
        self.write(json.dumps(ret))


application = tornado.web.Application([
    (r"/ping", PingHandler),
    (r"/upload", UploadHandler),
], static_path=file_root )

if __name__ == "__main__":
    application.listen(8080)
    print("file server start, listening at port 8080")
    tornado.ioloop.IOLoop.instance().start()
