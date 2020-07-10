# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/7/10 0010 下午 4:03
# Tool ：PyCharm

from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

# 简单的创建出很多的数据来试验
USER_LIST = []
for i in range(1, 999):
    temp = {'name': 'root' + str(i), 'age': i}
    USER_LIST.append(temp)


def index1(request):
    # 全部数据：USER_LIST，=》得出共有多少条数据
    # per_page: 每页显示条目数量
    # count:    数据总个数
    # num_pages:总页数
    # page_range:总页数的索引范围，如: (1,10),(1,200)
    # page:     page对象（是否具有下一页；是否有上一页；）
    current_page = request.GET.get('p')

    if current_page ==None:
        current_page=1
    else:
        current_page=int(current_page)
    # Paginator对象
    paginator = Paginator(USER_LIST, 10)  # 一页放10个数据

    # 加判断当总页数大于10页 让一部分不显示出来
    if paginator.num_pages > 10:
        if current_page - 5 < 1:
            posts_list = range(1, 11)
        elif current_page + 5 > paginator.num_pages:
            posts_list = range(current_page - 5, paginator.num_pages + 1)
        else:
            posts_list = range(current_page - 5, current_page + 5)
    else:
        # 当小于等于10页时全部显示
        posts_list = paginator.page_range

    try:
        # Page对象
        posts = paginator.page(current_page)
        # has_next              是否有下一页
        # next_page_number      下一页页码
        # has_previous          是否有上一页
        # previous_page_number  上一页页码
        # object_list           分页之后的数据列表，已经切片好的数据
        # number                当前页
        # paginator             paginator对象
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'index1.html', {'posts': posts, "posts_list": posts_list})

