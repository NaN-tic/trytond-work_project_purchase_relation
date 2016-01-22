#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Purchase', 'PurchaseLine']
__metaclass__ = PoolMeta


class Purchase:
    __name__ = 'purchase.purchase'

    work_projects = fields.Function(fields.One2Many('work.project', None,
            'Work Projects'),
        'get_work_projects', searcher='search_work_projects')

    def get_work_projects(self, name):
        return list(set([w.id for l in self.lines for w in l.work_projects]))

    @classmethod
    def search_work_projects(cls, name, clause):
        return [('lines.work_projects',) + tuple(clause[1:])]


class PurchaseLine:
    __name__ = 'purchase.line'

    work_projects = fields.Many2Many('work.project-purchase.line',
        'purchase_line', 'work', 'Work Projects')
