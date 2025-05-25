import asyncio
import tornado
import tornado.web
import time
import os

import tornado.escape
from tornado.escape import json_encode, json_decode

settings = {
    "static_path": os.path.join(os.path.dirname(__file__),"static"),
    "debug": True,
}


from PCA9685 import PCA9685
pwm = PCA9685(0x41)
pwm.setPWMFreq(50)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.time_now = time.time()
        self.render("template/index.html")

class ActionsAPIHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def post(self):
        actions_str = self.get_argument("actions_str","{\"servo_data\":[]}")
        actions = json_decode(actions_str)
        for item in actions.get("servo_data",[]):
            rotate = item[0]
            time_sleep = int(item[1]/1000)
            if time_sleep<=1:
                time_sleep = 1
            pwm.setServoPulse(0,rotate)
            print("rotate:%s, sleep:%s"%(rotate,time_sleep))
            time.sleep(time_sleep)
        self.finish({
            "info":"ok",
            "about":"success"
        })

def make_app():
    return tornado.web.Application([
        (r"/api/actions", ActionsAPIHandler),
        (r"/", MainHandler),
    ],**settings)

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())