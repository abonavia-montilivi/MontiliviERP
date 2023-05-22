from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    name = fields.Char(compute='_get_name', string="Nom complet", readonly='True', store=False)    
    familia = fields.Char('Familia')
    nomCientific = fields.Char('Nom Cientific')
    nomVulgar = fields.Char('Nom Vulgar')
    perill = fields.Boolean('Perill')

    animal_ids = fields.One2many('zoo.animal','especie_id', string='Animals')

    def _get_name(self):
        for record in self:
            record.name = str(record.nomVulgar) + " " + str(record.nomCientific)
