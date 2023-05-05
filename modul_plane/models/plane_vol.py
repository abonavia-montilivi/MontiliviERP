from odoo import models, fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    codi = fields.Integer('Codi', requiered=True)
    passatgers = fields.Integer('Passatgers')
    dataSortida = fields.Date('Data Sortida')
    dataArrivada = fields.Date('Data Arrivada')
    