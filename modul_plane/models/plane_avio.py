from odoo import models, fields
class plane_avio(models.Model):
    _name = 'plane.avio'
    imatge = fields.Char('Imatge')
    marca = fields.Integer('marca')
    model = fields.Char('Model')
    maxVel = fields.Float('Maxima Velocitat')

    vol_ids = fields.One2many('plane.vol','avio_id', string='Vols')