# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = "product.product"

    



    def ar_total_tax(self):
        if self.taxes_id:
              return self.list_price * 0.15

    def total_amount_tax(self):
        if self.taxes_id:
            list = self.list_price * 0.15
            # return self.list_price + list
            return self.env.user.company_id.currency_id.name + str(round(self.list_price + list))

    def company_name(self):
        return self.env.user.company_id.name


    @api.depends('including_price','list_price')
    def onchange_including_price(self):
        if self.including_price:
            print('frtgrtr',self)
            tax_value =  self.including_price * 15 /(115)
            self.list_price = self.including_price-tax_value
            # return self.including_price-tax_value





class ProductTemplate(models.Model):
    _inherit = "product.template"


    including_price = fields.Float(string='Including Tax')
    no_of_barcodes = fields.Integer(string='No Of Barcodes')





    @api.depends('including_price','list_price')
    def onchange_including_price(self):
        if self.including_price:
            print('frtgrtr')
            tax_value =  self.including_price * 15 /(115)
            self.list_price = self.including_price-tax_value
            # return self.including_price-tax_value


    def ar_total_tax(self):
        if self.taxes_ids:
              return self.list_price * 0.15
    def total_amount_tax(self):
        if self.taxes_ids:
            list = self.list_price * 0.15
            return self.env.user.company_id.currency_id.name + str(round(self.list_price + list))

