# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .work import *
from .purchase import *


def register():
    Pool.register(
        Work,
        WorkPurchaseLine,
        Purchase,
        PurchaseLine,
        module='work_project_purchase_relation', type_='model')
