from odoo import models, fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    passatgers = fields.Integer('Passatgers')
    dataSortida = fields.Datetime('Data Sortida')
    dataArrivada = fields.Datetime('Data Arrivada')
    

    pilot_id = fields.Many2one('plane.pilot', string='Pilots')
    avio_id = fields.Many2one('plane.avio', string='Avions')
    desti_id = fields.Many2one('plane.aeroport', string='Desti')
    origen_id = fields.Many2one('plane.aeroport', string='Origen')
    #