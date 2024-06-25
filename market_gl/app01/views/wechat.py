from rest_framework.views import APIView
from rest_framework.response import Response


class WechatView(APIView):

    def post(self, request, *args, **kwargs):
        # 获取 POST 请求中的数据
        data = request.data
        print(data)
        # 返回一个包含消息的字典作为响应
        return Response({"message": "ok!"})
