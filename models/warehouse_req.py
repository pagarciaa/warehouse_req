from odoo import api, exceptions, fields, models, _

# TODO Check fields required


class WarehouseReq(models.Model):
    _name = 'warehouse.req'

    name = fields.Char(
        copy=False,
        default=lambda self: _('New'),
        index=True,
        string='Folio',
        readonly=True,
        required=True,
    )
    warehouse = fields.Many2one(
        comodel_name='stock.warehouse',
        required=True,
    )
    purchase_required = fields.Boolean(compute='_purchase_required')
    date_requested = fields.Date(
        default=fields.Date.today,
        readonly=True,
        string='Date of Request',
    )
    date_required = fields.Date()
    reason = fields.Selection(
        selection=[
            ('production', 'Production'),
            ('stock_cs', 'Stock CS'),
            ('loan', 'Loan'),
            ('warranty', 'Warranty'),
            ('sale', 'Sale'),
            ('reparation', 'Reparation'),
            ('replacement', 'Replacement'),
            ('internal', 'Internal Use'),
            ('integration', 'Integration'),
            ('minimal', 'Minimal Supplieres'),
        ],
        required=True,
    )
    reference_type = fields.Selection(
        selection=[
            ('support', 'Support'),
            ('kickoff', 'KickOff'),
            ('project', 'Project'),
            ('others', 'Others'),
            ('bill', 'Bill of Materials'),
        ],
    )
    reference_folio = fields.Integer()
    claimant_id = fields.Many2one(
        comodel_name='res.users',
        default=lambda self: self.env.uid,
        readonly=True,
        required=True,
        string='Claimant',
    )
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('required', 'Required'),
            ('approved', 'Approved'),
            ('done', 'Done'),
            # TODO verify status
        ]
    )
    shipping_type = fields.Selection(
        selection=[
            ('next', 'Next day'),
            ('other', 'Other'),
        ],
    )
    client_id = fields.Many2one(
        comodel_name="res.partner",
        domain="[('customer', '=', True)]",
        string='Client',
    )
    deliver_to = fields.Char()  # TODO field type
    deliver_address = fields.Char()  # TODO field type
    product_ids = fields.One2many(
        comodel_name='warehouse.req.product',
        inverse_name='warehouse_req_id',
        string='Products',
    )

    def _purchase_required(self):
        pass  # TODO

    @api.constrains('date_required')
    def _check_date_required_ge_date_requested(self):
        for r in self:
            if r.date_required and r.date_required < r.date_requested:
                raise exceptions.ValidationError(_("The date of requirement cannot be lower than the date of requestment"))

    @api.multi
    def action_draft(self):
        self.state = 'draft'

    @api.multi
    def action_require(self):
        self.state = 'required'

    @api.multi
    def action_approve(self):
        self.state = 'approved'

    @api.multi
    def action_done(self):
        self.state = 'self'

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('warehouse.req')
        return super(WarehouseReq, self).create(vals)
