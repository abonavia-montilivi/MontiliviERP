from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    id = fields.Integer('Id', requiered=True)
    familia = fields.Char('Familia')
    nomCientific = fields.Char('Nom Cientific')
    nomVulgar = fields.Char('Nom Vulgar')
    perill = fields.Boolean('Perill')

    animal_ids=fields.One2many('zoo.animal','especie_id',string='Animals')
