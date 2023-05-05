from odoo import models, fields
class plane_avio(models.Model):
    _name = 'plane.avio'
    codi = fields.Integer('Codi', requiered=True)
    imatge = fields.Char('Imatge')
    marca = fields.Integer('marca')
    model = fields.Char('Model')
    maxVel = fields.Float('Maxima Velocitat')