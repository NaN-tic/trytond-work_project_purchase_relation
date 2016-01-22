# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelSQL, fields
from trytond.pool import PoolMeta

__all__ = ['Work', 'WorkPurchaseLine']
__metaclass__ = PoolMeta


class Work:
    __name__ = 'work.project'

    purchases = fields.Function(fields.One2Many('purchase.purchase', None,
            'Purchases'), 'get_purchases', searcher='search_purchases')
    purchase_lines = fields.Many2Many('work.project-purchase.line',
        'work', 'purchase_line', 'Purchase Lines',
        readonly=True)

    def get_purchases(self, name):
        return list(set([pl.purchase.id for pl in self.purchase_lines]))

    @classmethod
    def search_purchases(cls, name, clause):
        return [('purchase_lines.purchase.id',) + tuple(clause[1:])]


class WorkPurchaseLine(ModelSQL):
    'Work Project - Purchase Line'
    __name__ = 'work.project-purchase.line'
    purchase_line = fields.Many2One('purchase.line', 'Purchase Line',
        required=True, select=True, ondelete='CASCADE')
    work = fields.Many2One('work.project', 'Work Project', required=True,
        select=True, ondelete='CASCADE')
