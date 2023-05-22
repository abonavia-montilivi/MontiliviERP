from odoo import models, fields
class plane_avio(models.Model):
    _name = 'plane.avio'
    name = fields.Char(compute='_get_name', string="Nom complet", readonly='True', store=False)
    imatge = fields.Char('Imatge')
    marca = fields.Integer('marca')
    model = fields.Char('Model')
    maxVel = fields.Float('Maxima Velocitat')

    vol_ids = fields.One2many('plane.vol','avio_id', string='Vols')

    def _get_name(self):
        for record in self:
            record.name = str(record.model) + " " + str(record.marca)