import json
from django.views.generic.base import View
from . models import Phb
from django.http import HttpResponse,JsonResponse
class IndexView(View):
    def post(self,request):
        content = request.body.decode()
        data = json.loads(content)
        username=data['user']
        grade=data['grade']
        users=Phb.objects.filter(user=username)
        if users:
            user=users.first()
            user.grade=grade
            user.save()
            return HttpResponse('上传成功')
        else:
            user=Phb()
            user.user=username
            user.grade=grade
            user.save()
            return HttpResponse('上传成功')
class SelectView(View):
    def post(self,request):
        active_user_detail = {}
        total_li=[]
        total_dic = {}
        index=1
        content = request.body.decode()
        data = json.loads(content)
        username = data['user']
        range=data['range']
        if range=='0':
            users=Phb.objects.all().order_by('-grade')
        else:
            start=int(range.split('~')[0])
            end=int(range.split('~')[1])
            users=Phb.objects.all().order_by('-grade')[start:end]
        for user in users:
            print(users)
            dic = {}
            dic['排名'] = index
            dic['客户端'] = user.user
            dic['分数'] = user.grade
            total_li.append(dic)
            if user.user == username:
                active_user_detail['排名'] = index
                active_user_detail['客户端'] = user.user
                active_user_detail['分数'] = user.grade
            index += 1
        total_li.append(active_user_detail)
        total_dic['查询结果'] = total_li
        return JsonResponse(total_dic)



