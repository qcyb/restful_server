# django 库
from rest_framework.views import APIView
from rest_framework.response import Response
# 第三方库
# 项目库


# /ping
class PingView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        return Response()
