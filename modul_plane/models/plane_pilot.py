from odoo import models, fields
class plane_pilot(models.Model):
    _name = 'plane.pilot'
    nom = fields.Char('Nom')
    cognoms = fields.Char('Cognoms')
    nif = fields.Char('NIF')
    telf = fields.Char('Telf')
    email = fields.Char('Email')