# -*- coding: utf-8 -*-
############################################################################
#    Coded by: Humanytek-Team (https://github.com/humanytek-team)
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Warehouse Req',
    'version': '1.1',
    'author': 'Humanytek',
    'website': 'http://humanytek.com',
    'depends': [
        'purchase',
        'stock',
    ],
    'data': [
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
        'security/warehouse_req_access_rules.xml',
        'views/warehouse_req.xml',
        'workflows/warehouse_req_workflow.xml',
    ]
}
