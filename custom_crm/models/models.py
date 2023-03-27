# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
import logging

_logger = logging.getLogger(__name__)

class Visit(models.Model):
    _name = 'custom_crm.visit'
    _description = 'Visit'

    name = fields.Char(string='Description')
    customer = fields.Many2one(string='Customer', comodel_name='res.partner')
    date = fields.Datetime(string='Date')
    type = fields.Selection([
        ('O','OnSite'),
        ('W','Whatsapp'),
        ('P','Phone'),
    ], string='Type', required=True)
    done = fields.Boolean(string='Done', default=False)
    image = fields.Binary(string='Image')

    @api.model
    def create_orm_test(self):
        visit = {
            'name': 'ORM test',
            'customer': 1,
            'date': fields.Date.today(),
            'type': 'O',
            'done': False
        }
        _logger.debug('Creating ORM test record: %s', visit)
        self.env['custom_crm.visit'].create(visit)

    @api.model
    def search_update_orm_test(self):
        visit = self.env['custom_crm.visit'].search([('name','=','ORM test')], limit=1)
        _logger.debug('Searching for ORM test record: %s', visit.name)

        visit.write({
            'name': 'ORM Test Write'
        })

    @api.model
    def delete_orm_test(self):
        visit = self.env['custom_crm.visit'].search([('name','=','ORM test')], limit=1)
        visit.unlink()
        _logger.debug('Deleted ORM test record')
