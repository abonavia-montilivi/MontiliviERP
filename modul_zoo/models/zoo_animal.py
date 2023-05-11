from odoo import models, fields
class zoo_animal(models.Model):
    _name = 'zoo.animal'
    continentOrigen = fields.Char('Continent Origen')
    dataNaix = fields.Date('Data de naixement')
    paisOrigen = fields.Char('Pais Origen')
    sexe = fields.Char('Sexe')