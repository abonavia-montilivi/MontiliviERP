from odoo import models, fields
class zoo_zoo(models.Model):
    _name = 'zoo.zoo'
    id = fields.Integer('Id', requiered=True)
    grandaria = fields.Float('Float')
    nom = fields.Char('Nom')
    ciutat = fields.Char('Ciutat')
    pais = fields.Char('Pais')