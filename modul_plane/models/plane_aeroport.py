from odoo import models, fields
class plane_aeroport(models.Model):
    _name = 'plane.aeroport'
    codi = fields.Integer('Codi', requiered=True)
    nom = fields.Char('Nom')
    imatge = fields.Char('Imatge')
    ciutat = fields.Char('Ciutat')
    pais = fields.Char('Pais')
    latitud = fields.Float('Latitud')
    longitud = fields.Float('Longitud')