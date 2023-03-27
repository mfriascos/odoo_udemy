# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CustomSaleOrder(models.Model):
    
    _inherit = 'sale.order'

    zone = fields.Selection([
        ('N', 'North'),
        ('C', 'Central'),
        ('S', 'South'),
    ], string='Commercial Zone')