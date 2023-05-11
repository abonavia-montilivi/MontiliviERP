from odoo import models, fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    passatgers = fields.Integer('Passatgers')
    dataSortida = fields.DateTime('Data Sortida')
    dataArrivada = fields.DateTime('Data Arrivada')
    