from django.db import models
# 自己的库
from trade.user.models import User
from trade.order.models import Orders


# 用户免费资源
class Resource(models.Model):
    class Meta:
        db_table = 'resource'

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    expired_at = models.DateTimeField(auto_now_add=True)    # ﻿auto_now_add only generated on 新创建
    updated_at = models.DateTimeField(auto_now=True)        # ﻿auto_now is generated on 每次修改


# 账本变更明细
class ResourceChange(models.Model):
    class Meta:
        db_table = 'resource_change'

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    orders = models.ForeignKey(Orders, null=False)
    before = models.DateTimeField()
    after = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)    # ﻿auto_now_add only generated on 新创建