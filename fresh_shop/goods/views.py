from django.shortcuts import render

from goods.models import GoodsCategory, Goods


def index(request):
    if request.method == 'GET':
        # 如果访问首页，返回渲染的首页index.html页面
        # 思路: 组装结果[object1, object2, object3, object4, object5, object6]
        # 组装结果的对象object: 包含分类，该分类的前四个商品信息
        # 方式1: object==> [GoodsCategory Object, [Goods objects1, Goods objects2, Goods objects3, Goods objects4]]
        # 方式2: object==> {'category_name': [Goods objects1, Goods objects2, Goods objects3, Goods objects4]}
        categorys = GoodsCategory.objects.all()
        result = []
        for category in categorys:
            goods = category.goods_set.all()[:4]
            data = [category, goods]
            result.append(data)
        category_type = GoodsCategory.CATEGORY_TYPE
        return render(request, 'index.html',
                      {'result': result, 'category_type': category_type})


def detail(request, id):
    if request.method == 'GET':
        # 返回详情页面解析的商品信息
        goods = Goods.objects.filter(pk=id).first()
        return render(request, 'detail.html', {'goods': goods})
