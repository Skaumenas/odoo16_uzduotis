from odoo import fields, models


class Dokumentas(models.Model):
    _name = "rastines.dokumentas"
    pavadinimas = fields.Char(string="Pavadinimas", required=True)
    aprasymas = fields.Text(string="Aprasymas")
    imone_id = fields.Many2one(comodel_name='res.company', string='Įmonė', required=True)
