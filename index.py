import tornado.web
import tornado.ioloop
import json
import asyncio


class mainRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fh = open("list.txt", "r")
        fruits = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits))

    def post(self):
        fruit = self.get_argument("fruit")
        fh = open("list.txt", "a")
        fh.write(f"{fruit}\n")
        fh.close()
        self.write(json.dumps({"message": "Fruit added successfully."}))


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", mainRequestHandler),
        (r"/list", listRequestHandler),
    ])

    port = 8882
    app.listen(port)
    print(f"Application ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
